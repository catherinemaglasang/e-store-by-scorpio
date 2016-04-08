create or replace function new_user(in par_id int, in par_username text, in par_password text, in par_email text, in par_is_admin boolean) returns text as
$$
declare
  loc_id text;
  loc_res text;
begin
  select into loc_id user_id from users where user_id = par_id;
  if loc_id isnull then
    if par_username='' or par_password='' or par_email='' then
      loc_res='error';
    else
      insert into users(user_id, username, password, email, is_admin) values (par_id, par_username, par_password, par_email, par_is_admin);
      loc_res = 'OK';
    end if;

  else
    loc_res = 'USER EXISTS';
  end if;
  return loc_res;
  end;
$$
language 'plpgsql';

create or replace function get_users(out int, out text, out text, out boolean) returns setof record as
$$
   select user_id, username, email, is_admin from users;
$$
 language 'sql';

--select * from get_users();

create or replace function get_user(in par_id int, out text, out text, out boolean) returns setof record as
$$
  select username, email, is_admin from users where user_id = par_id
$$
  language 'sql';


--select * from get_user(1);

create or replace function new_supplier(in par_id int, in par_name text, in par_address text, in par_phone text, in par_fax text,in par_email text, in par_is_active boolean) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
     select into loc_id name from suppliers where name = par_name;
     if loc_id isnull then
       if par_name='' or par_address='' or par_phone='' or par_fax='' or par_email='' then
         loc_res='error';
       else
         insert into suppliers(name, address, phone, fax, email, is_active) values (par_name, par_address, par_phone, par_fax, par_email, par_is_active);
         loc_res = 'OK';
       end if;

     else
       loc_res = 'SUPPLIER EXISTS';
     end if;
     return loc_res;
  end;
$$
 language 'plpgsql';

create or replace function get_suppliers(out int, out text, out text, out text, out text, out text, out boolean) returns setof record as
$$
   select supplier_id, name, address, phone, fax, email, is_active from suppliers;
$$
 language 'sql';


create or replace function get_supplier(in par_id int, out text, out text, out text, out text, out text, out boolean) returns setof record as
$$
 select  name, address, phone, fax, email, is_active from suppliers where supplier_id = par_id;
$$
 language 'sql';

create or replace function new_cart(in par_id int, in par_session_id int, in par_date_created DATE, in par_customer_id int, in par_is_active boolean) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
     select into loc_id id from carts where id = par_id;
     if loc_id isnull then

       insert into carts(id, session_id, date_created, customer_id, is_active) values (par_id, par_session_id, par_date_created, par_customer_id, par_is_active);
       loc_res = 'OK';

     else
       loc_res = 'ID EXISTS';
     end if;
     return loc_res;
  end;
$$
 language 'plpgsql';

create or replace function get_carts(out int, out int, out DATE, out int, out boolean) returns setof record as
$$
   select id, session_id, date_created, customer_id, is_active from carts;
$$
 language 'sql';

create or replace function get_cart(in par_id int, out int, out DATE, out int, out boolean) returns setof record as
$$
   select session_id, date_created, customer_id, is_active from carts where id = par_id;

$$
 language 'sql';


create or replace function new_cart_item(in par_id int, in par_cart_id int, in par_item_id int, in par_quantity int, in par_time_stamp timestamp) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
    select into loc_id id from cart_items where id=par_id;
    if loc_id isnull then

       insert into cart_items(id, cart_id, item_id, quantity, time_stamp) values (par_id, par_cart_id, par_item_id, par_quantity, par_time_stamp);
       loc_res = 'OK';

     else
       loc_res = 'ID EXISTS';
     end if;
     return loc_res;
  end;
$$  

language 'plpgsql';


create or replace function get_cart_items(out int, out int, out int, out int, out timestamp) returns setof record as
$$
   select id, cart_id, item_id, quantity, time_stamp from cart_items;
$$
 language 'sql';


create or replace function get_cart_item(in par_id int, out int, out int, out int, out timestamp) returns setof record as
$$
  select cart_id, item_id, quantity, time_stamp from cart_items where id = par_id;
$$
  language 'sql';


create or replace function new_wishlist_item(in par_id int, in par_wishlist_id int, in par_item_id int, in par_time_stamp timestamp) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
    select into loc_id wishlist_item_id from wishlist_items where wishlist_item_id=par_id;
    if loc_id isnull then

       insert into wishlist_items(wishlist_item_id, wishlist_id, item_id, time_stamp) values (par_id, par_wishlist_id, par_item_id, par_time_stamp);
       loc_res = 'OK';

     else
       loc_res = 'ID EXISTED';
     end if;
     return loc_res;
  end;
$$  

language 'plpgsql';


create or replace function get_wishlist_items(out int, out int, out int, out timestamp) returns setof record as
$$
   select wishlist_item_id, wishlist_id, item_id, time_stamp from wishlist_items;
$$
 language 'sql';
 

create or replace function get_wishlist_item(in par_id int, out int, out int, out timestamp) returns setof record as
$$
  select wishlist_id, item_id, time_stamp from wishlist_items where wishlist_item_id = par_id;
$$
  language 'sql';


create or replace function new_wishlist(in par_id int, in par_wishlist_name text) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
    select into loc_id wishlist_id from wishlists where wishlist_id=par_id;
    if loc_id isnull then

       insert into wishlists(wishlist_name) values (par_wishlist_name);
       loc_res = 'OK';

     else
       loc_res = 'ID EXISTED';
     end if;
     return loc_res;
  end;
$$

language 'plpgsql';
-- create or replace function new_wishlist(in par_id int8) returns text as
-- $$
--   declare
--     loc_id text;
--     loc_res text;
--   begin
--     select into loc_id id from wishlist where id=par_id;
--     if loc_id isnull then

--        insert into wishlist(id) values (par_id);
--        loc_res = 'OK';

--      else
--        loc_res = 'ID EXISTED';
--      end if;
--      return loc_res;
--   end;
-- $$  

-- language 'plpgsql';


create or replace function get_wishlists(out int, out text) returns setof record as
$$
  select wishlist_id, wishlist_name from wishlists;
$$
language 'sql';


create or replace function get_wishlist(in par_id int, out int, out text) returns setof record as
$$
  select wishlist_id, wishlist_name from wishlists where wishlist_id = par_id;
$$
  language 'sql';

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
<<<<<<< HEAD
      els
          insert into orders(id, customer_id, payment_id, transaction_date, shipping_date, time_stamp, transaction_status, total) values (par_id, par_customer_id, par_payment_id, par_transaction_date, par_shipping_date, par_time_stamp, par_transaction_status, par_total);
=======
      else
          insert into orders(order_id, customer_id, payment_id, transaction_date, shipping_date, time_stamp, transaction_status, total) values (par_id, par_customer_id, par_payment_id, par_transaction_date, par_shipping_date, par_time_stamp, par_transaction_status, par_total);
>>>>>>> 2d2bb11e79d9802473cec82abaaa92a12f4b11a3
          loc_res = 'OK';
      end if;
     else
       loc_res = 'ID EXISTS';
     end if;
     return loc_res;
  end;
$$

language 'plpgsql';

create or replace function get_orders(out int, out int, out int, out date, out date, out timestamp, out text, out numeric) returns setof record as
$$
  select order_id, customer_id, payment_id, transaction_date, shipping_date, time_stamp, transaction_status, total from orders
$$

language 'sql';

create or replace function get_order_id(in par_id int, out int, out int, out date, out date, out timestamp, out text, out numeric) returns setof record as
$$
   select customer_id, payment_id, transaction_date, shipping_date, time_stamp, transaction_status, total from orders where order_id = par_id;

$$
 language 'sql';



create or replace function new_order_item(in par_id int, in par_order_id int, in par_item_id int, in par_unit_price float8, in par_discount float8, in par_quantity int) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
    select into loc_id id from order_items where id=par_id;
    if loc_id isnull then
       if par_item_id isnull or par_id isnull or par_order_id isnull or par_unit_price isnull or par_discount isnull or par_quantity isnull then
         loc_res='error';
       else
         insert into order_items(id, order_id, item_id, unit_price, discount, quantity) values (par_id, par_order_id, par_item_id, par_unit_price, par_discount, par_quantity);
         loc_res = 'OK';
       end if;
     else
       loc_res = 'ID EXISTS';
     end if;
     return loc_res;
  end;
$$

language 'plpgsql';


  create or replace function get_order_items(out int, out int, out int, out numeric, out numeric, out int) returns setof record as
  $$
    select id, order_id, item_id, unit_price, discount, quantity from order_items
  $$

  language 'sql';

create or replace function get_order_item_id(in par_id int, out int, out int, out numeric, out numeric, out int) returns setof record as
$$
   select order_id, item_id, unit_price, discount, quantity from order_items where id = par_id;

$$
 language 'sql';

create or replace function new_customer(in par_id int, in par_first_name text, in par_last_name text, in par_address text, in par_city text, in par_state text, in par_postal_code text, in par_country text, in par_phone text, in par_email text, in par_user_id int, in par_billing_address text, in par_shipping_address text, in par_date_created timestamp) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
    select into loc_id id from customers where id=par_id;
    if loc_id isnull then
      if par_first_name='' or par_last_name='' or par_address='' or par_city='' or par_state='' or par_postal_code='' or par_country='' or par_phone='' or par_email='' or par_billing_address='' or par_shipping_address='' then
        loc_res='error';
      else
        insert into customers(id, first_name, last_name, address, city, state, postal_code, country, phone, email, user_id, billing_address, shipping_address, date_created) values (par_id, par_first_name, par_last_name, par_address, par_city, par_state, par_postal_code, par_country, par_phone, par_email, par_user_id, par_billing_address, par_shipping_address, par_date_created);
        loc_res = 'ok';
      end if;
    else
      loc_res = 'CUSTOMER EXISTS';
    end if;
    return loc_res;
  end;
$$

language 'plpgsql';

create or replace function get_all_customers(out int, out text, out text, out text, out text, out text, out text, out text, out text, out text, out int, out text, out text, out timestamp) returns setof record as
$$
  select id, first_name, last_name, address, city, state, postal_code, country, phone, email, user_id, billing_address, shipping_address, date_created from customers
$$
  language 'sql';

create or replace function get_single_customer(in par_id int, out text, out text, out text, out text, out text, out text, out text, out text, out text, out int, out text, out text, out timestamp) returns setof record as
$$
  select first_name, last_name, address, city, state, postal_code, country, phone, email, user_id, billing_address, shipping_address, date_created from customers where id = par_id
$$
  language 'sql';