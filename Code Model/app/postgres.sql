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
