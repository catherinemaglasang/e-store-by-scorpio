from sqlalchemy import create_engine
from flask import current_app as app


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
                print app.config['TESTING']
                dbo.rollback_transaction()

        return res
    except:
        res = [("Error: " + str(sys.exc_info()[0]) + " " + str(sys.exc_info()[1]),)]
    return res
