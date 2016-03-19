import json
from app.models import spcall

class Base:
    def get(self):
        pass

    def save(self):
        pass

    def put(self):
        pass

class Product(Base):
    def __init__(self):
        self.product_id = ''
        self.title = ''
        self.description = ''
        self.date_added = ''
        self.ordering = ''
        self.supplier_id = ''
        self.category_id = ''
        self.site_id = ''
        self.product_type_id = ''
        # TODO: Include product attributes
        self.on_hand = ''
        self.re_order_level = ''
        self.is_active = ''

    def save(self):
        response = spcall('new_product', (
        self.product_id,
        self.title,
        self.description,
        self.date_added,
        self.ordering,
        self.supplier_id,
        self.category_id,
        self.site_id,
        self.product_type_id,
        self.on_hand,
        self.re_order_level,
        self.is_active), True)

        if 'Error' in response[0][0]:
            response = {'status': 'error', 'message': response[0][0]}
        else:
            response = {'status': 'ok', 'message': response[0][0]}

        return response

    def get(id=None):
        response =

    def from_json(self, _json):
        """ This function converts the json sent by the client to dictionary so that the server
        may be able to process it.
        """
        data = json.loads(_json)
        self.product_id = data['product_id']
        self.title = data['title']
        self.description = data['description']
        self.date_added = data['date_added']
        self.ordering = data['ordering']
        self.supplier_id = data['supplier_id']
        self.category_id = data['category_id']
        self.site_id = data['site_id']
        self.product_type_id = data['product_type_id']
        self.on_hand = data['on_hand']
        self.re_order_level = data['re_order_level']
        self.is_active = data['is_active']
        return data
