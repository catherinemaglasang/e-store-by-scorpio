import json
from unittest import TestCase
import app


class ProductTestCase(TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_new_product(self):
        self.assertEqual(5,5)
        self.assertAlmostEqual(1, 1.0001, places=4)
        self.assertRaises(AttributeError)
