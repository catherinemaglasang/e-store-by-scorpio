-- Stored procedures for inventory

-- Create table for products
create table products (
   product_id int primary key,
   title text,
   description text,
   date_added timestamp,
   ordering int,
   supplier_id int,
   category_id int,
   site_id int,
   product_type_id int,
   on_hand int,
   re_order_level int,
   is_active boolean
);

-- Function: Create new product
-- Sample: select * from get_products();
create or replace function new_product(in par_product_id int, in par_title text, in par_description text, in par_date_added TIMESTAMP, in par_ordering int, in par_supplier_id int, in par_category_id int, in par_site_id int, in par_product_type_id int, in par_on_hand int, in par_re_order_level int, in par_is_active boolean) returns text as
$$
  declare
    loc_product_id text;
    loc_res text;
  begin
     select into loc_product_id product_id from products where product_id = par_product_id;
     if loc_product_id isnull then
       insert into products(product_id, title, description, date_added, ordering, supplier_id, category_id, site_id, product_type_id, on_hand, re_order_level, is_active) values (par_product_id, par_title, par_description, par_date_added, par_ordering, par_supplier_id, par_category_id, par_site_id, par_product_type_id, par_on_hand, par_re_order_level, par_is_active);
       loc_res = 'ok';
     else
       loc_res = 'id exists';
     end if;
     return loc_res;
  end;
$$
 language 'plpgsql';

-- Create Sample Product
select new_product(100, 'title', 'description', '1999-01-08 04:05:06', 0, 1, 1, 1, 1, 100, 10, true);

-- Function: Get all product
create or replace function get_products(out int, out text, out text, out timestamp, out int, out int, out int, out int, out int, out int, out int, out boolean) returns setof record as
$$
  select * from products;
$$
 language 'sql';

-- Function: Get single product. Input: ID
-- Sample: select * from get_product_id(2);
create or replace function get_product_id(in par_product_id int, out int, out text, out text, out timestamp, out int, out int, out int, out int, out int, out int, out int, out boolean) returns setof record as
$$
   select product_id, title, description, date_added, ordering, supplier_id, category_id, site_id, product_type_id, on_hand, re_order_level, is_active from products where product_id = par_product_id;
$$
 language 'sql';

-- Function: Update single product. Input: ID
create or replace function update_product_id(in par_product_id int, in par_title text, in par_description text, in par_date_added TIMESTAMP, in par_ordering int, in par_supplier_id int, in par_category_id int, in par_site_id int, in par_product_type_id int, in par_on_hand int, in par_re_order_level int, in par_is_active boolean) returns text as
$$
  declare
    loc_product_id text;
    loc_res text;
  begin
     update products set
       title = COALESCE(par_title, title),
       description = COALESCE(par_description, description),
       date_added = COALESCE(par_date_added, date_added),
       ordering = COALESCE(par_ordering, ordering),
       supplier_id = COALESCE(par_supplier_id, supplier_id),
       category_id = COALESCE(par_category_id, category_id),
       site_id = COALESCE(par_site_id, site_id),
       product_type_id = COALESCE(par_product_type_id, product_type_id),
       on_hand = COALESCE(par_on_hand, on_hand),
       re_order_level = COALESCE(par_re_order_level, re_order_level),
       is_active = COALESCE(par_is_active, is_active)
     where product_id = par_product_id;

     loc_res = 'ok';
     return loc_res;
  end;
$$
 language 'plpgsql';


-- Modified Function
CREATE OR REPLACE FUNCTION add_product(par_product_id int, par_title text, par_description text, par_date_added TIMESTAMP, par_ordering int, par_supplier_id int, par_category_id int, par_site_id int, par_product_type_id int, par_on_hand int, par_re_order_level int, par_is_active boolean) returns void as $$
  BEGIN
    insert into products values(par_product_id, par_title, par_description, par_date_added, par_ordering, par_supplier_id, par_category_id, par_site_id, par_product_type_id, par_on_hand, par_re_order_level, par_is_active);
  END;
$$ LANGUAGE 'plpgsql';

create or replace function get_products() returns SETOF RECORD as $$
  BEGIN
    select * from products;
  END;
$$ language 'plpgsql';