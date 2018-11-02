"""This module has the db connection"""

import os
import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    '''Class for database connection'''
    conn = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')
    cursor = None
    app = None

    def init_app(self, app):
        '''create the database connection'''
        self.app = app
        self.conn = conn
        # self.conn = psycopg2.connect(
        # 	dbname=app.config['DATABASE_NAME'],
        # 	user=os.getenv("user"),
        # 	host=os.getenv("host"),
        # 	password=os.getenv("password")
        # 	)
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)