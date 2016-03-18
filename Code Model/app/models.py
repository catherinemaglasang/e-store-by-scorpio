from sqlalchemy import create_engine
from app import app

# Define the attributes for each table. TODO: Refactor! Create class for each model, then instantiate.
tables = {'product': ['product_id', 'title', 'description', 'date_added', 'ordering', 'supplier_id', 'category_id',
                      'site_id', 'product_type_id', 'on_hand', 're_order_level', 'is_active']}


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
        cursor = self.conn.connection.cursor()
        return cursor

    def dbcommit(self):
        self.trans.commit()

    def commit_transaction(self):
        self.trans.commit()

    def close_transaction(self):
        self.trans.close()

    def initialize(self):
        engine = create_engine("%s" % (app.config['DATABASE']), echo=False)
        print app.config['DATABASE']
        # connect to the database
        self.conn = engine.connect()
        self.trans = self.conn.begin()

    def rollback_transaction(self):
        # http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html
        # self.session.close()

        # rollback - everything that happened with the
        # Session above (including calls to commit())
        # is rolled back.
        self.trans.rollback()

        # return connection to the Engine
        # self.conn.close()

    def call_procedure(self, qry, param, _resource, commit=False):
        """ This function calls the stored procedure function in database, and processes
        the output in a dictionary form which the view shall convert to json.
        :param param:
        :param qry:
        :param commit:
        :param _resource:
        :rtype: object
        """
        # bind an individual Session to the connection
        cursor = self.conn.connection.cursor()

        cursor.callproc(qry, param)

        # The ff line will return an array of tuples representing the rows in the result of the function call
        results = cursor.fetchall()

        if commit:
            self.trans.commit()

        out = {}

        # Process the results
        # Check if an error is in the results
        out['status'] = 'ok'
        out['message'] = 'ok'
        if len(results) == 0:
            # Check if length of rows is greater than zero.
            # Note that this should come first so that no errors should be generated.
            out['entries'] = []
            out['count'] = len(out['entries'])
        elif 'Error' in str(results[0][0]):
            # Check and return error by db
            out['status'] = 'error'
            out['message'] = results[0][0]
        else:
            out['entries'] = []
            for row in results:
                # Initialize item to be appended to entries
                item = {}

                # Query the resource (i.e. product, productType, etc.)
                resource = tables[_resource]
                attr_len = len(resource)

                # Set index to zero. TODO: Refactor!
                index = 0
                for col in row:
                    # Loop over every attribute in the resource, and assign the value in the
                    # results obtained from the spcall.
                    item[resource[index]] = col
                    index = index + 1

                # append item to entries
                out['entries'].append(item)
            out['count'] = len(out['entries'])
        return out
