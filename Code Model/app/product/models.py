class Product:
    def __init__(self, _product_id, ):
        self.product_id = _product_id
        self.title = _title
        self.description = _description
        self.date_added = _date_added
        self.ordering = _ordering
        self.supplier_id = _supplier_id
        self.category_id = _category_id
        self.site_id = _site_id
        self.product_type_id = _product_type_id

        self.on_hand = _on_hand
        self.re_order_level = _re_order_level
        self.is_active = _is_active

    def from_json(self, _json):
        data = json.loads(_json)
        return data
