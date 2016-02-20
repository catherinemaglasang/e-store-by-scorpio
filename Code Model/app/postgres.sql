create table tasks (
   id int8 primary key,
   title text,
   description text,
   done boolean
);

create or replace function newtask(par_id int8, par_title  text, par_description text, par_done boolean) returns text as
$$
  declare
    loc_id text;
    loc_res text;
  begin
     select into loc_id id from tasks where id = par_id;
     if loc_id isnull then

       insert into tasks (id, title, description, done) values (par_id, par_title, par_description, par_done);
       loc_res = 'OK';

     else
       loc_res = 'ID EXISTED';  
     end if;
     return loc_res;
  end;
$$
 language 'plpgsql';

--select newtask(1, 'Buy Groceries','Milk, Cheese, Pizza, Fruit, Tylenol', false); 
--select newtask(2, 'Learn Python','Need to find a good Python tutorial on the web', false); 

create or replace function gettasks(out int8, out text, out text, out boolean) returns setof record as
$$
   select id, title, description, done from tasks;

$$
 language 'sql';
 
--select * from gettasks();

create or replace function gettaskid(in par_id int8, out text, out text, out boolean) returns setof record as
$$
   select title, description, done from tasks where id = par_id;

$$
 language 'sql';
 
--select * from gettaskid(2);

