import psycopg2
from psycopg2.extensions import AsIs

from src.settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USERNAME


class DatabasePipeline:
    def __init__(self):
        self.conn = psycopg2.connect(
            database=DB_NAME,
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USERNAME,
            password=DB_PASSWORD,
        )

        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        self.cur.execute(
            """insert into %s (name) values (%s)""", (
                AsIs(spider.name),
                item["name"],
            ),
        )

        self.conn.commit()

    def close_spider(self, _):
        self.cur.close()
        self.conn.close()
