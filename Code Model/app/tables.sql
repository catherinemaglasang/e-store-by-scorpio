-- Source: http://codehandbook.org/creating-restful-api-using-python-flask-mysql/
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
   date_created text,
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