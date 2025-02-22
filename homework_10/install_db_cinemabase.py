import sqlite3


def create_tables(db_name):
    conn = sqlite3.connect(db_name)

    cursor = conn.cursor()

    cursor.execute('''
   CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        release_year INTEGER,
        genre VARCHAR(255)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS actors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_year INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movie_cast (
        movie_id INTEGER,
        actor_id INTEGER,
        PRIMARY KEY(movie_id, actor_id),
        FOREIGN KEY(movie_id) REFERENCES movies(id),
        FOREIGN KEY(actor_id) REFERENCES actors(id)
    )
    ''')
    conn.commit()


