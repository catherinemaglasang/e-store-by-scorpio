-- -------------------------------------
-- Authentication & Registration Module
-- -------------------------------------
CREATE TABLE customers (
  id               serial PRIMARY KEY,
  first_name       TEXT,
  last_name        TEXT,
  address          TEXT,
  city             TEXT,
  state            TEXT,
  postal_code      TEXT,
  country          TEXT,
  phone            TEXT,
  email            TEXT UNIQUE,
  user_id          INT,
  billing_address  TEXT,
  shipping_address TEXT,
  date_created     TIMESTAMP
);

CREATE TABLE users (
  user_id      SERIAL       NOT NULL PRIMARY KEY,
  username     VARCHAR(100) NOT NULL UNIQUE,
  email        VARCHAR(100) NOT NULL,
  password     VARCHAR(100) NOT NULL,
  date_created TIMESTAMP DEFAULT now(),
  is_admin     BOOLEAN
);

-- -------------------------------------
-- Inventory Module
-- -------------------------------------

CREATE TABLE suppliers (
  supplier_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
  name        TEXT,
  address     TEXT,
  phone       TEXT,
  fax         TEXT,
  email       TEXT,
  is_active   BOOLEAN
);

CREATE TABLE locations (
  location_id   SERIAL UNIQUE NOT NULL PRIMARY KEY,
  location_name TEXT          NOT NULL
);

CREATE TABLE option_groups (
  option_group_id   SERIAL NOT NULL PRIMARY KEY,
  option_group_name TEXT
);

CREATE TABLE options (
  option_id       SERIAL NOT NULL PRIMARY KEY,
  option_group_id INTEGER REFERENCES option_groups,
  option_value    TEXT
);


CREATE TABLE transfers (
  transfer_id          SERIAL NOT NULL PRIMARY KEY,
  source_location      INTEGER REFERENCES locations,
  destination_location INTEGER REFERENCES locations,
  date_transferred     TIMESTAMP DEFAULT now()
);

CREATE TABLE attributes (
  attribute_id   SERIAL NOT NULL PRIMARY KEY,
  attribute_name TEXT,
  validation     TEXT
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
  supplier_id       INTEGER REFERENCES suppliers
);

CREATE TABLE sales_orders (
  sales_order_id SERIAL NOT NULL PRIMARY KEY,
  created_at     TIMESTAMP DEFAULT now(),
  created_by     INTEGER REFERENCES users,
  customer_id    INTEGER REFERENCES customers,
  or_number      TEXT,
  reference_no   TEXT
);


CREATE TABLE items (
  item_id      SERIAL NOT NULL PRIMARY KEY,
  name         TEXT,
  description  TEXT,
  date_added   TIMESTAMP DEFAULT now(),
  date_updated TIMESTAMP DEFAULT now(),
  is_active    BOOL      DEFAULT TRUE
);

CREATE TABLE item (
  location_item_id SERIAL NOT NULL PRIMARY KEY,
  notes            TEXT,
  location_id      INTEGER REFERENCES locations,
  item_id          INTEGER REFERENCES items
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
  tax                    NUMERIC,
  tax_percentage         NUMERIC
);

CREATE TABLE sales_order_items (
  sales_order_item_id SERIAL NOT NULL PRIMARY KEY,
  quantity            NUMERIC,
  actual_unit_cost    NUMERIC,
  discount            NUMERIC,
  discount_percentage NUMERIC,
  tax                 NUMERIC,
  tax_percentage      NUMERIC,
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
  attribute_value TEXT,
  attribute_id    INTEGER REFERENCES attributes,
  item_id         INTEGER REFERENCES items,
  PRIMARY KEY (attribute_id, item_id)
);







CREATE TABLE item_variations (
  stock_on_hand     NUMERIC DEFAULT 0,
  unit_cost         NUMERIC,
  re_order_level    NUMERIC,
  re_order_quantity NUMERIC,
  is_active         BOOL,
  item_id           INTEGER REFERENCES items, -- parent item
  option_id         INTEGER REFERENCES items,
  PRIMARY KEY (item_id, option_id)
);


CREATE TABLE orders (
  order_id           SERIAL UNIQUE NOT NULL PRIMARY KEY,
  customer_id        INT REFERENCES customers,
  payment_id         INT,
  transaction_date   DATE,
  shipping_date      DATE,
  time_stamp         TIMESTAMP,
  transaction_status TEXT,
  total              NUMERIC
);



CREATE TABLE order_items (
  id         SERIAL PRIMARY KEY,
  order_id   INT REFERENCES orders,
  item_id    INT REFERENCES items,
  unit_price NUMERIC,
  discount   NUMERIC,
  quantity   INT
);

-- -------------------------------------
-- Cart Module
-- -------------------------------------

CREATE TABLE carts (
  id           INT PRIMARY KEY,
  session_id   INT,
  date_created DATE,
  customer_id  INT,
  is_active    BOOLEAN
);

CREATE TABLE cart_items (
  id         SERIAL PRIMARY KEY,
  cart_id    INT,
  item_id    INT,
  quantity   INT,
  time_stamp TIMESTAMP
);

CREATE TABLE wishlists (
  wishlist_id   SERIAL NOT NULL PRIMARY KEY,
  wishlist_name TEXT
);

CREATE TABLE wishlist_items (
  wishlist_item_id SERIAL NOT NULL PRIMARY KEY,
  wishlist_id      INT REFERENCES wishlists,
  item_id          INT REFERENCES items,
  time_stamp       TIMESTAMP
);

