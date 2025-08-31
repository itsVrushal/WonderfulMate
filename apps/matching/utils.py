# Simple matching utilities and a placeholder for embedding operations.
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from geopy.distance import great_circle
from django.conf import settings


model = SentenceTransformer('all-MiniLM-L6-v2')


def embed_text(text: str):
    if not text:
        return np.zeros((384,))
    return model.encode(text, convert_to_numpy=True)


def text_cosine(a: np.ndarray, b: np.ndarray) -> float:
    if a is None or b is None:
        return 0.0
    return float(cosine_similarity(np.array([a]), np.array([b]))[0][0])



def location_similarity(loc1, loc2, radius_km=50):
    if not loc1 or not loc2:
        return 0.0
    dist = great_circle(loc1, loc2).km
    return max(0.0, 1 - (dist / radius_km))


def behavioral_similarity(t1, t2):
    # normalize differences into [0,1]
    d_resp = abs(t1.get('avg_response_time',10)-t2.get('avg_response_time',10))
    d_len = abs(t1.get('avg_msg_length',20)-t2.get('avg_msg_length',20))
    score = 1 / (1 + d_resp + 0.1 * d_len)
    return float(score)