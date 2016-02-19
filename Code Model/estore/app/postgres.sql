create table products (
    id int8 primary key,
    title text,
    description text,
    unit_price float8,
    is_active boolean
);


create or replace function newproduct(par_id int8, par_title  text, par_description text, par_unit_price float8, par_is_active boolean) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
     select into loc_id id from products where id = par_id;
     if loc_id isnull then

       insert into products (id, title, description, unit_price, is_active) values (par_id, par_title, par_description, par_unit_price, par_is_active);
       loc_res = 'OK';

     else
       loc_res = 'ID EXISTED';
     end if;
     return loc_res;
  end;
$$

language 'plpgsql';

--select newproduct(1, 'Guitar','Bass',2000, false);
--select newproduct(2, 'Amplifier','Bass Amp',3000, false);

create or replace function getproducts(out int8, out text, out text,out float8, out boolean) returns setof record as
$$
   select id, title, description, unit_price, is_active from products;

$$

language 'sql';

--select * from getproducts();

create or replace function getproductid(in par_id int8, out text, out text, out float8, out boolean) returns setof record as
$$
   select title, description, unit_price, is_active from products where id = par_id;

$$
 language 'sql';

--select * from getproductid(2);
