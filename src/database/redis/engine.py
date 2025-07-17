import redis.asyncio as redis
from celery import Celery
from src.config.setting import settings

redis_client = redis.Redis.from_url(settings.REDIS_URI)

celery_app = Celery(
  main="worker",
  broker=settings.REDIS_URI,
  backend=settings.REDIS_URI,
)

celery_app.autodiscover_tasks(['src.database.redis'])

