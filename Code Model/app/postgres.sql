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

create or replace function new_product(par_id int8, par_sku text, par_supplier_id int8, par_title  text, par_description text, par_category_id int8, par_unit_price float8, par_on_hand int8, par_re_order_level int8, par_is_active boolean) returns text as
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

