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

--select new_product(1, '0111AB',, 11, 'Webster', 'Dictionary', '0111', 999.99, 20, 10, false);
--select new_product(2, '0222AB', 22, 'Python', 'Learning Python', '0222', 1500.00, 20, 10, false);

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

create or replace function new_supplier(in par_id int8, in par_name text, in par_address text, in par_phone text, in par_fax text, in par_is_active boolean) returns text as
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
 language 'sql';s

create or replace function new_cart(in par_id int8, in par_session_id int8, in par_date_created text, in par_customer_id int8, in par_is_active boolean) returns text as
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

create or replace function get_carts(out int8, out int8, out text, out int8, out boolean) returns setof record as
$$
   select id, session_id, date_created, customer_id, is_active from carts;
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