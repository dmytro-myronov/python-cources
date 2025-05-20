from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])  # IP адреса кластера Cassandra
session = cluster.connect()

# Створення keyspace (бази даних) з простою стратегією реплікації
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS logs_keyspace
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'}
""")

# Використовуємо створений keyspace
session.set_keyspace('logs_keyspace')

# Створення таблиці логів подій
session.execute("""
    CREATE TABLE IF NOT EXISTS event_logs (
        event_id UUID PRIMARY KEY,
        user_id UUID,
        event_type text,
        timestamp timestamp,
        metadata text
    )
""")
