"""This module has the db connection"""

import os
import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    '''Class for database connection'''
    conn = None
    cursor = None
    app = None

    def init_app(self, app):
        '''create the database connection'''
        self.app = app
        self.conn = psycopg2.connect(
        	dbname="db5h1pj6grd382",
        	user="ccsndmujpnfgbg",
        	host="ec2-107-22-164-225.compute-1.amazonaws.com",
        	password="90f4121b74b520f6aaf1bed892b72549319df7f0809833edcf60390a45227e0e"
        	)
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)