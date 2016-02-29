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
   date_created text,
   customer_id int8,
   is_active boolean
);