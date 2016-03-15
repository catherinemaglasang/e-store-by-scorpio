import os
import json
import app
import unittest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config import config
Session = sessionmaker()


class ProductTestCase(unittest.TestCase):
    """ Test api """

    def setUp(self):
        # Use configs for testing environment
        app.app.config.from_object(config['testing'])

        # connect to the database using sqlalchemy engine
        engine = create_engine("%s" % (app.app.config['DATABASE']), echo=False)
        self.connection = engine.connect()
        self.trans = self.connection.begin()
        # self.cursor = self.connection.cursor()

        # Reset and setup db
        # self.cursor.execute("""DROP TABLE products;""")
        # self.cursor.execute("""CREATE TABLE products;""")

        self.session = Session(bind=self.connection)
        self.app = app.app.test_client()

    def tearDown(self):
        self.trans.rollback()
        self.connection.close()

    def check_content_type(self, headers):
        self.assertEqual(headers['Content-Type'], 'application/json')

    def test_home(self):
        rv = self.app.get('/')
        resp = json.loads(rv.data)
        self.assertEqual(resp['status'], 'ok')

    def test_empty_db(self):

        # Get all products in db
        rv = self.app.get('/api/v1/products/')
        resp = json.loads(rv.data)

        self.check_content_type(rv.headers)
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(resp['status'], 'ok')

        # Make sure that it returns proper message if no entries are found
        if len(resp['entries']) == 0:
            self.assertEqual(resp['message'], 'No entries found')
            self.assertEqual(resp['count'], '0')
            self.assertEqual(len(resp['entries']), 0)

        # Get single product in db
        rv = self.app.get('/api/v1/products/')
        resp = json.loads(rv.data)

        self.check_content_type(rv.headers)
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(resp['status'], 'ok')

        # Make sure that it returns proper message if no entries are found
        if len(resp['entries']) == 0:
            self.assertEqual(resp['message'], 'No entries found')
            self.assertEqual(resp['count'], '0')
            self.assertEqual(len(resp['entries']), 0)

    def test_invalid_product_id(self):
        rv = self.app.get('/api/v1/products/abcxyz')
        self.assertRaises(AttributeError)

    def test_create_product(self):
        data = {
            'product_id': '1',
            'title': 'Product Name',
            'description': 'Product Description',
            'date_added': '1/1/1 1:1:1',
            'ordering': '0',
            'supplier_id': '1',
            'category_id': '1',
            'site_id': '1',
            'product_type_id': '1',
            # 'product_attributes': [
            #     {'isbn': 'isbn1'},
            #     {'author': 'author1'},
            # ]
            'on_hand': '100',
            're_order_level': '10',
            'is_active': 'True'
        }
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        rv = self.app.post("/api/v1/products/",
                           headers=headers,
                           data=json.dumps(data))

        self.check_content_type(rv.headers)
        self.assertEqual(rv.status_code, 201)

    def test_create_existing_product(self):
        data = {
            'product_id': '1',
            'title': 'Product Name',
            'description': 'Product Description',
            'date_added': '1/1/1 1:1:1',
            'ordering': '0',
            'supplier_id': '1',
            'category_id': '1',
            'site_id': '1',
            'product_type_id': '1',
            # 'product_attributes': [
            #     {'isbn': 'isbn1'},
            #     {'author': 'author1'},
            # ]
            'on_hand': '100',
            're_order_level': '10',
            'is_active': 'True'
        }
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        rv = self.app.post("/api/v1/products/",
                           headers=headers,
                           data=json.dumps(data))

        self.check_content_type(rv.headers)
        self.assertEqual(rv.status_code, 201)

        data_json = json.loads(rv.data)
        self.assertEqual(data_json['status'], 'ok')
        self.assertEqual(data_json['message'], 'id exists')

    def test_update_product(self):
        old_product = self.app.get("/api/v1/products/1/")
        response = json.loads(old_product.data)
        product_id = response['entries'][0].product_id
        print product_id

    def test_get_product(self):
        pass

# Sources: http://mkelsey.com/2013/05/15/test-driven-development-of-a-flask-api/
