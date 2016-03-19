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
        response = spcall('get_product', ())
        entries = []

        if len(response) == 0:
            return jsonify({"status": "ok", "message": "No entries found", "entries": [], "count": "0"})
        elif 'Error' in str(response[0][0]):
            return jsonify({'status': 'error', 'message': response[0][0]})
        else:
            for row in response:
                entries.append({"product_id": row[0],
                                "title": row[1],
                                "description": row[2],
                                "date_added": row[3],
                                "ordering": row[4],
                                "supplier_id": row[5],
                                "category_id": row[6],
                                "site_id": row[7],
                                "product_type_id": row[8],
                                "on_hand": row[9],
                                "re_order_level": row[10],
                                "is_active": row[11]})
            return jsonify({'status': 'ok', 'message': 'ok', 'entries': entries, 'count': len(entries)})

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
