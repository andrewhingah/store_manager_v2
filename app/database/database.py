import psycopg2
import os
from psycopg2.extras import RealDictCursor


class Database:
    conn = None
    cursor = None
    app = None

    def init_app(self, app):
        self.app = app
        self.conn = psycopg2.connect(dbname=app.config['DATABASE_NAME'], user=os.getenv("user"), host=os.getenv("host"), password=os.getenv("password"))
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)