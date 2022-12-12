import psycopg2
from psycopg2.extensions import AsIs

from src.settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USERNAME


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            database=DB_NAME,
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USERNAME,
            password=DB_PASSWORD,
        )
        self.cur = self.conn.cursor()

    def fetch_all_genres(self):
         self.cur.execute(
            """SELECT id, name FROM (%s)""", (
                AsIs('genres'),
            ),
        )

    def insert_name(self, table, name):
        self.cur.execute(
            """INSERT INTO %s (name) values (%s)""", (
                AsIs(table),
                name,
            ),
        )
        self.conn.commit()

    def fetch_genre_by_name(self, name):
        self.cur.execute(
            """SELECT id, name FROM %s WHERE name=%s""", (
                AsIs('genres'),
                name,
            ),
        )

        return self.cur.fetchone()

    def insert_subgenre(self, table, name, genre_id):
        self.cur.execute(
            """INSERT INTO %s (name, genre_id) values (%s, %s)""", (
                AsIs(table),
                name,
                genre_id,
            ),
        )
        self.conn.commit()

    def insert_album(self, name, artist_id, genre_id):
        self.cur.execute(
            """INSERT INTO %s (name, artist_id, genre_id) values (%s, %s, %s)""", (
                AsIs('albums'),
                name,
                artist_id,
                genre_id,
            ),
        )
        self.conn.commit()

    def insert_song(self, table, name, artist_id, album_id):
        self.cur.execute(
            """INSERT INTO %s (name, artist_id, album_id) values (%s, %s, %s)""", (
                AsIs(table),
                name,
                artist_id,
                album_id,
            ),
        )
        self.conn.commit()


    def fetch_artist_by_name(self, name):
        self.cur.execute(
            """SELECT id, name FROM %s WHERE name=%s""", (
                AsIs('artists'),
                name,
            ),
        )

        return self.cur.fetchone() or (None, None)

    def fetch_album_by_name(self, name):
        self.cur.execute(
            """SELECT id, name FROM %s WHERE name=%s""", (
                AsIs('albums'),
                name,
            ),
        )

        return self.cur.fetchone() or (None, None)


    def insert_artist(self, name, genre_id):
        self.cur.execute(
            """INSERT INTO %s (name, genre_id) values (%s, %s)""", (
                AsIs('artists'),
                name,
                genre_id,
            ),
        )
        self.conn.commit()
