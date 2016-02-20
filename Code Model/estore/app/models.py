from sqlalchemy import create_engine
import os

class DBconn:
    def __init__(self):
        engine = create_engine("postgresql://bookshop:bookshop@127.0.0.1:5432/bookshopdb", echo=False)
        self.conn = engine.connect()
        self.trans = self.conn.begin()

    def getcursor(self):
        cursor = self.conn.connection.cursor()
        return cursor

    def dbcommit(self):
        self.trans.commit()

















 # engine = create_engine("postgresql://magic2:asdasd@127.0.0.1:5432/estore", echo=False)


# from app import db
# from datetime import datetime
# from flask import url_for
#
# class User(db.Model):
#     """An admin user capable of viewing reports.
#
#     :param str email: email address of user
#     :param str password: encrypted password for the user
#
#     """
#     id = db.Column(db.Integer)
#     email = db.Column(db.String, primary_key=True)
#     password = db.Column(db.String)
#     is_admin = db.Column(db.Boolean, default=False)
#
#     def __repr__(self):
#         return '%s' % (self.email)
#
# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     sku = db.Column(db.String)
#     supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
#     title = db.Column(db.Integer)
#     description = db.Column(db.String)
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     unit_price = db.Column(db.Float)
#     on_hand = db.Column(db.Integer)
#     re_order_level = db.Column(db.Integer)
#     is_active = db.Column(db.Boolean, default=True)
#
# class Supplier(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     address = db.Column(db.String)
#     phone = db.Column(db.String)
#     fax = db.Column(db.String)
#     email = db.Column(db.String)
#     is_active = db.Column(db.Boolean, default=True)
#
# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     description = db.Column(db.Text)
#     main_image = db.Column(db.LargeBinary)
#     is_active = db.Column(db.Boolean, default=True)
#
# class Cart(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     session_id = db.Column(db.Integer)
#     date_created = db.Column(db.Integer)
#     is_active = db.Column(db.Boolean, default=True)
#
# class CartDetails(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
#     quantity = db.Column(db.Integer)
#     timestamp = db.Column(db.DateTime)
#
# class WishlistDetails(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlist.id'))
#     product_id = db.Column(db.Integer)
#     timestamp = db.Column(db.DateTime)
#
# class Wishlist(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#
# class Customer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String)
#     last_name = db.Column(db.String)
#     address = db.Column(db.String)
#     city = db.Column(db.String)
#     state = db.Column(db.String)
#     postal_code = db.Column(db.String)
#     country = db.Column(db.String)
#     phone = db.Column(db.String)
#     email = db.Column(db.String)
#     user_id = db.Column(db.Integer)
#     billing_address = db.Column(db.String)
#     shipping_address = db.Column(db.String)
#     date_created = db.Column(db.DateTime)
#
# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
#     payment_id = db.Column(db.Integer)
#     transaction_date = db.Column(db.DateTime)
#     shipping_date = db.Column(db.DateTime)
#     timestamp = db.Column(db.DateTime)
#     transaction_status = db.Column(db.String)
#     total = db.Column(db.Float)
#
# class OrderDetails(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
#     product_id = db.Column(db.Integer)
#     unit_price = db.Column(db.Float)
#     discount = db.Column(db.Float)
#     quantity = db.Column(db.Integer)
