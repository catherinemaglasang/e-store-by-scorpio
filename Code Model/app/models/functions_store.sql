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


CREATE OR REPLACE FUNCTION new_wishlist_item(IN par_id         INT, IN par_wishlist_id INT, IN par_item_id INT,
                                             IN par_time_stamp TIMESTAMP)
  RETURNS TEXT AS
$$
DECLARE
  loc_id  TEXT;
  loc_res TEXT;
BEGIN
  SELECT INTO loc_id wishlist_item_id
  FROM wishlist_items
  WHERE wishlist_item_id = par_id;
  IF loc_id ISNULL
  THEN
    IF par_wishlist_item_id = '' OR par_wishlist_id = '' OR par_item_id = '' OR par_time_stamp = ''
    THEN
      loc_res='error';
    ELSE
      INSERT INTO wishlist_items (wishlist_item_id, wishlist_id, item_id, time_stamp) VALUES (par_id, par_wishlist_id, par_item_id, par_time_stamp);
      loc_res = 'OK';
    END IF;

  ELSE
    loc_res = 'WISHLIST ITEM EXISTED';
  END IF;
  RETURN loc_res;
END;
$$

LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION get_wishlist_items(OUT INT, OUT INT, OUT INT, OUT TIMESTAMP)
  RETURNS SETOF RECORD AS
$$
SELECT
  wishlist_item_id,
  wishlist_id,
  item_id,
  time_stamp
FROM wishlist_items;
$$
LANGUAGE 'sql';


CREATE OR REPLACE FUNCTION get_wishlist_item(IN par_id INT, OUT INT, OUT INT, OUT INT, OUT TIMESTAMP)
  RETURNS SETOF RECORD AS
$$
SELECT
  wishlist_item_id,
  wishlist_id,
  item_id,
  time_stamp
FROM wishlist_items
WHERE wishlist_item_id = par_id;
$$
LANGUAGE 'sql';


CREATE OR REPLACE FUNCTION new_wishlist(IN par_id INT, IN par_wishlist_name TEXT)
  RETURNS TEXT AS
$$
DECLARE
  loc_id  TEXT;
  loc_res TEXT;
BEGIN
  SELECT INTO loc_id wishlist_id
  FROM wishlists
  WHERE wishlist_id = par_id;
  IF loc_id ISNULL
  THEN
    IF par_id ISNULL OR par_wishlist_name = '' 
    THEN
      loc_res='error';
    ELSE
      INSERT INTO wishlists (wishlist_id, wishlist_name) VALUES (par_id, par_wishlist_name);
      loc_res = 'OK';
    END IF;

  ELSE
    loc_res = 'ERROR';
  END IF;
  RETURN loc_res;
END;
$$
LANGUAGE 'plpgsql';



-- CREATE OR REPLACE FUNCTION new_wishlist(IN par_id INT, IN par_wishlist_name TEXT)
--   RETURNS TEXT AS
-- $$
-- DECLARE
--   loc_id  TEXT;
--   loc_res TEXT;
-- BEGIN
--   SELECT INTO loc_id wishlist_id
--   FROM wishlists
--   WHERE loc_id = par_id;
--   IF loc_id ISNULL
--   THEN

--     INSERT INTO wishlists (wishlist_name) VALUES (par_wishlist_name);
--     loc_res = 'OK';

--   ELSE
--     loc_res = 'ID EXISTED';
--   END IF;
--   RETURN loc_res;
-- END;
-- $$
-- LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION get_wishlists(OUT INT, OUT TEXT)
  RETURNS SETOF RECORD AS
$$
SELECT
  wishlist_id,
  wishlist_name
FROM wishlists;
$$
LANGUAGE 'sql';


CREATE OR REPLACE FUNCTION get_wishlist(IN par_id INT, OUT INT, OUT TEXT)
  RETURNS SETOF RECORD AS
$$
SELECT * FROM wishlists WHERE wishlist_id = par_id;
$$
LANGUAGE 'sql';


-- create or replace function new_order(in par_id int, in par_customer_id int, in par_payment_id int, in par_transaction_date date, in par_shipping_date date, in par_time_stamp timestamp, in par_transaction_status text, par_total numeric) returns text as
-- $$
--   declare
--     loc_id text;
--     loc_res text;
--   begin
--     select into loc_id order_id from orders where order_id=par_id;
--     if loc_id isnull then
--       if par_transaction_status='' or par_id isnull or par_customer_id isnull or par_payment_id isnull or par_total isnull then
--           loc_res='error';
--       else
--           insert into orders(order_id, customer_id, payment_id, transaction_date, shipping_date, time_stamp, transaction_status, total) values (par_id, par_customer_id, par_payment_id, par_transaction_date, par_shipping_date, par_time_stamp, par_transaction_status, par_total);
--           loc_res = 'OK';
--       end if;
--      else
--        loc_res = 'ID EXISTS';
--      end if;
--      return loc_res;
--   end;
-- $$
-- LANGUAGE 'plpgsql';


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