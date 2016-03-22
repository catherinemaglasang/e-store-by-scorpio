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
select add_product_type('test', 'test description 2');
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




create table categories (
   category_id serial primary key,
   name text,
   description text,
   image text
);
-----------------------------------------------------------------
-- insert into categories(name,description,image) values ('1','1Description','image url soon')
-----------------------------------------------------------------
create or replace function add_category(in par_name text, in par_description text, in par_image text) returns text as $$
  DECLARE
    loc_response text;
  BEGIN
    insert into categories(name, description, image) values (par_name, par_description, par_image);
    loc_response = 'ok';
    return loc_response;
  END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
select add_category('test', 'test description 2', 'url');
-----------------------------------------------------------------
create or replace function get_categories(out int, out text, out text, out text) returns setof record as $$
    select * from categories;
  $$ LANGUAGE 'sql';
-----------------------------------------------------------------
-- select * from get_categories();
-----------------------------------------------------------------
create or replace function get_category(in par_category_id int, out int, out text, out text, out text) returns setof record as $$
    select * from categories where category_id = par_category_id;
  $$ LANGUAGE 'sql';
-----------------------------------------------------------------
-- select * from get_category(1);
-----------------------------------------------------------------
create or replace function update_category(in par_category_id int, in par_name text, in par_description text, in par_image text) returns text as $$
DECLARE
  loc_response text;
BEGIN
  update categories set name = par_name, description = par_description, image = par_image where category_id = par_category_id;
  loc_response = 'ok';
  return loc_response;
END;
  $$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select update_category(1, 'new name', 'new desc', 'new image');
-----------------------------------------------------------------



create table product_attributes (
   product_attribute_id serial primary key,
   product_type_id int,
   name text,
   code text,
   type text,
   is_active BOOLEAN
);
-----------------------------------------------------------------
-- insert into product_attributes(name, code, type, is_active) values ('ISBN','ISBN','string', 'true')
-----------------------------------------------------------------
create or replace function product_attributes_create(in par_product_type_id int, in par_name text, in par_code text, in par_type text, in par_is_active boolean) returns text as $$
  DECLARE
    loc_response text;
  BEGIN
    insert into product_attributes(product_type_id, name, code, type, is_active) values (par_product_type_id, par_name, par_code, par_type, par_is_active);
    loc_response = 'ok';
    return loc_response;
  END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
select product_attributes_create(1, 'test', 'test code', 'test type', true);
-----------------------------------------------------------------
create or replace function product_attributes_get_all(in par_product_type_id int, out int, out int, out text, out text, out text, out boolean) returns setof record as $$
    select * from product_attributes
    where product_type_id= par_product_type_id;
  $$ LANGUAGE 'sql';
-----------------------------------------------------------------
-- select * from product_attributes_get_all(1);
-----------------------------------------------------------------
create or replace function product_attributes_get(in par_product_type_id int, in par_product_attribute_id int, out int, out int, out text, out text, out text, out boolean) returns setof record as $$
    select * from product_attributes
    where product_attribute_id = par_product_attribute_id and product_type_id = par_product_type_id;
  $$ LANGUAGE 'sql';
-----------------------------------------------------------------
-- select * from product_attributes_get(1,1);
-----------------------------------------------------------------
--  Note that the product type id can't be updated when we want to update a product attribute
create or replace function product_attributes_update(in par_product_attribute_id int, in par_product_type_id int, in par_name text, in par_code text, in par_type text, in par_is_active boolean) returns text as $$
DECLARE
  loc_response text;
BEGIN
  update product_attributes set name = par_name, code = par_code, type = par_type, is_active = par_is_active
  where product_attribute_id = par_product_attribute_id and product_type_id = par_product_type_id;
  loc_response = 'ok';
  return loc_response;
END;
  $$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select product_attributes_update(1, 'new name', 'new desc', 'new type', true);
-----------------------------------------------------------------






create table product_categories (
   product_category_id serial primary key,
   product_id int,
   category_id text
);
-----------------------------------------------------------------
-- insert into product_attributes(name, code, type, is_active) values ('ISBN','ISBN','string', 'true')
-----------------------------------------------------------------
create or replace function product_categories_upsert(in par_product_category_id int, in par_product_id int, in par_category_id int) returns text as $$
  DECLARE
    loc_response text;
    loc_product_id text;
    loc_category_id text;
    loc_product_category text;
  BEGIN

    -- If no product_category_id was passed, then create a new row else update the row
    if par_product_category_id isnull then
      insert into product_categories(product_id, category_id) values (par_product_id, par_category_id);
      loc_response = 'ok';
    else
      update product_categories set category_id = par_category_id
      where product_category_id = par_product_category_id and product_id = par_product_id;
      loc_response = 'ok';
    end if;

    return loc_response;
  END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
select product_categories_upsert(null, 1, 1);
select product_categories_upsert(null, 1, 2);
-----------------------------------------------------------------
create or replace function product_categories_get(in par_product_id int, in par_product_category_id int) returns setof product_categories as $$
  -- If no product_category_id is passed, then return all rows of categories for the product, else, only return the single product-category pair
  -- Source: http://www.postgresql.org/docs/9.1/static/plpgsql-control-structures.html
  BEGIN
    if par_product_category_id isnull then
      return query select * from product_categories where product_id = par_product_id;
    else
      return query select * from product_categories where product_id = par_product_id and product_category_id = par_product_category_id;
    end if;
  END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
select * from product_categories_get(1, null);
-----------------------------------------------------------------




create table product_attribute_values (
   product_attribute_value_id serial primary key,
   product_id int,
   product_attribute_id int,
   value text
);
-----------------------------------------------------------------
-- insert into product_attributes(name, code, type, is_active) values ('ISBN','ISBN','string', 'true')
-----------------------------------------------------------------
create or replace function product_attribute_values_upsert(in par_product_attribute_value_id int, in par_product_id int, in par_product_attribute_id int, in par_value text) returns text as $$
  DECLARE
    loc_response text;
    loc_product_id text;
    loc_category_id text;
    loc_product_category text;
  BEGIN

    -- If no product_category_id was passed, then create a new row else update the row
    if par_product_attribute_value_id isnull then
      insert into product_attribute_values(product_id, product_attribute_id, value) values (par_product_id, par_product_attribute_id, par_value);
      loc_response = 'ok';
    else
      update product_categories set product_attribute_id = par_product_attribute_id, value = par_value
      where product_attribute_value_id = par_product_attribute_value_id and product_id = par_product_id;
      loc_response = 'ok';
    end if;

    return loc_response;
  END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
select product_attribute_values_upsert(null, 1, 1, 'hi');
select product_attribute_values_upsert(null, 1, 2, 'ho');
-----------------------------------------------------------------
create or replace function product_attribute_values_get(in par_product_id int, in par_product_attribute_value_id int) returns setof product_attribute_values as $$
  BEGIN
    if par_product_attribute_value_id isnull then
      return query select * from product_attribute_values where product_id = par_product_id;
    else
      return query select * from product_attribute_values where product_id = par_product_id and product_attribute_value_id = par_product_attribute_value_id;
    end if;
  END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
select * from product_attribute_values_get(1, null);
-----------------------------------------------------------------









create table product_images (
  product_image_id serial primary key,
  product_id int,
  image_url text,
  caption text,
  display_order int
);
-----------------------------------------------------------------
-- **
-----------------------------------------------------------------
create or replace function product_images_upsert(
  in par_product_image_id int,
  in par_product_id int,
  in par_image_url text,
  in par_caption text,
  in par_display_order int) returns text as $$

  DECLARE
    loc_response text;
    loc_product_id text;
    loc_category_id text;
    loc_product_category text;
  BEGIN

    -- If no product_image_id was passed, then create a new row else update the row
    if par_product_image_id isnull then
      insert into product_images(product_id, image_url, caption, display_order) values (par_product_id, par_image_url, par_caption, par_display_order);
      loc_response = 'ok';
    else
      update product_images set image_url = par_image_url, caption = par_caption, display_order = par_display_order
      where product_image_id = par_product_image_id and product_id = par_product_id;
      loc_response = 'ok';
    end if;

    return loc_response;
  END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
select product_images_upsert(null, 1, 'url', 'hi', 0);
select product_images_upsert(null, 1, 'url2', 'ho', 0);
-----------------------------------------------------------------
create or replace function product_images_get(in par_product_id int, in par_product_image_id int) returns setof product_images as $$
  BEGIN
    if par_product_image_id isnull then
      return query select * from product_images where product_id = par_product_id;
    else
      return query select * from product_images where product_id = par_product_id and product_image_id = par_product_image_id;
    end if;
  END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
select * from product_images_get(1, null);
-----------------------------------------------------------------








