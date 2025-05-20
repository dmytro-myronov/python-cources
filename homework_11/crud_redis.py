import uuid
from datetime import datetime, timezone


import redis

def get_redis_client():
    return redis.Redis(
        host='localhost',
        port=6379,
        db=0,
        decode_responses=True
    )


def create_session(user_id):
    session_token = str(uuid.uuid4())
    login_time = datetime.now(timezone.utc).isoformat()
    red_ = get_redis_client()
    key = f"session:{user_id}"
    red_.hset(key, mapping={
        "session_token": session_token,
        "login_time": login_time,
        "last_active_time": login_time
    })
    print("set session key:", key)
    # TTL: 30 хвилин (1800 секунд)
    red_.expire(key, 1800)

    return session_token


def get_session(user_id):
    r = get_redis_client()
    return r.hgetall(f"session:{user_id}")

def update_last_active(user_id):
    r = get_redis_client()
    now = datetime.now(timezone.utc).isoformat()
    key = f"session:{user_id}"
    r.hset(key, "last_active_time", now)
    r.expire(key, 1800)

def delete_session(user_id):
    r = get_redis_client()
    print("delete session:", user_id)
    r.delete(f"session:{user_id}")


red_ = get_redis_client()
session = create_session(1)
delete_session(session)