  create table products (
     id int8 primary key,
     sku text,
     supplier_id int8,
     title text,
     description text,
     category_id int8,
     unit_price float8,
     on_hand int8,
     re_order_level int8,
     is_active boolean
  );

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
  create table users (
     id int8 primary key,
     username text,
     password text,
     is_admin boolean
  );

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

create or replace function get_user(in par_id int8, out text, out text, out boolean) returns setof record as
$$
  select username, password, is_admin from users where id = par_id
$$
  language 'sql';

  --select * from get_user(1);
