-- Source: http://codehandbook.org/creating-restful-api-using-python-flask-mysql/
create table users (
   id int8 primary key,
   username text,
   password text,
   email text unique,
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
create table order_items(
  id int8 primary key,
  order_id int8,
  product_id int8,
  unit_price float8,
  discount float8,
  quantity int8
)

create table customer(
  id int8 primary key,
  first_name text,
  last_name text,
  address text,
  city text,
  state text,
  postal_code text,
  country text,
  phone text,
  email text unique,
  user_id int8,
  billing_address text,
  shipping_address text,
  date_created timestamp
)