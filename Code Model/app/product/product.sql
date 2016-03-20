---------------------------------------------------------------------------
--
-- Execute this script before before running the app
-- Stored procedures for inventory
-- Database: Postgresql
--
-- Author: Roselle Ebarle
-- http://roselleebarle.com
--
-----------------------------------------------------------------
create table products (
   product_id serial primary key,
   title text,
   description text,
   date_added timestamp without time zone NOT NULL DEFAULT now(),
   ordering int DEFAULT 0,
   supplier_id int,
   category_id int,
   site_id int,
   product_type_id int,
   on_hand int,
   re_order_level int,
   is_active boolean DEFAULT TRUE
);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION add_product(in par_title text, in par_description text, in par_supplier_id int, in par_category_id int, in par_site_id int, in par_product_type_id int, in par_on_hand int, in par_re_order_level int) returns text as $$
  DECLARE
    loc_response text;
  BEGIN
    -- Note: Attributes with a default value shouldn't be included below nor in the input parameters.
    insert into products(title, description, supplier_id, category_id, site_id, product_type_id, on_hand, re_order_level) values (par_title, par_description,par_supplier_id, par_category_id, par_site_id, par_product_type_id, par_on_hand, par_re_order_level);
    loc_response = 'ok';
    return loc_response;
  END;
$$ LANGUAGE 'plpgsql';
--------------------------------------------------------------------------------------------------------
select add_product('test','description',1,1,1,1,100,10);
--------------------------------------------------------------------------------------------------------
create or replace function get_products(out product_id int, out title text, out description text, out date_added timestamp, out ordering int, out supplier_id int, out category_id int, out site_id int, out product_type_id int, out on_hand int, out re_order_level int, out is_active boolean) returns setof record as $$
    select * from products;
$$ language 'sql';
-----------------------------------------------------------------
select * from get_products();
-----------------------------------------------------------------
create or replace function get_product(par_product_id int, out product_id int, out title text, out description text, out date_added timestamp, out ordering int, out supplier_id int, out category_id int, out site_id int, out product_type_id int, out on_hand int, out re_order_level int, out is_active boolean) returns SETOF RECORD as $$
    select * from products where product_id=par_product_id;
$$ language 'sql';
-----------------------------------------------------------------
-- select * from get_product(1);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION update_product(in par_product_id int, in par_title text, in par_description text, in par_supplier_id int, in par_category_id int, in par_site_id int, in par_product_type_id int, in par_on_hand int, in par_re_order_level int) returns text as $$
  DECLARE
    loc_response text;
  BEGIN
    update products set title=par_title, description=par_description, supplier_id=par_supplier_id, category_id=par_category_id, site_id=par_site_id, product_type_id=par_product_type_id, on_hand=par_on_hand, re_order_level=par_re_order_level where product_id=par_product_id;
    loc_response = 'ok';
    RETURN loc_response;
  END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
select update_product(1, 'test new','description new',1,1,1,1,100,10);
-----------------------------------------------------------------
create table product_types (
   product_type_id serial primary key,
   name text,
   description text
);
-----------------------------------------------------------------
-- insert into product_types(name,description) values ('1','1Description')
-----------------------------------------------------------------
create or replace function add_product_type(in par_name text, in par_description text) returns text as $$
  DECLARE
    loc_response text;
  BEGIN
    insert into product_types(name, description) values (par_name, par_description);
    loc_response = 'ok';
    return loc_response;
  END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select add_product_type('test', 'test description 2');
-----------------------------------------------------------------
create or replace function get_product_types(out int, out text, out text) returns setof record as $$
    select * from product_types;
  $$ LANGUAGE 'sql';
-----------------------------------------------------------------
-- select * from get_product_types();
-----------------------------------------------------------------
create or replace function get_product_type(in par_product_type_id int, out int, out text, out text) returns setof record as $$
    select * from product_types where product_type_id = par_product_type_id;
  $$ LANGUAGE 'sql';
-----------------------------------------------------------------
-- select * from get_product_type(1);
-----------------------------------------------------------------
create or replace function update_product_type(in par_product_type_id int, in par_name text, in par_description text) returns text as $$
DECLARE
  loc_response text;
BEGIN
  update product_types set name = par_name, description = par_description where product_type_id = par_product_type_id;
  loc_response = 'ok';
  return loc_response;
END;
  $$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select update_product_type(1, 'new name', 'new desc');
-----------------------------------------------------------------
