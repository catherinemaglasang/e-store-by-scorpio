import json
from unittest import TestCase
import app


class ProductTestCase(TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_new_product(self):
        self.fail()
