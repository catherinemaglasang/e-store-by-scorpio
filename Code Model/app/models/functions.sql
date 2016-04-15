CREATE OR REPLACE FUNCTION attributes_upsert(IN par_attribute_id   INT,
                                             IN par_attribute_name TEXT, IN par_validation TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN

  IF par_attribute_id ISNULL
  THEN
    INSERT INTO attributes (attribute_name, validation)
    VALUES (par_attribute_name, par_validation);
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
CREATE OR REPLACE FUNCTION attributes_get(IN par_attribute_id INT)
  RETURNS SETOF attributes AS $$
BEGIN
  IF par_attribute_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM attributes;
  ELSE
    RETURN QUERY SELECT *
                 FROM attributes
                 WHERE attribute_id = par_attribute_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
--------------------------------------------------------------------------------------------------------
-- SELECT attributes_get(NULL, 1);
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
CREATE OR REPLACE FUNCTION item_attributes_upsert(IN par_attribute_id INT,
                                                  IN par_item_id      INT, IN par_attribute_value TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
  loc_id       INT;
BEGIN
  SELECT INTO loc_id attribute_id
  FROM item_attributes
  WHERE attribute_id = par_attribute_id AND item_id = par_item_id;
  IF loc_id ISNULL
  THEN
    INSERT INTO item_attributes (attribute_id, item_id, attribute_value)
    VALUES (par_attribute_id, par_item_id, par_attribute_value);
    loc_response = 'ok';
  ELSE
    UPDATE item_attributes
    SET attribute_value = par_attribute_value
    WHERE item_id = par_item_id AND attribute_id = par_attribute_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-------------------------------------------------------------------------------
-- select images_get(null);
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION item_attributes_get(IN par_attribute_id INT, IN par_item_id INT)
  RETURNS SETOF item_attributes AS $$
BEGIN
  IF par_attribute_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM item_attributes
                 WHERE item_id = par_item_id;
  ELSE
    RETURN QUERY SELECT *
                 FROM item_attributes
                 WHERE attribute_id = par_attribute_id AND item_id = par_item_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-------------------------------------------------------------------------------
-- select images_get(null);
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION item_variations_upsert(IN par_item_id        INT, IN par_option_id INT,
                                                  IN par_stock_on_hand  NUMERIC, IN par_unit_cost NUMERIC,
                                                  IN par_re_order_level NUMERIC, IN par_re_order_quantity NUMERIC,
                                                  IN par_is_active      BOOLEAN)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
  loc_id       INT;
BEGIN

  SELECT INTO loc_id item_id
  FROM item_variations
  WHERE item_id = par_item_id AND option_id = par_option_id;
  IF loc_id ISNULL
  THEN
    INSERT INTO item_variations (item_id, option_id, stock_on_hand, unit_cost, re_order_level, re_order_quantity, is_active)
    VALUES (par_item_id, par_option_id, par_stock_on_hand, par_unit_cost, par_re_order_level, par_re_order_quantity,
            par_is_active);
    loc_response = 'ok';
  ELSE
    UPDATE item_variations
    SET option_id    = par_option_id, stock_on_hand = par_stock_on_hand, unit_cost = par_unit_cost,
      re_order_level = par_re_order_level, re_order_quantity = par_re_order_quantity, is_active = par_is_active
    WHERE item_id = par_item_id AND option_id = par_option_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-------------------------------------------------------------------------------
-- select images_get(null);
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION item_variations_get(IN par_item_id INT, IN par_option_id INT)
  RETURNS SETOF item_variations AS $$
BEGIN
  IF par_option_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM item_variations
                 WHERE item_id = par_item_id;
  ELSE
    RETURN QUERY SELECT *
                 FROM item_variations
                 WHERE item_id = par_item_id AND option_id = par_option_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-------------------------------------------------------------------------------
-- select images_get(null);
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION items_upsert(IN par_item_id     INT, IN par_name TEXT,
                                        IN par_description TEXT, IN par_date_added DATE, IN par_date_updated DATE,
                                        IN par_is_active   BOOLEAN)
  RETURNS TEXT AS $$
DECLARE
  loc_response INT;
BEGIN

  IF par_item_id ISNULL
  THEN
    INSERT INTO items (name, description, date_added, date_updated, is_active)
    VALUES (par_name, par_description, par_date_added,
            par_date_updated, par_is_active)
    RETURNING item_id
      INTO loc_response;
  ELSE
    UPDATE items
    SET name       = par_name, description = par_description, date_added = par_date_added,
      date_updated = par_date_updated,
      is_active    = par_is_active
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
                                                 IN par_item_id          INT, IN par_notes TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN

  IF par_location_item_id ISNULL
  THEN
    INSERT INTO location_items (location_id, item_id, notes)
    VALUES (par_location_id, par_item_id, par_notes);
    loc_response = 'ok';
  ELSE
    UPDATE location_items
    SET location_id = par_location_id, item_id = par_item_id, notes = par_notes
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
CREATE OR REPLACE FUNCTION option_groups_upsert(IN par_option_group_id INT, IN par_option_group_name TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_option_group_id ISNULL
  THEN
    INSERT INTO option_groups (option_group_name)
    VALUES (par_option_group_name);
    loc_response = 'ok';
  ELSE
    UPDATE option_groups
    SET option_group_name = par_option_group_name
    WHERE option_group_id = par_option_group_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION option_groups_get(IN par_option_group_id INT)
  RETURNS SETOF option_groups AS $$
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
    SET option_value = par_option_value
    WHERE option_id = par_option_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION options_get(IN par_option_id INT, IN par_option_group_id INT)
  RETURNS SETOF options AS $$
BEGIN
  IF par_option_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM options
                 WHERE option_group_id = par_option_group_id;
  ELSE
    RETURN QUERY SELECT *
                 FROM options
                 WHERE option_id = par_option_id AND option_group_id = par_option_group_id;
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
CREATE OR REPLACE FUNCTION purchase_order_upsert(IN par_purchase_order_id INT, IN par_supplier_id INT,
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
    INSERT INTO purchase_orders (supplier_id, date_issued, date_expected, status, reference_no, notes, shipping_fee, tracking_no)
    VALUES
      (par_supplier_id, par_date_issued, par_date_expected, par_status, par_reference_no, par_notes, par_shipping_fee,
       par_tracking_no);
    loc_response = 'ok';
  ELSE
    UPDATE purchase_orders
    SET supplier_id = par_supplier_id, date_issued = par_date_issued, date_expected = par_date_expected,
      status        = par_status, reference_no = par_reference_no, notes = par_notes, shipping_fee = par_shipping_fee,
      tracking_no   = par_tracking_no
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
CREATE OR REPLACE FUNCTION suppliers_upsert(IN par_supplier_id INT, IN par_name TEXT, IN par_address TEXT,
                                            IN par_phone       TEXT,
                                            IN par_fax         TEXT, IN par_email TEXT, IN par_is_active BOOLEAN)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_supplier_id ISNULL
  THEN
    INSERT INTO suppliers (name, address, phone, fax, email, is_active)
    VALUES (par_name, par_address, par_phone, par_fax, par_email, par_is_active);
    loc_response = 'ok';
  ELSE
    UPDATE suppliers
    SET name    = par_name, address = par_address, phone = par_phone, fax = par_fax, email = par_email,
      is_active = par_is_active
    WHERE supplier_id = par_supplier_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION suppliers_get(IN par_supplier_id INT)
  RETURNS SETOF suppliers AS $$
BEGIN
  IF par_supplier_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM suppliers;
  ELSE
    RETURN QUERY SELECT *
                 FROM suppliers
                 WHERE supplier_id = par_supplier_id;
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



--////////////////////////////////////////////////////////////---

-- To Sort

-----------------------------------------------------------------
-- select * from locations_get(NULL);
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION wishlists_upsert(IN par_wishlist_id INT, IN par_wishlist_name TEXT)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
BEGIN
  IF par_wishlist_id ISNULL
  THEN
    INSERT INTO wishlists (wishlist_name)
    VALUES (par_wishlist_name);
    loc_response = 'ok';
  ELSE
    UPDATE wishlists
    SET wishlist_name = par_wishlist_name
    WHERE wishlist_id = par_wishlist_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION wishlists_get(IN par_wishlist_id INT)
  RETURNS SETOF wishlists AS $$
BEGIN
  IF par_wishlist_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM wishlists;
  ELSE
    RETURN QUERY SELECT *
                 FROM wishlists
                 WHERE wishlist_id = par_wishlist_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION wishlist_items_upsert(IN par_wishlist_id INT, IN par_item_id INT,
                                                 IN par_time_stamp  TIMESTAMP)
  RETURNS TEXT AS $$
DECLARE
  loc_response TEXT;
  loc_id       INT;
BEGIN
  SELECT INTO loc_id wishlist_id
  FROM wishlist_items
  WHERE item_id = par_item_id AND wishlist_id = par_wishlist_id;

  IF loc_id ISNULL
  THEN
    INSERT INTO wishlist_items (wishlist_id, item_id, time_stamp)
    VALUES (par_wishlist_id, par_item_id, par_time_stamp);
    loc_response = 'ok';
  ELSE
    UPDATE wishlist_items
    SET time_stamp = par_time_stamp
    WHERE wishlist_id = par_wishlist_id AND item_id = par_item_id;
    loc_response = 'ok';
  END IF;

  RETURN loc_response;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------
CREATE OR REPLACE FUNCTION wishlist_items_get(IN par_wishlist_id INT, IN par_item_id INT)
  RETURNS SETOF wishlist_items AS $$
BEGIN
  IF par_item_id ISNULL
  THEN
    RETURN QUERY SELECT *
                 FROM wishlist_items
                 WHERE wishlist_id = par_wishlist_id;
  ELSE
    RETURN QUERY SELECT *
                 FROM wishlist_items
                 WHERE wishlist_id = par_wishlist_id AND item_id = par_item_id;
  END IF;
END;
$$ LANGUAGE 'plpgsql';
-----------------------------------------------------------------
-- SELECT locations_upsert(NULL, 'test');
-----------------------------------------------------------------


CREATE OR REPLACE FUNCTION new_user(IN par_username     TEXT, IN par_email TEXT, IN par_password TEXT,
                                    IN par_date_created TIMESTAMP, IN par_is_admin BOOLEAN)
  RETURNS TEXT AS
$$
DECLARE
  loc_id  TEXT;
  loc_res TEXT;
  loc_user text;
BEGIN
  SELECT INTO loc_user username
  FROM users
  WHERE username = par_username;
  IF loc_user ISNULL
  THEN
    IF par_username = '' OR par_password = '' OR par_email = ''
    THEN
      loc_res='error';
    ELSE
      INSERT INTO users (username, email, password, date_created, is_admin)
      VALUES (par_username, par_email, par_password, par_date_created, par_is_admin);
      loc_res = 'OK';
    END IF;
  ELSE
    loc_res = 'USER EXISTS';
  END IF;
  RETURN loc_res;
END;
$$
LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION get_users(OUT INT, OUT VARCHAR(100), OUT VARCHAR(100), OUT TIMESTAMP, OUT BOOLEAN)
  RETURNS SETOF RECORD AS
$$
SELECT
  user_id,
  username,
  email,
  date_created,
  is_admin
FROM users;
$$
LANGUAGE 'sql';

--select * from get_users();

CREATE OR REPLACE FUNCTION get_user(IN par_id INT, OUT INT, OUT VARCHAR(100), OUT VARCHAR(100), OUT TIMESTAMP,
                                    OUT       BOOLEAN)
  RETURNS SETOF RECORD AS
$$
SELECT
  user_id,
  username,
  email,
  date_created,
  is_admin
FROM users
WHERE user_id = par_id
$$
LANGUAGE 'sql';

--select * from get_user(1);

CREATE OR REPLACE FUNCTION new_supplier(IN par_id  INT, IN par_name TEXT, IN par_address TEXT, IN par_phone TEXT,
                                        IN par_fax TEXT, IN par_email TEXT, IN par_is_active BOOLEAN)
  RETURNS TEXT AS
$$
DECLARE
  loc_id  TEXT;
  loc_res TEXT;
BEGIN
  SELECT INTO loc_id name
  FROM suppliers
  WHERE name = par_name;
  IF loc_id ISNULL
  THEN
    IF par_name = '' OR par_address = '' OR par_phone = '' OR par_fax = '' OR par_email = ''
    THEN
      loc_res='error';
    ELSE
      INSERT INTO suppliers (name, address, phone, fax, email, is_active)
      VALUES (par_name, par_address, par_phone, par_fax, par_email, par_is_active);
      loc_res = 'OK';
    END IF;

  ELSE
    loc_res = 'SUPPLIER EXISTS';
  END IF;
  RETURN loc_res;
END;
$$
LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION get_suppliers(OUT INT, OUT TEXT, OUT TEXT, OUT TEXT, OUT TEXT, OUT TEXT, OUT BOOLEAN)
  RETURNS SETOF RECORD AS
$$
SELECT
  supplier_id,
  name,
  address,
  phone,
  fax,
  email,
  is_active
FROM suppliers;
$$
LANGUAGE 'sql';


CREATE OR REPLACE FUNCTION get_supplier(IN par_id INT, OUT TEXT, OUT TEXT, OUT TEXT, OUT TEXT, OUT TEXT, OUT BOOLEAN)
  RETURNS SETOF RECORD AS
$$
SELECT
  name,
  address,
  phone,
  fax,
  email,
  is_active
FROM suppliers
WHERE supplier_id = par_id;
$$
LANGUAGE 'sql';

CREATE OR REPLACE FUNCTION new_cart(IN par_id          INT, IN par_session_id INT, IN par_date_created DATE,
                                    IN par_customer_id INT, IN par_is_active BOOLEAN)
  RETURNS TEXT AS
$$
DECLARE
  loc_id  TEXT;
  loc_res TEXT;
BEGIN
  SELECT INTO loc_id id
  FROM carts
  WHERE id = par_id;
  IF loc_id ISNULL
  THEN

    INSERT INTO carts (id, session_id, date_created, customer_id, is_active)
    VALUES (par_id, par_session_id, par_date_created, par_customer_id, par_is_active);
    loc_res = 'OK';

  ELSE
    loc_res = 'ID EXISTS';
  END IF;
  RETURN loc_res;
END;
$$
LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION get_carts(OUT INT, OUT INT, OUT DATE, OUT INT, OUT BOOLEAN)
  RETURNS SETOF RECORD AS
$$
SELECT
  id,
  session_id,
  date_created,
  customer_id,
  is_active
FROM carts;
$$
LANGUAGE 'sql';

CREATE OR REPLACE FUNCTION get_cart(IN par_id INT, OUT INT, OUT DATE, OUT INT, OUT BOOLEAN)
  RETURNS SETOF RECORD AS
$$
SELECT
  session_id,
  date_created,
  customer_id,
  is_active
FROM carts
WHERE id = par_id;

$$
LANGUAGE 'sql';


CREATE OR REPLACE FUNCTION new_cart_item(IN par_id         INT, IN par_cart_id INT, IN par_item_id INT,
                                         IN par_quantity   INT, IN par_time_stamp TIMESTAMP)
  RETURNS TEXT AS
$$
DECLARE
  loc_id  TEXT;
  loc_res TEXT;
BEGIN
  SELECT INTO loc_id id
  FROM cart_items
  WHERE id = par_id;
  IF loc_id ISNULL
  THEN

    INSERT INTO cart_items (id, cart_id, item_id, quantity, time_stamp)
    VALUES (par_id, par_cart_id, par_item_id, par_quantity, par_time_stamp);
    loc_res = 'OK';

  ELSE
    loc_res = 'ID EXISTS';
  END IF;
  RETURN loc_res;
END;
$$

LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION get_cart_items(IN par_cart_id INT, OUT INT, OUT INT, OUT INT, OUT INT, OUT TIMESTAMP)
  RETURNS SETOF RECORD AS
$$
SELECT
  id,
  cart_id,
  item_id,
  quantity,
  time_stamp
FROM cart_items
WHERE cart_id = par_cart_id;
$$
LANGUAGE 'sql';


CREATE OR REPLACE FUNCTION get_cart_item(IN par_id INT, IN par_cart_id INT, OUT INT, OUT INT, OUT INT, OUT TIMESTAMP)
  RETURNS SETOF RECORD AS
$$
SELECT
  cart_id,
  item_id,
  quantity,
  time_stamp
FROM cart_items
WHERE cart_id = par_cart_id AND id = par_id;
$$
LANGUAGE 'sql';


create or replace function new_order(in par_id int, in par_customer_id int, in par_payment_id int, in par_transaction_date date, in par_shipping_date date, in par_time_stamp timestamp, in par_transaction_status text, par_total numeric) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
    select into loc_id order_id from orders where order_id=par_id;
    if loc_id isnull then
      if par_transaction_status='' or par_id isnull or par_customer_id isnull or par_payment_id isnull or par_total isnull then
          loc_res='error';
      else
          insert into orders(order_id, customer_id, payment_id, transaction_date, shipping_date, time_stamp, transaction_status, total) values (par_id, par_customer_id, par_payment_id, par_transaction_date, par_shipping_date, par_time_stamp, par_transaction_status, par_total);
          loc_res = 'OK';
      end if;
     else
       loc_res = 'ID EXISTS';
     end if;
     return loc_res;
  end;
$$
LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION get_wishlist(IN par_id INT, OUT INT, OUT TEXT)
  RETURNS SETOF RECORD AS
$$
SELECT
  wishlist_id,
  wishlist_name
FROM wishlists
WHERE wishlist_id = par_id;
$$
LANGUAGE 'sql';

CREATE OR REPLACE FUNCTION new_order(IN par_id               INT, IN par_customer_id INT, IN par_payment_id INT,
                                     IN par_transaction_date DATE, IN par_shipping_date DATE,
                                     IN par_time_stamp       TIMESTAMP, IN par_transaction_status TEXT,
                                        par_total            NUMERIC)
  RETURNS TEXT AS
$$
DECLARE
  loc_id  TEXT;
  loc_res TEXT;
BEGIN
  SELECT INTO loc_id order_id
  FROM orders
  WHERE order_id = par_id;
  IF loc_id ISNULL
  THEN
    IF par_transaction_status = '' OR par_id ISNULL OR par_customer_id ISNULL OR par_payment_id ISNULL OR
       par_total ISNULL
    THEN
      loc_res='error';
    ELSE
      INSERT INTO orders (order_id, customer_id, payment_id, transaction_date, shipping_date, time_stamp, transaction_status, total)
      VALUES (par_id, par_customer_id, par_payment_id, par_transaction_date, par_shipping_date, par_time_stamp,
              par_transaction_status, par_total);
      loc_res = 'OK';
    END IF;
  ELSE
    loc_res = 'ID EXISTS';
  END IF;
  RETURN loc_res;
END;
$$

LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION get_orders(OUT INT, OUT INT, OUT INT, OUT DATE, OUT DATE, OUT TIMESTAMP, OUT TEXT,
                                      OUT NUMERIC)
  RETURNS SETOF RECORD AS
$$
SELECT
  order_id,
  customer_id,
  payment_id,
  transaction_date,
  shipping_date,
  time_stamp,
  transaction_status,
  total
FROM orders
$$

LANGUAGE 'sql';

CREATE OR REPLACE FUNCTION get_order_id(IN par_id INT, OUT INT, OUT INT, OUT DATE, OUT DATE, OUT TIMESTAMP, OUT TEXT,
                                        OUT       NUMERIC)
  RETURNS SETOF RECORD AS
$$
SELECT
  customer_id,
  payment_id,
  transaction_date,
  shipping_date,
  time_stamp,
  transaction_status,
  total
FROM orders
WHERE order_id = par_id;

$$
LANGUAGE 'sql';


CREATE OR REPLACE FUNCTION new_order_item(IN par_id         INT, IN par_order_id INT, IN par_item_id INT,
                                          IN par_unit_price FLOAT8, IN par_discount FLOAT8, IN par_quantity INT)
  RETURNS TEXT AS
$$
DECLARE
  loc_id  TEXT;
  loc_res TEXT;
BEGIN
  SELECT INTO loc_id id
  FROM order_items
  WHERE id = par_id;
  IF loc_id ISNULL
  THEN
    IF par_item_id ISNULL OR par_id ISNULL OR par_order_id ISNULL OR par_unit_price ISNULL OR par_discount ISNULL OR
       par_quantity ISNULL
    THEN
      loc_res='error';
    ELSE
      INSERT INTO order_items (id, order_id, item_id, unit_price, discount, quantity)
      VALUES (par_id, par_order_id, par_item_id, par_unit_price, par_discount, par_quantity);
      loc_res = 'OK';
    END IF;
  ELSE
    loc_res = 'ID EXISTS';
  END IF;
  RETURN loc_res;
END;
$$

LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION get_order_items(OUT INT, OUT INT, OUT INT, OUT NUMERIC, OUT NUMERIC, OUT INT)
  RETURNS SETOF RECORD AS
$$
SELECT
  id,
  order_id,
  item_id,
  unit_price,
  discount,
  quantity
FROM order_items
$$

LANGUAGE 'sql';

CREATE OR REPLACE FUNCTION get_order_item_id(IN par_id INT, OUT INT, OUT INT, OUT NUMERIC, OUT NUMERIC, OUT INT)
  RETURNS SETOF RECORD AS
$$
SELECT
  order_id,
  item_id,
  unit_price,
  discount,
  quantity
FROM order_items
WHERE id = par_id;

$$
LANGUAGE 'sql';

CREATE OR REPLACE FUNCTION new_customer(IN par_id               INT, IN par_first_name TEXT, IN par_last_name TEXT,
                                        IN par_address          TEXT, IN par_city TEXT, IN par_state TEXT,
                                        IN par_postal_code      TEXT, IN par_country TEXT, IN par_phone TEXT,
                                        IN par_email            TEXT, IN par_user_id INT, IN par_billing_address TEXT,
                                        IN par_shipping_address TEXT, IN par_date_created TIMESTAMP)
  RETURNS TEXT AS
$$
DECLARE
  loc_id  TEXT;
  loc_res TEXT;
BEGIN
  SELECT INTO loc_id id
  FROM customers
  WHERE id = par_id;
  IF loc_id ISNULL
  THEN
    IF par_first_name = '' OR par_last_name = '' OR par_address = '' OR par_city = '' OR par_state = '' OR
       par_postal_code = '' OR par_country = '' OR par_phone = '' OR par_email = '' OR par_billing_address = '' OR
       par_shipping_address = ''
    THEN
      loc_res='error';
    ELSE
      INSERT INTO customers (id, first_name, last_name, address, city, state, postal_code, country, phone, email, user_id, billing_address, shipping_address, date_created)
      VALUES (par_id, par_first_name, par_last_name, par_address, par_city, par_state, par_postal_code, par_country,
                      par_phone, par_email, par_user_id, par_billing_address, par_shipping_address, par_date_created);
      loc_res = 'ok';
    END IF;
  ELSE
    loc_res = 'CUSTOMER EXISTS';
  END IF;
  RETURN loc_res;
END;
$$

LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION get_all_customers(OUT INT, OUT TEXT, OUT TEXT, OUT TEXT, OUT TEXT, OUT TEXT, OUT TEXT,
                                             OUT TEXT, OUT TEXT, OUT TEXT, OUT INT, OUT TEXT, OUT TEXT, OUT TIMESTAMP)
  RETURNS SETOF RECORD AS
$$
SELECT
  id,
  first_name,
  last_name,
  address,
  city,
  state,
  postal_code,
  country,
  phone,
  email,
  user_id,
  billing_address,
  shipping_address,
  date_created
FROM customers
$$
LANGUAGE 'sql';

CREATE OR REPLACE FUNCTION get_single_customer(IN par_id INT, OUT TEXT, OUT TEXT, OUT TEXT, OUT TEXT, OUT TEXT,
                                               OUT       TEXT, OUT TEXT, OUT TEXT, OUT TEXT, OUT INT, OUT TEXT,
                                               OUT       TEXT, OUT TIMESTAMP)
  RETURNS SETOF RECORD AS
$$
SELECT
  first_name,
  last_name,
  address,
  city,
  state,
  postal_code,
  country,
  phone,
  email,
  user_id,
  billing_address,
  shipping_address,
  date_created
FROM customers
WHERE id = par_id
$$
LANGUAGE 'sql';