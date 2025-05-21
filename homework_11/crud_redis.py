import uuid
from datetime import datetime, timezone
from typing import Dict, Optional

import redis


def get_redis_client() -> redis.Redis:
    """
    Создаёт и возвращает клиент Redis с параметрами подключения по умолчанию.

    :return: Redis клиент
    """
    return redis.Redis(
        host='localhost',
        port=6379,
        db=0,
        decode_responses=True
    )


def create_session(user_id: int) -> str:
    """
    Создаёт сессию для пользователя, генерирует уникальный токен и сохраняет данные в Redis.
    Устанавливает TTL для сессии 30 минут (1800 секунд).

    :param user_id: ID пользователя
    :return: сессионный токен
    """
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
    red_.expire(key, 1800)
    return session_token


def get_session(user_id: int) -> Dict[str, Optional[str]]:
    """
    Получает данные сессии пользователя из Redis.

    :param user_id: ID пользователя
    :return: словарь с данными сессии (ключи: session_token, login_time, last_active_time)
             или пустой словарь, если сессия не найдена
    """
    r = get_redis_client()
    return r.hgetall(f"session:{user_id}")


def update_last_active(user_id: int) -> None:
    """
    Обновляет поле last_active_time текущим временем UTC и продлевает TTL сессии на 30 минут.

    :param user_id: ID пользователя
    """
    r = get_redis_client()
    now = datetime.now(timezone.utc).isoformat()
    key = f"session:{user_id}"
    r.hset(key, "last_active_time", now)
    r.expire(key, 1800)


def delete_session(user_id: int) -> None:
    """
    Удаляет сессию пользователя из Redis.

    :param user_id: ID пользователя
    """
    r = get_redis_client()
    print("delete session:", user_id)
    r.delete(f"session:{user_id}")


# Пример использования:
red_ = get_redis_client()
session_token = create_session(1)
delete_session(1)
