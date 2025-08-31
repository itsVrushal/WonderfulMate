# WonderfulMate

This repo contains a prototype Django backend scaffold for the WonderfulMate app. The code includes core models, serializers, basic views, and a Celery task to recompute recommendations.

## Quickstart

1. Create virtualenv & install requirements:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Setup DB (Postgres recommended) and update `settings.py` DATABASES.
3. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser:

```bash
python manage.py createsuperuser
```

5. Start Redis (for Celery) and run Celery worker:

```bash
redis-server
celery -A wonderfulmate worker -l info
```

6. Run Django server:

```bash
python manage.py runserver
```

### NOTES & NEXT STEPS

- This scaffold is intentionally minimal. Production-ready features to add:
- Proper authentication flows (email/phone verification)
- Rate limiting & WAF
- Background workers for heavy embedding operations
- Caching recommendations (Redis) + Recommendation model/table
- Extensive tests and CI/CD
- Privacy controls and abuse prevention (reporting/blocking)

# End of scaffold
