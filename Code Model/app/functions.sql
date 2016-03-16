create or replace function new_product(in par_id int8, in par_sku text, in par_supplier_id int8, in par_title  text, in par_description text,in par_category_id int8, in par_unit_price float8, in par_on_hand int8, in par_re_order_level int8, in par_is_active boolean) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
     select into loc_id id from products where id = par_id;
     if loc_id isnull then

       insert into products(id, sku, supplier_id, title, description, category_id, unit_price, on_hand, re_order_level, is_active) values (par_id, par_sku, par_supplier_id, par_title, par_description, par_category_id, par_unit_price, par_on_hand, par_re_order_level, par_is_active);
       loc_res = 'OK';

     else
       loc_res = 'ID EXISTED';
     end if;
     return loc_res;
  end;
$$
 language 'plpgsql';


create or replace function get_product(out int8, out text, out int8, out text, out text, out int8, out float8, out int8, out int8, out boolean) returns setof record as
$$
   select id, sku, supplier_id, title, description, category_id, unit_price, on_hand, re_order_level, is_active from products;

$$
 language 'sql';

--select * from get_products();

create or replace function get_product_id(in par_id int8, out text, out int8, out text, out text, out int8, out float8, out int8, out int8, out boolean) returns setof record as
$$
   select sku, supplier_id, title, description, category_id, unit_price, on_hand, re_order_level, is_active from products where id = par_id;

$$
 language 'sql';

--select * from get_product_id(2);

create or replace function new_user(in par_id int8, in par_username text, in par_password text, in par_is_admin boolean) returns text as
$$
declare
  loc_id text;
  loc_username text;
  loc_passwrod text;
  loc_is_admin boolean;
  loc_res text;
begin
  select into loc_id id from users where id = par_id;
  if loc_id isnull then
    insert into users(id, username, password, is_admin) values (par_id, par_username, par_password, par_is_admin);
    loc_res = 'OK';
  else
    loc_res = 'USER EXISTS';
  end if;
  return loc_res;
  end;
$$
language 'plpgsql';

--select new_user(1, 'roselle', 'roselle', true);

create or replace function new_user(par_id int8, par_username text, par_password text, par_is_admin boolean) returns text as
$$
  declare
    loc_id text;
    loc_username text;
    loc_passwrod text;
    loc_is_admin boolean;
    loc_res text;
  begin
    select into loc_id id from users where id = par_id;
    if loc_id isnull then
      insert into users(id, username, password, is_admin) values (par_id, par_username, par_password, par_is_admin);
      loc_res = 'OK';
    else
      loc_res = 'USER EXISTS';
    end if;
    return loc_res;
    end;
$$
  language 'plpgsql';

--select new_user(1, 'roselle', 'roselle', true);

create or replace function get_users(out int8, out text, out text, out boolean) returns setof record as
$$
   select id, username, password, is_admin from users;
$$
 language 'sql';

--select * from get_users();

create or replace function get_user(in par_id int8, out text, out text, out boolean) returns setof record as
$$
  select username, password, is_admin from users where id = par_id
$$
  language 'sql';


--select * from get_user(1);

create or replace function new_supplier(in par_id int8, in par_name text, in par_address text, in par_phone text, in par_fax text,in par_email text, in par_is_active boolean) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
     select into loc_id id from suppliers where id = par_id;
     if loc_id isnull then

       insert into suppliers(id, name, address, phone, fax, email, is_active) values (par_id, par_name, par_address, par_phone, par_fax, par_email, par_is_active);
       loc_res = 'OK';

     else
       loc_res = 'ID EXISTED';
     end if;
     return loc_res;
  end;
$$
 language 'plpgsql';

create or replace function get_suppliers(out int8, out text, out text, out text, out text, out text, out boolean) returns setof record as
$$
   select id, name, address, phone, fax, email, is_active from suppliers;
$$
 language 'sql';


create or replace function get_supplier(in par_id int8, out text, out text, out text, out text, out text, out boolean) returns setof record as
$$
 select  name, address, phone, fax, email, is_active from suppliers where id = par_id
$$
 language 'sql';

create or replace function new_cart(in par_id int8, in par_session_id int8, in par_date_created DATE, in par_customer_id int8, in par_is_active boolean) returns text as
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
       loc_res = 'ID EXISTED';
     end if;
     return loc_res;
  end;
$$
 language 'plpgsql';

create or replace function get_carts(out int8, out int8, out DATE, out int8, out boolean) returns setof record as
$$
   select id, session_id, date_created, customer_id, is_active from carts;
$$
 language 'sql';

create or replace function get_cart(in par_id int8, out int8, out DATE, out int8, out boolean) returns setof record as
$$
   select session_id, date_created, customer_id, is_active from carts where id = par_id;

$$
 language 'sql';


create or replace function new_category(in par_id int8, in par_name text, in par_description text,  in par_main_image bytea, in par_parent_category_id int8, in par_is_active boolean) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
    select into loc_id id from categories where id=par_id;
    if loc_id isnull then

       insert into categories(id, name, description, main_image, parent_category_id, is_active) values (par_id, par_name, par_description, par_main_image, par_parent_category_id, par_is_active);
       loc_res = 'OK';

     else
       loc_res = 'ID EXISTED';
     end if;
     return loc_res;
  end;
$$  

language 'plpgsql';


create or replace function new_cart_detail(in par_id int8, in par_cart_id int8, in par_product_id int8, in par_quantity int8, in par_time_stamp timestamp) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
    select into loc_id id from cart_detail where id=par_id;
    if loc_id isnull then

       insert into cart_details(id, cart_id, product_id, quantity, time_stamp) values (par_id, par_cart_id, par_product_id, par_quantity, par_time_stamp);
       loc_res = 'OK';

     else
       loc_res = 'ID EXISTED';
     end if;
     return loc_res;
  end;
$$  

language 'plpgsql';


create or replace function get_cart_details(out int8, out int8, out int8, out int8, out timestamp) returns setof record as
$$
   select id, cart_id, product_id, quantity, time_stamp from cart_details;
$$
 language 'sql';


create or replace function get_cart_detail(in par_id int8, out int8, out int8, out int8, out timestamp) returns setof record as
$$
  select cart_id, product_id, quantity, time_stamp from cart_details where id = par_id;
$$
  language 'sql';


create or replace function new_wishlist_detail(in par_id int8, in par_wishlist_id int8, in par_product_id int8, in par_time_stamp timestamp) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
    select into loc_id id from cart_detail where id=par_id;
    if loc_id isnull then

       insert into cart_details(id, wishlist_id, product_id, time_stamp) values (par_id, par_wishlist_id, par_product_id, par_time_stamp);
       loc_res = 'OK';

     else
       loc_res = 'ID EXISTED';
     end if;
     return loc_res;
  end;
$$  

language 'plpgsql';


create or replace function get_wishlist_details(out int8, out int8, out int8, out timestamp) returns setof record as
$$
   select id, wishlist_id, product_id, time_stamp from wishlist_details;
$$
 language 'sql';
 

create or replace function get_wishlist_detail(in par_id int8, out int8, out int8, out timestamp) returns setof record as
$$
  select wishlist_id, product_id, time_stamp from wishlist_details where id = par_id;
$$
  language 'sql';


create or replace function new_wishlist(in par_id int8) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
    select into loc_id id from cart where id=par_id;
    if loc_id isnull then

       insert into cart(id) values (par_id);
       loc_res = 'OK';

     else
       loc_res = 'ID EXISTED';
     end if;
     return loc_res;
  end;
$$  

language 'plpgsql';



create or replace function new_orders(in par_id int8, in par_customer_id int8, in par_payment_id int8, in par_transaction_date date, in par_shipping_date date, in par_time_stamp timestamp, in par_transaction_status text, par_total float8) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
    select into loc_id id from orders where id=par_id;
    if loc_id isnull then

       insert into orders(id, customer_id, payment_id, transaction_date, shipping_date, time_stamp, transaction_status, total) values (par_id, par_customer_id, par_payment_id, par_transaction_date, par_shipping_date, par_time_stamp, par_transaction_status, par_total);
       loc_res = 'OK';

     else
       loc_res = 'ID EXISTED';
     end if;
     return loc_res;
  end;
$$

language 'plpgsql';

create or replace function get_orders(out int8, out int8, out int8, out date, out date, out timestamp, out text, out float8) returns setof record as
$$
  select id, customer_id, payment_id, transaction_date, shipping_date, time_stamp, transaction_status, total from orders
$$

language 'sql';

create or replace function get_order_id(in par_id int8, out int8, out int8, out date, out date, out timestamp, out text, out float8) returns setof record as
$$
   select customer_id, payment_id, transaction_date, shipping_date, time_stamp, transaction_status, total from orders where id = par_id;

$$
 language 'sql';


create or replace function new_order_details(in par_id int8, in par_order_id int8, in par_product_id int8, in par_unit_price float8, in par_discount float8, in par_quantity int8) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
    select into loc_id id from orders where id=par_id;
    if loc_id isnull then

       insert into orders(id, order_id, product_id, unit_price, discount, quantity) values (par_id, par_order_id, par_product_id, par_unit_price, par_discount, par_quantity);
       loc_res = 'OK';

     else
       loc_res = 'ID EXISTED';
     end if;
     return loc_res;
  end;
$$

language 'plpgsql';

create or replace function get_order_details(out int8, out int8, out int8, out float8, out float8, out int8) returns setof record as
$$
  select id, order_id, product_id, unit_price, discount, quantity from order_details
$$

language 'sql';

create or replace function get_order_details_id(in par_id int8, out int8, out int8, out float8, out float8, out int8) returns setof record as
$$
   select order_id, product_id, unit_price, discount, quantity from order_details where id = par_id;

$$
 language 'sql';
