"""Redis session backend example"""
from django.conf import settings
import redis

def get_redis_connection():
    r = redis.StrictRedis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=0,
        decode_responses=True
    )
    return r
