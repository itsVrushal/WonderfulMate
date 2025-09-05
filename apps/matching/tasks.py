from celery import shared_task # type: ignore
from .utils import embed_text, text_cosine, location_similarity, behavioral_similarity
from apps.users.models import UserProfile

@shared_task
def recompute_recommendations_for_user(user_id):
    """Compute top matches for a user and store into cache/table.
    This is a placeholder implementing the prototype scoring.
    """
    try:
        user = UserProfile.objects.select_related('telemetry').get(pk=user_id)
    except UserProfile.DoesNotExist:
        return
    users = UserProfile.objects.exclude(pk=user_id).select_related('telemetry')
    emb_u = embed_text(user.about or "")
    results = []
    for other in users:
        emb_o = embed_text(other.about or "")
        text_sim = text_cosine(emb_u, emb_o)
        interest_sim = 0.0
        try:
            a = set(user.interests or [])
            b = set(other.interests or [])
            interest_sim = len(a & b) / len(a | b) if (a|b) else 0
        except Exception:
            pass
        hobby_sim = 0.0
        try:
            a = set((user.hobbies or "").split(', '))
            b = set((other.hobbies or "").split(', '))
            hobby_sim = len(a & b) / len(a | b) if (a|b) else 0
        except Exception:
            pass
        location_sim = location_similarity(user.location_tuple(), other.location_tuple())
        behavior_sim = behavioral_similarity(getattr(user, 'telemetry').__dict__, getattr(other, 'telemetry').__dict__)
        score = 0.3*text_sim + 0.25*interest_sim + 0.15*hobby_sim + 0.2*location_sim + 0.1*behavior_sim
        results.append((other.pk, float(score)))
    # Sort and persist top-k; for prototype, store to a simple model or cache.
    results.sort(key=lambda x: x[1], reverse=True)
    topk = results[:50]
    # TODO: store in a Recommendation table or cache. For prototype, print.
    print(f"Top matches for {user_id}: {topk}")

from celery import shared_task

@shared_task
def test_task():
    print("✅ Celery is working!")
    return "hello"
