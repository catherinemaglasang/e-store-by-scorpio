CREATE OR REPLACE FUNCTION areas_upsert(IN par_area_id INT, IN par_area_description TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN

  IF par_area_id ISNULL
  THEN
    INSERT INTO areas (area_description)
    VALUES (par_area_description);
    loc_response = 'ok';
  ELSE
    UPDATE areas
    SET area_description = par_area_description
    WHERE area_id = par_area_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
--------------------------------------------------------------------------------------------------------
-- select areas_upsert(null, 'shelf 1');
--------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION areas_get(IN par_area_id INT)
  RETURNS SETOF areas AS $$
BEGIN
  IF par_area_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM areas;
  ELSE
    RETURN QUERY SELECT *
                 FROM areas
                 WHERE area_id = par_area_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
--------------------------------------------------------------------------------------------------------
-- select areas_get(null);
--------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION attributes_upsert(IN par_attribute_id   INT, IN par_type_id INT,
                                             IN par_attribute_name TEXT, IN par_validation TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN

  IF par_attribute_id ISNULL
  THEN
    INSERT INTO attributes (type_id, attribute_name, validation)
    VALUES (par_type_id, par_attribute_name, par_validation);
    loc_response = 'ok';
  ELSE
    UPDATE attributes
    SET attribute_name = par_attribute_name, validation = par_validation
    WHERE attribute_id = par_attribute_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
--------------------------------------------------------------------------------------------------------
-- SELECT attributes_upsert(NULL, 1, 'isbnyeah', 'textyeah');
--------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION attributes_get(IN par_attribute_id INT, IN par_type_id INT)
  RETURNS SETOF attributes AS $$
BEGIN
  IF par_attribute_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM attributes
                 WHERE type_id = par_type_id;
  ELSE
    RETURN QUERY SELECT *
                 FROM attributes
                 WHERE attribute_id = par_attribute_id AND type_id = par_type_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
--------------------------------------------------------------------------------------------------------
SELECT attributes_get(NULL, 1);
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION customers_upsert(IN par_customer_id      INT, IN par_name TEXT, IN par_billing_address TEXT,
                                            IN par_shipping_address TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN

  IF par_customer_id ISNULL
  THEN
    INSERT INTO customers (name, billing_address, shipping_address)
    VALUES (par_name, par_billing_address, par_shipping_address);
    loc_response = 'ok';
  ELSE
    UPDATE customers
    SET name = par_name, billing_address = par_billing_address, shipping_address = par_shipping_address
    WHERE customer_id = par_customer_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
--------------------------------------------------------------------------------------------------------
-- SELECT customers_upsert(null,'name','billing_address', 'shipping_address');
--------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION customers_get(IN par_customer_id INT)
  RETURNS SETOF customers AS $$
BEGIN
  IF par_customer_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM customers;
  ELSE
    RETURN QUERY SELECT *
                 FROM customers
                 WHERE customer_id = par_customer_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
--------------------------------------------------------------------------------------------------------
-- select customers_get(null);
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION images_upsert(IN par_image_id INT, IN par_item_id INT, IN par_image_url TEXT,
                                         IN par_caption  TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN

  IF par_image_id ISNULL
  THEN
    INSERT INTO images (item_id, image_url, caption)
    VALUES (par_item_id, par_image_url, par_caption);
    loc_response = 'ok';
  ELSE
    UPDATE images
    SET item_id = par_item_id, image_url = par_image_url, caption = par_caption;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
--------------------------------------------------------------------------------------------------------
-- SELECT images_upsert(null,null, 'http://google.com/', 'google');
--------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION images_get(IN par_image_id INT)
  RETURNS SETOF images AS $$
BEGIN
  IF par_image_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM images;
  ELSE
    RETURN QUERY SELECT *
                 FROM images
                 WHERE image_id = par_image_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-------------------------------------------------------------------------------
-- select images_get(null);
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION item_attributes_upsert(IN par_item_attribute_id INT, IN par_attribute_id INT,
                                                  IN par_item_id           INT, IN par_attribute_value TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN

  IF par_item_attribute_id ISNULL
  THEN
    INSERT INTO item_attributes (attribute_id, item_id, attribute_value)
    VALUES (par_attribute_id, par_item_id, par_attribute_value);
    loc_response = 'ok';
  ELSE
    UPDATE item_attributes
    SET attribute_id = par_attribute_id, item_id = par_item_id, attribute_value = par_attribute_value
    WHERE item_attribute_id = par_item_attribute_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-------------------------------------------------------------------------------
-- select images_get(null);
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION item_attributes_get(IN par_item_attribute_id INT)
  RETURNS SETOF item_attributes AS $$
BEGIN
  IF par_item_attribute_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM item_attributes;
  ELSE
    RETURN QUERY SELECT *
                 FROM item_attributes
                 WHERE item_attribute_id = par_item_attribute_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-------------------------------------------------------------------------------
-- select images_get(null);
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION item_variation_options_upsert(IN par_item_variation_option_id INT, IN par_option_id INT,
                                                         IN par_item_variation_id        INT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN

  IF par_item_variation_option_id ISNULL
  THEN
    INSERT INTO item_variation_options (option_id, item_variation_id) VALUES (par_option_id, par_item_variation_id);
    loc_response = 'ok';
  ELSE
    UPDATE item_variation_options
    SET option_id = par_option_id, item_variation_id = par_item_variation_id
    WHERE item_variation_option_id = par_item_variation_option_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-------------------------------------------------------------------------------
-- select images_get(null);
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION item_variation_options_get(IN par_item_variation_option_id INT)
  RETURNS SETOF item_variation_options AS $$
BEGIN
  IF par_item_variation_option_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM item_variation_options;
  ELSE
    RETURN QUERY SELECT *
                 FROM item_variation_options
                 WHERE item_variation_option_id = par_item_variation_option_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-------------------------------------------------------------------------------
-- select images_get(null);
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION item_variations_upsert(IN par_item_variation_id INT, IN par_item_id INT,
                                                  IN par_stock_on_hand     NUMERIC, IN par_unit_cost NUMERIC,
                                                  IN par_re_order_level    NUMERIC, IN par_re_order_quantity NUMERIC,
                                                  IN par_is_active         BOOLEAN)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN

  IF par_item_variation_id ISNULL
  THEN
    INSERT INTO item_variations (item_id, stock_on_hand, unit_cost, re_order_level, re_order_quantity, is_active)
    VALUES (par_item_id, par_stock_on_hand, par_unit_cost, par_re_order_level, par_re_order_quantity, par_is_active);
    loc_response = 'ok';
  ELSE
    UPDATE item_variations
    SET item_id      = par_item_id, stock_on_hand = par_stock_on_hand, unit_cost = par_unit_cost,
      re_order_level = par_re_order_level, re_order_quantity = par_re_order_quantity, is_active = par_is_active
    WHERE item_variation_id = par_item_variation_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-------------------------------------------------------------------------------
-- select images_get(null);
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION item_variation_options_get(IN par_item_variation_option_id INT)
  RETURNS SETOF item_variation_options AS $$
BEGIN
  IF par_item_variation_option_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM item_variation_options;
  ELSE
    RETURN QUERY SELECT *
                 FROM item_variation_options
                 WHERE item_variation_option_id = par_item_variation_option_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-------------------------------------------------------------------------------
-- select images_get(null);
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION items_upsert(IN par_item_id      INT, IN par_site_id INT, IN par_serial_no TEXT,
                                        IN par_tax_class_id INT, IN par_type_id INT, IN par_name TEXT,
                                        IN par_description  TEXT, IN par_date_added DATE, IN par_date_updated DATE,
                                        IN par_is_taxable   BOOLEAN,
                                        IN par_is_active    BOOLEAN, IN par_has_variations BOOLEAN)
  RETURNS TEXT AS $$
DECLARE
  loc_response INT;
BEGIN

  IF par_item_id ISNULL
  THEN
    INSERT INTO items (site_id, serial_no, tax_class_id, type_id, name, description, date_added, date_updated, is_taxable, is_active, has_variations)
    VALUES (par_site_id, par_serial_no, par_tax_class_id, par_type_id, par_name, par_description, par_date_added,
                         par_date_updated, par_is_taxable, par_is_active, par_has_variations)
    RETURNING item_id
      INTO loc_response;
  ELSE
    UPDATE items
    SET site_id    = par_site_id, serial_no = par_serial_no, tax_class_id = par_tax_class_id, type_id = par_type_id,
      name         = par_name, description = par_description, date_added = par_date_added,
      date_updated = par_date_updated, is_taxable = par_is_taxable,
      is_active    = par_is_active, has_variations = par_has_variations
    WHERE item_id = par_item_id;
    loc_response = par_item_id;
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
--------------------------------------------------------------------------------------------------------
-- SELECT * FROM items_upsert(NULL, NULL, 'SN153', NULL, NULL, 'Apple', 'test desc', NULL, NULL, TRUE, TRUE, TRUE);
--------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION items_get(IN par_item_id INT)
  RETURNS SETOF items AS $$
BEGIN
  IF par_item_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM items;
  ELSE
    RETURN QUERY SELECT *
                 FROM items
                 WHERE item_id = par_item_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT * FROM items_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION location_items_upsert(IN par_location_item_id INT, IN par_location_id INT,
                                                 IN par_item_id          INT, IN par_area_id INT, IN par_notes TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN

  IF par_location_item_id ISNULL
  THEN
    INSERT INTO location_items (location_id, item_id, area_id, notes)
    VALUES (par_location_id, par_item_id, par_area_id, par_notes);
    loc_response = 'ok';
  ELSE
    UPDATE location_items
    SET location_id = par_location_id, item_id = par_item_id, area_id = par_area_id, notes = par_notes
    WHERE location_item_id = par_location_item_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
--------------------------------------------------------------------------------------------------------
-- SELECT items_upsert(null, null, 'SN153', null, null, 'Fruits', 'test desc', null, null, true, 10.01, true, true);
--------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION location_items_get(IN par_location_item_id INT)
  RETURNS SETOF location_items AS $$
BEGIN
  IF par_location_item_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM location_items;
  ELSE
    RETURN QUERY SELECT *
                 FROM location_items
                 WHERE location_item_id = par_location_item_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from items_get(null);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION images_upsert(
  IN par_image_id  INT,
  IN par_item_id   INT,
  IN par_image_url TEXT,
  IN par_caption   TEXT)
  RETURNS TEXT AS $$

DECLARE
  loc_response TEXT;
BEGIN

  -- If no product_image_id was passed, then create a new row else update the row
  IF par_image_id ISNULL
  THEN
    INSERT INTO images (item_id, image_url, caption)
    VALUES (par_item_id, par_image_url, par_caption);
    loc_response = 'ok';
  ELSE
    UPDATE images
    SET item_id = par_item_id, image_url = par_image_url, caption = par_caption
    WHERE image_id = par_image_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT product_images_upsert(NULL, 1, 'url2', 'ho', 0);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION images_get(IN par_image_id INT, IN par_product_image_id INT)
  RETURNS SETOF images AS $$
BEGIN
  IF par_image_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM images;
  ELSE
    RETURN QUERY SELECT *
                 FROM images
                 WHERE image_id = par_image_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from product_images_get(1, null);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION types_upsert(IN par_type_id INT, IN par_name TEXT, IN par_description TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response INT;
BEGIN
  IF par_type_id ISNULL
  THEN
    INSERT INTO types (type_name, type_description) VALUES (par_name, par_description)
    RETURNING type_id
      INTO loc_response;
  ELSE
    UPDATE types
    SET type_name = par_name, type_description = par_description
    WHERE type_id = par_type_id;
    loc_response = par_type_id;
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT types_upsert(NULL, 'test', 'test description 2');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION types_get(IN par_type_id INT)
  RETURNS SETOF types AS $$
BEGIN
  IF par_type_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM types;
  ELSE
    RETURN QUERY SELECT *
                 FROM types
                 WHERE type_id = par_type_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT * FROM types_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION locations_upsert(IN par_location_id INT, IN par_location_name TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_location_id ISNULL
  THEN
    INSERT INTO locations (location_name) VALUES (par_location_name);
    loc_response = 'ok';
  ELSE
    UPDATE locations
    SET location_name = par_location_name
    WHERE location_id = par_location_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION locations_get(IN par_location_id INT)
  RETURNS SETOF locations AS $$
BEGIN
  IF par_location_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM locations;
  ELSE
    RETURN QUERY SELECT *
                 FROM locations
                 WHERE location_id = par_location_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT * FROM locations_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION option_groups_upsert(IN par_option_group_id          INT, IN par_option_group_name TEXT,
                                                IN par_option_group_description TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_option_group_id ISNULL
  THEN
    INSERT INTO option_groups (option_group_name, option_group_description)
    VALUES (par_option_group_name, par_option_group_description);
    loc_response = 'ok';
  ELSE
    UPDATE option_groups
    SET option_group_name = par_option_group_name, option_group_description = par_option_group_description
    WHERE option_group_id = par_option_group_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION option_groups_get(IN option_group_id INT)
  RETURNS SETOF locations AS $$
BEGIN
  IF par_option_group_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM option_groups;
  ELSE
    RETURN QUERY SELECT *
                 FROM option_groups
                 WHERE option_group_id = par_option_group_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from locations_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION options_upsert(IN par_option_id INT, IN par_option_group_id INT, IN par_option_value TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_option_id ISNULL
  THEN
    INSERT INTO options (option_group_id, option_value) VALUES (par_option_group_id, par_option_value);
    loc_response = 'ok';
  ELSE
    UPDATE options
    SET option_group_id = par_option_group_id, option_value = par_option_id
    WHERE option_id = par_option_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION options_get(IN par_option_id INT)
  RETURNS SETOF options AS $$
BEGIN
  IF par_option_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM options;
  ELSE
    RETURN QUERY SELECT *
                 FROM options
                 WHERE option_id = par_option_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from locations_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION purchase_order_items_upsert(IN par_purchase_order_item_id INT, IN par_purchase_order_id INT,
                                                       IN par_supplier_part_no       TEXT, IN par_quantity NUMERIC,
                                                       IN par_unit_cost              NUMERIC,
                                                       IN par_total_ordered          NUMERIC,
                                                       IN par_total_received         NUMERIC, IN par_discount NUMERIC,
                                                       IN par_discount_percentage    NUMERIC,
                                                       IN par_tax_percentage         NUMERIC)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_purchase_order_item_id ISNULL
  THEN
    INSERT INTO purchase_order_items (purchase_order_id, supplier_part_no, quantity, unit_cost, total_ordered, total_received, discount, discount_percentage, tax_percentage)
    VALUES
      (par_purchase_order_id, par_supplier_part_no, par_quantity, par_unit_cost, par_total_ordered, par_total_received,
       par_discount, par_discount_percentage, par_tax_percentage);
    loc_response = 'ok';
  ELSE
    UPDATE purchase_order_items
    SET purchase_order_id = par_purchase_order_id, supplier_part_no = par_supplier_part_no, quantity = par_quantity,
      unit_cost           = par_unit_cost, total_ordered = par_total_ordered, total_received = par_total_received,
      discount            = par_discount, discount_percentage = par_discount_percentage,
      tax_percentage      = par_tax_percentage
    WHERE purchase_order_item_id = par_purchase_order_item_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION purchase_order_items_get(IN par_purchase_order_item_id INT)
  RETURNS SETOF purchase_order_items AS $$
BEGIN
  IF par_purchase_order_item_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM purchase_order_items;
  ELSE
    RETURN QUERY SELECT *
                 FROM purchase_order_items
                 WHERE purchase_order_item_id = par_purchase_order_item_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from locations_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION purchase_order_upsert(IN par_purchase_order_id INT, IN par_vendor_id INT,
                                                 IN par_date_issued       DATE, IN par_date_expected DATE,
                                                 IN par_status            TEXT, IN par_reference_no TEXT,
                                                 IN par_notes             TEXT, IN par_shipping_fee NUMERIC,
                                                 IN par_tracking_no       TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_purchase_order_id ISNULL
  THEN
    INSERT INTO purchase_orders (vendor_id, date_issued, date_expected, status, reference_no, notes, shipping_fee, tracking_no)
    VALUES
      (par_vendor_id, par_date_issued, par_date_expected, par_status, par_reference_no, par_notes, par_shipping_fee,
       par_tracking_no);
    loc_response = 'ok';
  ELSE
    UPDATE purchase_orders
    SET vendor_id = par_vendor_id, date_issued = par_date_issued, date_expected = par_date_expected,
      status      = par_status, reference_no = par_reference_no, notes = par_notes, shipping_fee = par_shipping_fee,
      tracking_no = par_tracking_no
    WHERE purchase_order_id = par_purchase_order_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION purchase_order_get(IN par_purchase_order_id INT)
  RETURNS SETOF purchase_orders AS $$
BEGIN
  IF par_purchase_order_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM purchase_orders;
  ELSE
    RETURN QUERY SELECT *
                 FROM purchase_orders
                 WHERE purchase_order_id = par_purchase_order_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from locations_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION sites_upsert(IN par_site_id       INT, IN par_owner_id INT, IN par_name TEXT,
                                        IN par_business_code TEXT, IN par_domain TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_site_id ISNULL
  THEN
    INSERT INTO sites (owner_id, name, business_code, domain)
    VALUES (par_owner_id, par_name, par_business_code, par_domain);
    loc_response = 'ok';
  ELSE
    UPDATE sites
    SET owner_id = par_owner_id, name = par_name, business_code = par_business_code, domain = par_domain
    WHERE site_id = par_site_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION sites_get(IN par_site_id INT)
  RETURNS SETOF purchase_orders AS $$
BEGIN
  IF par_site_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM sites;
  ELSE
    RETURN QUERY SELECT *
                 FROM sites
                 WHERE site_id = par_site_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from locations_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION stock_adjustments_upsert(IN par_stock_adjustment_id INT, IN par_item_id INT,
                                                    IN par_new_quantity        NUMERIC)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_stock_adjustment_id ISNULL
  THEN
    INSERT INTO stock_adjustments (item_id, new_quantity) VALUES (par_item_id, par_new_quantity);
    loc_response = 'ok';
  ELSE
    UPDATE stock_adjustments
    SET item_id = par_item_id, new_quantity = par_new_quantity
    WHERE stock_adjustment_id = par_stock_adjustment_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION stock_adjustments_get(IN par_stock_adjustment_id INT)
  RETURNS SETOF stock_adjustments AS $$
BEGIN
  IF par_stock_adjustment_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM stock_adjustments;
  ELSE
    RETURN QUERY SELECT *
                 FROM stock_adjustments
                 WHERE stock_adjustment_id = par_stock_adjustment_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from locations_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION tax_classes_upsert(IN par_tax_class_id INT, IN par_name TEXT, IN par_tax_percentage NUMERIC,
                                              IN par_description  TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_tax_class_id ISNULL
  THEN
    INSERT INTO tax_classes (name, tax_percentage, description) VALUES (par_name, par_tax_percentage, par_description);
    loc_response = 'ok';
  ELSE
    UPDATE tax_classes
    SET name = par_name, tax_class_id = par_tax_percentage, description = par_description
    WHERE tax_class_id = par_tax_class_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION tax_classes_get(IN par_tax_class_id INT)
  RETURNS SETOF tax_classes AS $$
BEGIN
  IF par_tax_class_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM tax_classes;
  ELSE
    RETURN QUERY SELECT *
                 FROM tax_classes
                 WHERE tax_class_id = par_tax_class_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from locations_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION vendors_upsert(IN par_vendor_id        INT, IN par_name TEXT, IN par_billing_address TEXT,
                                          IN par_shipping_address VARCHAR(100))
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_vendor_id ISNULL
  THEN
    INSERT INTO vendors (name, billing_address, shipping_address)
    VALUES (par_name, par_billing_address, par_shipping_address);
    loc_response = 'ok';
  ELSE
    UPDATE vendors
    SET name = par_name, billing_address = par_billing_address, shipping_address = par_shipping_address
    WHERE vendor_id = par_vendor_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION vendors_get(IN par_vendor_id INT)
  RETURNS SETOF vendors AS $$
BEGIN
  IF par_vendor_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM vendors;
  ELSE
    RETURN QUERY SELECT *
                 FROM vendors
                 WHERE vendor_id = par_vendor_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from locations_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION transfer_items_upsert(IN par_transfer_item_id INT, IN par_item_id INT,
                                                 IN par_transfer_id      INT, IN par_quantity NUMERIC)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_transfer_item_id ISNULL
  THEN
    INSERT INTO transfer_items (item_id, transfer_id, quantity) VALUES (par_item_id, par_transfer_id, par_quantity);
    loc_response = 'ok';
  ELSE
    UPDATE transfer_items
    SET item_id = par_item_id, transfer_id = par_transfer_id, quantity = par_quantity
    WHERE transfer_item_id = par_transfer_item_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION transfer_items_get(IN par_transfer_item_id INT)
  RETURNS SETOF transfer_items AS $$
BEGIN
  IF par_transfer_item_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM transfer_items;
  ELSE
    RETURN QUERY SELECT *
                 FROM transfer_items
                 WHERE transfer_item_id = par_transfer_item_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from locations_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION transfers_upsert(IN par_transfer_id          INT, IN par_source_location INT,
                                            IN par_destination_location INT, IN par_date_transferred DATE)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_transfer_id ISNULL
  THEN
    INSERT INTO transfers (source_location, destination_location, date_transferred)
    VALUES (par_source_location, par_destination_location, par_date_transferred);
    loc_response = 'ok';
  ELSE
    UPDATE transfers
    SET source_location = par_source_location, destination_location = par_destination_location,
      date_transferred  = par_date_transferred
    WHERE transfer_id = par_transfer_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION transfers_get(IN par_transfer_id INT)
  RETURNS SETOF transfers AS $$
BEGIN
  IF par_transfer_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM transfers;
  ELSE
    RETURN QUERY SELECT *
                 FROM transfers
                 WHERE transfer_id = par_transfer_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from locations_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION sales_order_items_upsert(IN par_sales_order_item_id INT, IN par_item_id INT,
                                                    IN par_sales_order_id      INT, IN par_quantity NUMERIC,
                                                    IN par_actual_unit_cost    NUMERIC, IN par_discount NUMERIC,
                                                    IN par_discount_percentage NUMERIC, IN par_total_cost NUMERIC)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_sales_order_item_id ISNULL
  THEN
    INSERT INTO sales_order_items (item_id, sales_order_id, quantity, actual_unit_cost, discount, discount_percentage, total_cost)
    VALUES (par_item_id, par_sales_order_id, par_quantity, par_actual_unit_cost, par_discount, par_discount_percentage,
            par_total_cost);
    loc_response = 'ok';
  ELSE
    UPDATE sales_order_items
    SET item_id        = par_item_id, sales_order_id = par_sales_order_id, quantity = par_quantity,
      actual_unit_cost = par_actual_unit_cost, discount = par_discount, discount_percentage = par_discount_percentage,
      total_cost       = par_total_cost
    WHERE sales_order_item_id = par_sales_order_item_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION sales_order_items_get(IN par_sales_order_item_id INT)
  RETURNS SETOF sales_order_items AS $$
BEGIN
  IF par_sales_order_item_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM sales_order_items;
  ELSE
    RETURN QUERY SELECT *
                 FROM sales_order_items
                 WHERE sales_order_item_id = par_sales_order_item_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from locations_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION sales_orders_upsert(IN par_sales_order_id INT, IN par_created_by INT, IN par_customer_id INT,
                                               IN par_created_at     TIMESTAMP, IN par_or_number TEXT,
                                               IN par_reference_no   TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_sales_order_id ISNULL
  THEN
    INSERT INTO sales_orders (created_by, customer_id, created_at, or_number, reference_no)
    VALUES (par_created_by, par_customer_id, par_created_at, par_or_number, par_reference_no);
    loc_response = 'ok';
  ELSE
    UPDATE sales_orders
    SET created_by = par_created_by, customer_id = par_customer_id, created_at = par_created_at,
      or_number    = par_or_number, reference_no = par_reference_no
    WHERE sales_order_id = par_sales_order_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION sales_orders_get(IN par_sales_order_id INT)
  RETURNS SETOF sales_orders AS $$
BEGIN
  IF par_sales_order_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM sales_orders;
  ELSE
    RETURN QUERY SELECT *
                 FROM sales_orders
                 WHERE sales_order_id = par_sales_order_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- select * from locations_get(NULL);
-----------------------------------------------------------------


