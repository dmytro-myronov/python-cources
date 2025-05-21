from cassandra.cluster import Cluster, Session
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Any
import uuid
import json


def connect_cassandra(nodes: List[str]) -> Session:
    """
    Підключається до кластера Cassandra та повертає сесію.

    :param nodes: Список IP-адрес вузлів Cassandra.
    :return: Об'єкт сесії Cassandra.
    """
    cluster = Cluster(nodes)
    session = cluster.connect()
    return session


def setup_keyspace_and_table(session: Session) -> None:
    """
    Створює keyspace та таблицю logs, якщо вони не існують.

    :param session: Сесія Cassandra.
    """
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS event_logs WITH replication = {
            'class': 'SimpleStrategy',
            'replication_factor': 3
        }
    """)
    session.set_keyspace('event_logs')
    session.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            event_id UUID,
            user_id UUID,
            event_type text,
            timestamp timestamp,
            metadata text,
            PRIMARY KEY ((event_type), timestamp, event_id)
        ) WITH CLUSTERING ORDER BY (timestamp DESC)
    """)


def create_log(session: Session, user_id: uuid.UUID, event_type: str, metadata: Dict[str, Any]) -> Tuple[
    uuid.UUID, datetime]:
    """
    Додає новий лог події.

    :param session: Сесія Cassandra.
    :param user_id: UUID користувача.
    :param event_type: Тип події.
    :param metadata: Додаткові дані у вигляді словника.
    :return: Кортеж (event_id, timestamp) створеного запису.
    """
    event_id = uuid.uuid4()
    timestamp = datetime.utcnow()
    metadata_json = json.dumps(metadata)

    session.execute("""
        INSERT INTO logs (event_id, user_id, event_type, timestamp, metadata)
        VALUES (%s, %s, %s, %s, %s)
    """, (event_id, user_id, event_type, timestamp, metadata_json))

    return event_id, timestamp


def read_logs(session: Session, event_type: str) -> List[Dict[str, Any]]:
    """
    Отримує всі події певного типу за останні 24 години.

    :param session: Сесія Cassandra.
    :param event_type: Тип події.
    :return: Список подій у вигляді словників.
    """
    since = datetime.utcnow() - timedelta(days=1)
    query = """
        SELECT event_id, user_id, event_type, timestamp, metadata
        FROM logs
        WHERE event_type = %s AND timestamp > %s
        ALLOW FILTERING
    """
    rows = session.execute(query, (event_type, since))
    results = []
    for row in rows:
        results.append({
            'event_id': row.event_id,
            'user_id': row.user_id,
            'event_type': row.event_type,
            'timestamp': row.timestamp,
            'metadata': json.loads(row.metadata)
        })
    return results


def update_metadata(session: Session, event_type: str, timestamp: datetime, event_id: uuid.UUID,
                    new_metadata: Dict[str, Any]) -> None:
    """
    Оновлює metadata для певного event_id.

    :param session: Сесія Cassandra.
    :param event_type: Тип події.
    :param timestamp: Час події.
    :param event_id: UUID події.
    :param new_metadata: Нові дані metadata у вигляді словника.
    """
    metadata_json = json.dumps(new_metadata)
    session.execute("""
        UPDATE logs SET metadata = %s
        WHERE event_type = %s AND timestamp = %s AND event_id = %s
    """, (metadata_json, event_type, timestamp, event_id))


def delete_old_logs(session: Session) -> None:
    """
    Видаляє події старші за 7 днів.
    Для великих обсягів даних краще використовувати TTL.

    :param session: Сесія Cassandra.
    """
    threshold = datetime.utcnow() - timedelta(days=7)
    query = """
        SELECT event_type, timestamp, event_id FROM logs
        WHERE timestamp < %s ALLOW FILTERING
    """
    rows = session.execute(query, (threshold,))
    for row in rows:
        session.execute("""
            DELETE FROM logs
            WHERE event_type = %s AND timestamp = %s AND event_id = %s
        """, (row.event_type, row.timestamp, row.event_id))


if __name__ == "__main__":
    # Підключення
    session = connect_cassandra(['127.0.0.1'])
    setup_keyspace_and_table(session)

    user_id = uuid.uuid4()
    event_id, ts = create_log(session, user_id, 'login', {'ip': '192.168.1.1'})

    logs = read_logs(session, 'login')
    print(f"Знайдено логів: {len(logs)}")

    update_metadata(session, 'login', ts, event_id, {'ip': '192.168.1.2', 'device': 'mobile'})

    delete_old_logs(session)
