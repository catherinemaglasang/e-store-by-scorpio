import os
import psycopg2
import sys
from sqlalchemy import create_engine
from flask import current_app as app


class DBconn:
    """ This helper function will allow us to instantiate our database using sqlalchemy engine
    and use stored procedures defined in app.
    """

    def __init__(self):
        engine = create_engine("%s" % (app.config['DATABASE']), echo=False)
        # connect to the database
        self.conn = engine.connect()
        self.trans = self.conn.begin()

    def getcursor(self):
        # http://stackoverflow.com/questions/21158033/query-from-postgresql-using-python-as-dictionary
        cursor = self.conn.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return cursor

    def dbcommit(self):
        self.trans.commit()

    def rollback_transaction(self):
        self.trans.rollback()


def spcall(qry, param, commit=False):
    """ Stored procedure util function """
    try:
        dbo = DBconn()
        cursor = dbo.getcursor()
        cursor.callproc(qry, param)
        res = cursor.fetchall()
        if commit:
            dbo.dbcommit()

            # Rollback transaction if in testing environment
            if app.config['TESTING']:
                dbo.rollback_transaction()

        return res
    except:
        res = [("Error: " + str(sys.exc_info()[0]) + " " + str(sys.exc_info()[1]),)]
    return res
