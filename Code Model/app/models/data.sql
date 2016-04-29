select items_upsert(null, 'default', 'default', '2016-04-05 23:02:58', '2016-04-05 23:02:58', true);

select option_groups_upsert(null, 'default');

select options_upsert(null, 1, 'default');

select locations_upsert(null, 'default');

select attributes_upsert(null, 'default', 'default');

-- select suppliers_upsert(null, 'default', null, null, null, null, true);

select new_customer(1, 'default', 'default', 'default', 'default', 'default', '9200', 'PH', 'default', 'default', 1, 'default', 'default', '1/1/1 1:1:1');

-- select new_order(1, 1, 1, '1/1/1', '1/1/1', '1/1/1 1:1:1', 'open', 100);

select wishlists_upsert(1, 'default');
