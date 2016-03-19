import json
import unittest
from app import create_app


class ProductTestCase(unittest.TestCase):
    """ Test api """

    def setUp(self):
        # Use configs for testing environment
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def check_content_type(self, headers):
        self.assertEqual(headers['Content-Type'], 'application/json')

    def test_home(self):
        rv = self.client.get('/')
        print rv
        resp = json.loads(rv.data)
        self.assertEqual(resp['status'], 'ok')

    def test_empty_db(self):

        # Get all products in db
        rv = self.client.get('/api/v1/products/')
        resp = json.loads(rv.data)

        self.check_content_type(rv.headers)
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(resp['status'], 'ok')

        # Make sure that it returns proper message if no entries are found
        if len(resp['entries']) == 0:
            self.assertEqual(resp['message'], 'No entries found')
            self.assertEqual(resp['count'], '0')
            self.assertEqual(len(resp['entries']), 0)

        self.check_content_type(rv.headers)
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(resp['status'], 'ok')

        # Make sure that it returns proper message if no entries are found
        if len(resp['entries']) == 0:
            self.assertEqual(resp['message'], 'No entries found')
            self.assertEqual(resp['count'], '0')
            self.assertEqual(len(resp['entries']), 0)

    def test_invalid_product_id(self):
        rv = self.client.get('/api/v1/products/abcxyz')
        self.assertRaises(AttributeError)

    def test_create_product(self):
        data = {
            'product_id': '100',
            'title': 'Product Name',
            'description': 'Product Description',
            'date_added': '1/1/1 1:1:1',
            'ordering': '0',
            'supplier_id': '1',
            'category_id': '1',
            'site_id': '1',
            'product_type_id': '1',
            'on_hand': '100',
            're_order_level': '10',
            'is_active': 'True'
        }
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        rv = self.client.post("/api/v1/products/",
                           headers=headers,
                           data=json.dumps(data))

        self.check_content_type(rv.headers)
        print json.loads(rv.data)
        # self.assertEqual(json.loads(rv.data), 'ok')
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
            'on_hand': '100',
            're_order_level': '10',
            'is_active': 'True'
        }
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        rv = self.client.post("/api/v1/products/",
                           headers=headers,
                           data=json.dumps(data))

        self.check_content_type(rv.headers)
        self.assertEqual(rv.status_code, 201)

        data_json = json.loads(rv.data)
        self.assertEqual(data_json['status'], 'ok')
        self.assertEqual(data_json['message'], 'id exists')

    def test_update_product(self):
        new_product = {
            'product_id': '1',
            'title': 'NEWNEW Product Name',
            'description': 'NEW  Product Description',
            'date_added': '1/1/1 1:1:1',
            'ordering': '0',
            'supplier_id': '1',
            'category_id': '1',
            'site_id': '1',
            'product_type_id': '1',
            'on_hand': '100',
            're_order_level': '10',
            'is_active': 'True'
        }
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        rv = self.client.put("/api/v1/products/1/", headers=headers, data=json.dumps(new_product))
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(json.loads(rv.data)['status'], 'ok')

# Sources: http://mkelsey.com/2013/05/15/test-driven-development-of-a-flask-api/
