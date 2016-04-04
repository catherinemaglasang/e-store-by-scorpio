User = {
  'user_id': '1',
  'username': 'username',
  'password': 'password',
  'email': 'roselle@gmail.com',
  'business_code': 'business123',
  'is_active': 'True',
  'date_created': '1/1/1',
  'date_confirmed': '1/1/1',
  'roles': ['admin', 'level1', 'level2'],
}

Customer = {
  'first_name': 'Roselle',
  'last_name': 'Ebarle',
  'user_id': '1',
  'title': 'MS, MR'
}

UserRole = [
  {
    'user_id': '1',
    'role_id': 'admin',
  },
  {
    'user_id': '1',
    'role_id': 'admin',
  }]

Role = {
  'role_id': '1',
  'name': 'admin',
  'description': 'Primary role needed to view dashboard. Each company owner will have admin access. Admin will be the paying user'.
}

Site = {
  'site_id': '1',
  'name': 'e-store',
  'code': 'S1',
  'domains': ['localhost:5000', 'store.com'],
  'is_default': 'true',
}

""" SiteVar table contains css settings """
SiteVariable = {
  'site_variable_id': '1',
  'key': 'Title',
  'value': 'Store',
  'site_id': '1',
}

SiteTracker = {
  """ Sample tracker is GA """
  'site_id': '1',
  'tracker_id': '1',

}

Product = {
  'product_id': '1',
  'title': 'Product Name',
  'description': 'Product Description',
  'date_added': '1/1/1 1:1:1',
  'ordering': '0',
  'supplier_id': '1',
  'category_id': '1',
  'site_id': '1',
  'product_type_id': '1',
  'product_attributes': [
    {'isbn': 'isbn1'},
    {'author': 'author1'},
  ],
  'on_hand': '0',
  're_order_level': '0',
  'is_active': 'true',
}

Category = {
  'category_id': '1',
  'name': 'Cat',
  'description': 'Desc',
  'site_id': '1',
}

Order = {
  'store_id': '1',
  'user_id': '1', # User who did the order
  'order_id': '1',
  'date_created': '1/1/1 10:10:10',
  'status': 'pending',
}

OrderProduct = {
  'order_id': '1',
  'product_id': '1',
  'quantity': '100',
}


Page = {
  """ Static pages """
  'id': '1',
  'title': 'Contact',
  'slug': 'contact-us',
  'body': 'bodyyy',
}

SitePage = {
  'site_id': '1',
  'page_id': '1',
}

ProductAttribute = {
  'attribute_id': '1',
  'product_type': 'book',
  'title': 'isbn',
  'description': 'Books isbn',
  'field_type': 'string',
}

ProductAttributeValue = {
  'product_id': '1',
  'attribute_id': '1',
  'value': '123'
}

ProductPrice = {
  'price_id': '1',
  'product_id': '1',
  'price': '100',
}

ProductImage = {
  'image_id': '1',
  'media_url': 'media/12/41'
               'product_id': '1',
                             'date_added': '1/1/1',
}

Order = {
  'order_id': '1',
  'site_id': '1',
  'user_id': '1',
  'order_method': 'Online, In-store',
  'discount_code': '',
  'notes': '11111',
  'shipping_method': '1',
  'shipping_address': '1',
}

OrderProduct = {
  'order_id': '1',
  'product_id': '1',
  'quantity': '100',
  'unit_price': '10',
  'unit_tax': '10',
  'line_item_price': '10',
  'line_item_tax': '100',
  'line_item_discount': '10', # generated automatically ,vice versa if set first instead of setting line item pricefirst.
}

""" order can have many order statuses """
OrderStatus = {
  'status_id': 'new, blocked, in-process, billed, shipped, completed, cancelled',
  'notes': 'notes saved',
  'timestamp': '1/1/1 1:1:1',
}

""" order can have multiple payments """
OrderPaymentAuthorization = {
  'amount': '100',
  'payment_method': 'VISA',
  'timestamp' : '1:1:1',
  'transaction_id': '1',
  'details': '1',
  'status': 'success, failed, pending'
}

ShippingMethod = {
  'shipping_method_id': '1',
  'name': 'free',
  'description': 'LBC pwd sad',
  'site_id': '1',
}

Address = {
  'street': '',
  'city': '',
  'state': '',
  'zip_code': '',
  'country': '',
  'user_id': '',
  'type': 'shipping | billing'
}

Cart = {
  'site_id': '1',
  'description': '1',
  'date_created': '1/1/1',
  'customer_id': '1',
  'is_active': 'true',
  'expire_on': '1/1/1',
}

CartItem = {
  'product_id': '1',
  'cart_id': '1',
  'quantity': '1',
}

Wishlist = {
  'title': 'Dream',
  'description': 'yeah',
  'site_id': '1',
  'customer_id': '1',
  'date_created': '1/1/1'
}

WishlistItem = {
  'product_id': '1',
  'wishlist_id': '1',
  'date_added': '1',
}

