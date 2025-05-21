from typing import Tuple
from pymongo.database import Database
from pymongo.mongo_client import MongoClient


def get_db() -> Tuple[Database, MongoClient]:
    """
    Создаёт подключение к MongoDB и возвращает объект базы данных и клиента.

    :return: Кортеж из (объект базы данных 'online_store', MongoClient)
    """
    client = MongoClient('mongodb://localhost:27017')
    db = client['online_store']
    return (db, client)
