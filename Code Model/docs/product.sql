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
CREATE TABLE items (
  item_id           SERIAL PRIMARY KEY,
  serial_no         TEXT,
  site_id           INT, -- user / business who owns the item
  barcode           TEXT,

  name              TEXT,
  description       TEXT,

  date_added        TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now(),
  date_updated      TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now(),

  taxable           BOOLEAN,
  tax_class         INT,

  unit_cost         INT,
  stock_on_hand     INT, -- generated
    re_order_level    INT,
  re_order_quantity INT,
  is_active         BOOLEAN                              DEFAULT TRUE
);

CREATE TABLE tax_classes (
  -- ex: VAT
  tax_class_id SERIAL PRIMARY KEY,
  title        TEXT,
  description  TEXT
);

CREATE TABLE locations (
  location_id SERIAL PRIMARY KEY,
  location    TEXT NOT NULL
);

CREATE TABLE areas (
  area_id SERIAL PRIMARY KEY,
  area    TEXT NOT NULL
);

CREATE TABLE location_items (
  location_item_id SERIAL PRIMARY KEY,
  item_id          INT REFERENCES items (item_id) ON UPDATE CASCADE ON DELETE CASCADE,
  location_id      INT REFERENCES locations (location_id) ON UPDATE CASCADE,
  area             INT REFERENCES areas (area_id) ON UPDATE CASCADE,
  notes            TEXT,

  CONSTRAINT item_location_id PRIMARY KEY (item_id, location_id)
);

CREATE TABLE vendors (
  vendor_id SERIAL PRIMARY KEY,
  name text,
  address text
);

CREATE TABLE transfers (
  transfer_id SERIAL PRIMARY KEY
);

CREATE TABLE transfer_items (
  transfer_item_id SERIAL PRIMARY KEY
);

-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION items_upsert(IN par_item_id           INT, IN par_serial_no TEXT, IN par_user_id INT,
                                        IN par_category          TEXT,
                                        IN par_type              TEXT,
                                        IN par_model             TEXT, IN par_brand TEXT, IN par_description TEXT,
                                        IN par_units             TEXT,
                                        IN par_date_added        TIMESTAMP, IN par_date_updated TIMESTAMP,
                                        IN par_stock_on_hand     INT, IN par_re_order_level INT,
                                        IN par_re_order_quantity INT, IN par_is_active BOOLEAN)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN

  IF par_item_id ISNULL
  THEN
    INSERT INTO items (title, description, supplier_id, category_id, site_id, product_type_id, on_hand, re_order_level)
    VALUES (par_title, par_description, par_supplier_id, par_category_id, par_site_id, par_product_type_id, par_on_hand,
            par_re_order_level);
    loc_response = 'ok';
  ELSE
    UPDATE products
    SET title     = par_title, description = par_description, supplier_id = par_supplier_id,
      category_id = par_category_id, site_id = par_site_id, product_type_id = par_product_type_id,
      on_hand     = par_on_hand, re_order_level = par_re_order_level
    WHERE product_id = par_product_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
--------------------------------------------------------------------------------------------------------
-- SELECT products_upsert(NULL, 'test', 'description', 1, 1, 1, 1, 100, 10);
--------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION products_get(IN par_product_id INT)
  RETURNS SETOF products AS $$
BEGIN
  IF par_product_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM products;
  ELSE
    RETURN QUERY SELECT *
                 FROM products
                 WHERE product_id = par_product_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from products_get();
-----------------------------------------------------------------





CREATE TABLE product_types (
  product_type_id SERIAL PRIMARY KEY,
  name            TEXT,
  description     TEXT
);
-----------------------------------------------------------------
-- insert into product_types(name,description) values ('1','1Description')
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION product_types_upsert(IN par_product_type_id INT, IN par_name TEXT, IN par_description TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_product_type_id ISNULL
  THEN
    INSERT INTO product_types (name, description) VALUES (par_name, par_description);
    loc_response = 'ok';
  ELSE
    UPDATE product_types
    SET name = par_name, description = par_description
    WHERE product_type_id = par_product_type_id;
    loc_response = 'ok';
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT product_types_upsert(NULL, 'test', 'test description 2');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION product_types_get(IN par_product_type_id INT)
  RETURNS SETOF product_types AS $$
BEGIN
  IF par_product_type_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM product_types;
  ELSE
    RETURN QUERY SELECT *
                 FROM product_types
                 WHERE product_type_id = par_product_type_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from get_product_types();
-----------------------------------------------------------------




CREATE TABLE categories (
  category_id SERIAL PRIMARY KEY,
  name        TEXT,
  description TEXT,
  image       TEXT
);
-----------------------------------------------------------------
-- insert into categories(name,description,image) values ('1','1Description','image url soon')
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION categories_upsert(IN par_category_id INT, IN par_name TEXT, IN par_description TEXT,
                                             IN par_image       TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_category_id ISNULL
  THEN
    INSERT INTO categories (name, description, image) VALUES (par_name, par_description, par_image);
    loc_response = 'ok';
  ELSE
    UPDATE categories
    SET name = par_name, description = par_description, image = par_image
    WHERE category_id = par_category_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
SELECT categories_upsert(NULL, 'test', 'test description 2', 'url');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION categories_get(IN par_category_id INT)
  RETURNS SETOF categories AS $$
BEGIN
  IF par_category_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM categories;
  ELSE
    RETURN QUERY SELECT *
                 FROM categories
                 WHERE category_id = par_category_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from get_categories();
-----------------------------------------------------------------



CREATE TABLE product_attributes (
  product_attribute_id SERIAL PRIMARY KEY,
  product_type_id      INT,
  name                 TEXT,
  code                 TEXT,
  type                 TEXT,
  is_active            BOOLEAN
);
-----------------------------------------------------------------
-- insert into product_attributes(name, code, type, is_active) values ('ISBN','ISBN','string', 'true')
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION product_attributes_upsert(IN par_product_type_id INT, IN par_product_attribute_id INT,
                                                     IN par_name            TEXT, IN par_code TEXT, IN par_type TEXT,
                                                     IN par_is_active       BOOLEAN)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_product_attribute_id ISNULL
  THEN
    INSERT INTO product_attributes (product_type_id, name, code, type, is_active)
    VALUES (par_product_type_id, par_name, par_code, par_type, par_is_active);
    loc_response = 'ok';
  ELSE
    UPDATE product_attributes
    SET name = par_name, code = par_code, type = par_type, is_active = par_is_active
    WHERE product_attribute_id = par_product_attribute_id AND product_type_id = par_product_type_id;
    loc_response = 'ok';
  END IF;
  RETURN loc_response;

END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
SELECT product_attributes_upsert(NULL, 1, 'test', 'test code', 'test type', TRUE);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION product_attributes_get(IN par_product_type_id INT, IN par_product_attribute_id INT)
  RETURNS SETOF product_attributes AS $$
BEGIN
  IF par_product_attribute_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM product_attributes
                 WHERE product_type_id = par_product_type_id;
  ELSE
    RETURN QUERY SELECT *
                 FROM product_attributes
                 WHERE product_type_id = par_product_type_id AND product_attribute_id = par_product_attribute_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from product_attributes_get(1,1);
-----------------------------------------------------------------




CREATE TABLE product_categories (
  product_category_id SERIAL PRIMARY KEY,
  product_id          INT,
  category_id         TEXT
);
-----------------------------------------------------------------
-- insert into product_attributes(name, code, type, is_active) values ('ISBN','ISBN','string', 'true')
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION product_categories_upsert(IN par_product_category_id INT, IN par_product_id INT,
                                                     IN par_category_id         INT)
  RETURNS TEXT AS $$
DECLARE
  loc_response         TEXT;
  loc_product_id       TEXT;
  loc_category_id      TEXT;
  loc_product_category TEXT;
BEGIN

  -- If no product_category_id was passed, then create a new row else update the row
  IF par_product_category_id ISNULL
  THEN
    INSERT INTO product_categories (product_id, category_id) VALUES (par_product_id, par_category_id);
    loc_response = 'ok';
  ELSE
    UPDATE product_categories
    SET category_id = par_category_id
    WHERE product_category_id = par_product_category_id AND product_id = par_product_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
SELECT product_categories_upsert(NULL, 1, 1);
SELECT product_categories_upsert(NULL, 1, 2);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION product_categories_get(IN par_product_id INT, IN par_product_category_id INT)
  RETURNS SETOF product_categories AS $$
-- If no product_category_id is passed, then return all rows of categories for the product, else, only return the single product-category pair
-- Source: http://www.postgresql.org/docs/9.1/static/plpgsql-control-structures.html
BEGIN
  IF par_product_category_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM product_categories
                 WHERE product_id = par_product_id;
  ELSE
    RETURN QUERY SELECT *
                 FROM product_categories
                 WHERE product_id = par_product_id AND product_category_id = par_product_category_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from product_categories_get(1, null);
-----------------------------------------------------------------




CREATE TABLE product_attribute_values (
  product_attribute_value_id SERIAL PRIMARY KEY,
  product_id                 INT,
  product_attribute_id       INT,
  value                      TEXT
);
-----------------------------------------------------------------
-- insert into product_attributes(name, code, type, is_active) values ('ISBN','ISBN','string', 'true')
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION product_attribute_values_upsert(IN par_product_attribute_value_id INT, IN par_product_id INT,
                                                           IN par_product_attribute_id       INT, IN par_value TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response         TEXT;
  loc_product_id       TEXT;
  loc_category_id      TEXT;
  loc_product_category TEXT;
BEGIN

  -- If no product_category_id was passed, then create a new row else update the row
  IF par_product_attribute_value_id ISNULL
  THEN
    INSERT INTO product_attribute_values (product_id, product_attribute_id, value)
    VALUES (par_product_id, par_product_attribute_id, par_value);
    loc_response = 'ok';
  ELSE
    UPDATE product_categories
    SET product_attribute_id = par_product_attribute_id, value = par_value
    WHERE product_attribute_value_id = par_product_attribute_value_id AND product_id = par_product_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
SELECT product_attribute_values_upsert(NULL, 1, 1, 'hi');
SELECT product_attribute_values_upsert(NULL, 1, 2, 'ho');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION product_attribute_values_get(IN par_product_id INT, IN par_product_attribute_value_id INT)
  RETURNS SETOF product_attribute_values AS $$
BEGIN
  IF par_product_attribute_value_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM product_attribute_values
                 WHERE product_id = par_product_id;
  ELSE
    RETURN QUERY SELECT *
                 FROM product_attribute_values
                 WHERE product_id = par_product_id AND product_attribute_value_id = par_product_attribute_value_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from product_attribute_values_get(1, null);
-----------------------------------------------------------------









CREATE TABLE product_images (
  product_image_id SERIAL PRIMARY KEY,
  product_id       INT,
  image_url        TEXT,
  caption          TEXT,
  display_order    INT
);
-----------------------------------------------------------------
-- **
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION product_images_upsert(
  IN par_product_image_id INT,
  IN par_product_id       INT,
  IN par_image_url        TEXT,
  IN par_caption          TEXT,
  IN par_display_order    INT)
  RETURNS TEXT AS $$

DECLARE
  loc_response         TEXT;
  loc_product_id       TEXT;
  loc_category_id      TEXT;
  loc_product_category TEXT;
BEGIN

  -- If no product_image_id was passed, then create a new row else update the row
  IF par_product_image_id ISNULL
  THEN
    INSERT INTO product_images (product_id, image_url, caption, display_order)
    VALUES (par_product_id, par_image_url, par_caption, par_display_order);
    loc_response = 'ok';
  ELSE
    UPDATE product_images
    SET image_url = par_image_url, caption = par_caption, display_order = par_display_order
    WHERE product_image_id = par_product_image_id AND product_id = par_product_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
SELECT product_images_upsert(NULL, 1, 'url', 'hi', 0);
SELECT product_images_upsert(NULL, 1, 'url2', 'ho', 0);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION product_images_get(IN par_product_id INT, IN par_product_image_id INT)
  RETURNS SETOF product_images AS $$
BEGIN
  IF par_product_image_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM product_images
                 WHERE product_id = par_product_id;
  ELSE
    RETURN QUERY SELECT *
                 FROM product_images
                 WHERE product_id = par_product_id AND product_image_id = par_product_image_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from product_images_get(1, null);
-----------------------------------------------------------------
