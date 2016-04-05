CREATE TABLE areas (
  area_id          SERIAL UNIQUE NOT NULL PRIMARY KEY,
  area_description TEXT
);

CREATE TABLE customers (
  customer_id      SERIAL NOT NULL PRIMARY KEY,
  name             TEXT,
  billing_address  TEXT,
  shipping_address VARCHAR(100)
);

CREATE TABLE locations (
  location_id   SERIAL UNIQUE NOT NULL PRIMARY KEY,
  location_name TEXT          NOT NULL
);

CREATE TABLE option_groups (
  option_group_id          SERIAL NOT NULL PRIMARY KEY,
  option_group_name        TEXT,
  option_group_description TEXT
);

CREATE TABLE options (
  option_id       SERIAL NOT NULL PRIMARY KEY,
  option_group_id INTEGER REFERENCES option_groups,
  option_value    TEXT
);

CREATE TABLE tax_classes (
  tax_class_id   SERIAL NOT NULL PRIMARY KEY,
  name           TEXT,
  tax_percentage NUMERIC,
  description    TEXT
);

CREATE TABLE transfers (
  transfer_id          SERIAL NOT NULL PRIMARY KEY,
  source_location      INTEGER REFERENCES locations,
  destination_location INTEGER REFERENCES locations,
  date_transferred     TIMESTAMP DEFAULT now()
);

CREATE TABLE types (
  type_id          SERIAL NOT NULL PRIMARY KEY,
  type_name        TEXT,
  type_description TEXT
);

CREATE TABLE users (
  user_id      SERIAL       NOT NULL PRIMARY KEY,
  username     VARCHAR(100) NOT NULL UNIQUE,
  email        VARCHAR(100) NOT NULL,
  password     VARCHAR(100) NOT NULL,
  date_created TIMESTAMP DEFAULT now()
);

CREATE TABLE vendors (
  vendor_id        SERIAL NOT NULL PRIMARY KEY,
  name             TEXT,
  billing_address  TEXT,
  shipping_address VARCHAR(100)
);

CREATE TABLE attributes (
  attribute_id   SERIAL NOT NULL PRIMARY KEY,
  attribute_name TEXT,
  validation     TEXT,
  type_id        INTEGER REFERENCES types
);

CREATE TABLE purchase_orders (
  purchase_order_id SERIAL NOT NULL PRIMARY KEY,
  date_issued       TIMESTAMP DEFAULT now(),
  date_expected     TIMESTAMP,
  status            TEXT,
  reference_no      TEXT,
  notes             TEXT,
  shipping_fee      NUMERIC,
  tracking_no       TEXT,
  vendor_id         INTEGER REFERENCES vendors
);

CREATE TABLE sales_orders (
  sales_order_id SERIAL NOT NULL PRIMARY KEY,
  created_at     TIMESTAMP DEFAULT now(),
  created_by     INTEGER REFERENCES users,
  customer_id    INTEGER REFERENCES customers,
  or_number      TEXT,
  reference_no   TEXT
);

CREATE TABLE sites (
  site_id       SERIAL NOT NULL PRIMARY KEY,
  name          TEXT,
  business_code TEXT,
  owner_id      INTEGER REFERENCES users,
  domain        TEXT
);

CREATE TABLE items (
  item_id        SERIAL NOT NULL PRIMARY KEY,
  serial_no      TEXT,
  site_id        INTEGER REFERENCES sites,
  name           TEXT,
  description    TEXT,
  date_added     TIMESTAMP DEFAULT now(),
  date_updated   TIMESTAMP DEFAULT now(),
  is_taxable     BOOL DEFAULT TRUE,
  is_active      BOOL DEFAULT TRUE,
  has_variations BOOL DEFAULT FALSE,
  tax_class_id   INTEGER REFERENCES tax_classes,
  type_id        INTEGER REFERENCES types
);

CREATE TABLE location_items (
  location_item_id SERIAL NOT NULL PRIMARY KEY,
  notes            TEXT,
  location_id      INTEGER REFERENCES locations,
  item_id          INTEGER REFERENCES items,
  area_id          INTEGER REFERENCES areas
);

CREATE TABLE purchase_order_items (
  purchase_order_item_id SERIAL NOT NULL PRIMARY KEY,
  supplier_part_no       TEXT,
  quantity               NUMERIC DEFAULT 0,
  unit_cost              NUMERIC DEFAULT 0,
  total_ordered          NUMERIC,
  total_received         NUMERIC,
  purchase_order_id      INTEGER REFERENCES purchase_orders,
  discount               NUMERIC,
  discount_percentage    NUMERIC,
  tax_percentage         NUMERIC
);

CREATE TABLE sales_order_items (
  sales_order_item_id SERIAL NOT NULL PRIMARY KEY,
  quantity            NUMERIC,
  actual_unit_cost    NUMERIC,
  discount            NUMERIC,
  discount_percentage NUMERIC,
  total_cost          NUMERIC,
  item_id             INTEGER REFERENCES items,
  sales_order_id      INTEGER REFERENCES sales_orders
);

CREATE TABLE stock_adjustments (
  stock_adjustment_id SERIAL NOT NULL PRIMARY KEY,
  item_id             INTEGER REFERENCES items,
  new_quantity        NUMERIC
);

CREATE TABLE transfer_items (
  transfer_item_id SERIAL NOT NULL PRIMARY KEY,
  quantity         NUMERIC,
  item_id          INTEGER REFERENCES items,
  transfer_id      INTEGER REFERENCES transfers
);

CREATE TABLE images (
  image_id  SERIAL NOT NULL PRIMARY KEY,
  image_url TEXT,
  item_id   INTEGER REFERENCES items,
  caption   TEXT
);

CREATE TABLE item_attributes (
  item_attribute_id SERIAL NOT NULL PRIMARY KEY,
  attribute_value   TEXT,
  attribute_id      INTEGER REFERENCES attributes,
  item_id           INTEGER REFERENCES items
);

CREATE TABLE item_variations (
  item_variation_id SERIAL NOT NULL PRIMARY KEY,
  stock_on_hand     NUMERIC DEFAULT 0,
  unit_cost         NUMERIC,
  re_order_level    NUMERIC,
  re_order_quantity NUMERIC,
  is_active         BOOL,
  item_id           INTEGER REFERENCES items
);

CREATE TABLE item_variation_options (
  item_variation_option_id SERIAL  NOT NULL PRIMARY KEY,
  option_id                INTEGER NOT NULL REFERENCES options,
  item_variation_id        INTEGER REFERENCES item_variations
);

