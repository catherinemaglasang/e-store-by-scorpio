from sqlalchemy import create_engine
import os
from app import app

class DBconn:
    def __init__(self):
        engine = create_engine("%s" % (app.config['DATABASE']), echo=False)
        self.conn = engine.connect()
        self.trans = self.conn.begin()

    def getcursor(self):
        cursor = self.conn.connection.cursor()
        return cursor

    def dbcommit(self):
        self.trans.commit()

    def rollback_transaction(self):
        self.trans.rollback()

