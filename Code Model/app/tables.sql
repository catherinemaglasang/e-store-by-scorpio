create table products (
   id int8 primary key,
   sku text,
   supplier_id int8,
   title text,
   description text,
   category_id int8,
   unit_price float8,
   on_hand int8,
   re_order_level int8,
   is_active boolean
);

create table users (
   id int8 primary key,
   username text,
   password text,
   is_admin boolean
);

create table suppliers (
   id int8 primary key,
   name text,
   address text,
   phone text,
   fax text,
   email text,
   is_active boolean
);

create table carts (
   id int8 primary key,
   session_id int8,
   date_created DATE,
   customer_id int8,
   is_active boolean
);
Given I am at the add product form page
When I add new product with the following details:
| id | sku | supplier_id | title | description  | category_id | unit_price| on_hand | re_order_level | is_active |
| 1  | 100  | 1                  | title1| description1| 1                 | 100             | 20        | 10                          | True       |
Then I should get a '200' response
And the new product should appear on the product table
create table categories (
   id int8 primary key,
   name text,
   description text,
   main_image bytea,
   parent_category_id int8,
   is_active boolean
);

create table cart_details (
   id int8 primary key,
   cart_id int8,
   product_id int8,
   quantity int8,
   time_stamp timestamp
);

create table wishlist_details (
   id int8 primary key,
   wishlist_id int8,
   product_id int8,
   time_stamp timestamp
);

create table wishlist (
   id int8 primary key
);

create table orders(
   id int8 primary key,
   customer_id int8,
   payment_id int8,
   transaction_date date,
   shipping_date date,
   time_stamp timestamp,
   transaction_status text,
   total float8
)

create table order_details(
  id int8 primary key,
  order_id int8,
  product_id int8,
  unit_price float8,
  discount float8,
  quantity int8
)