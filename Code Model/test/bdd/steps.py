import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import create_app


@before.all
def before_all():
    app = create_app()
    world.app = app.test_client()


""" Create cart item sunny case and rainy case """


@step("I have the following cart item details")
def given_I_have_th_following_cart_item_details(step):
    """
    :type step: lettuce.core.Step
    """
    world.cartItem1 = step.hashes[0]


@step("I Post the cart item to resource_url  '/api/v1/cart_items/'")
def when_I_Post_the_cart_item_to_resource_url(step):
    """
    :type step: lettuce.core.Step
    """
    world.cartItem_post_uri = '/api/v1/cart_items/'
    world.cartItem_post_response = world.app.post(world.cartItem_post_uri, data=json.dumps(world.cartItem1))


@step("I should get response \'(.*)\'")
def then_I_should_get_response(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.cartItem_post_response.status_code, int(expected_status_code))


@step('I should get "status" \'(.*)\'')
def and_I_should_get_status(step, status):
    """
    :type step: lettuce.core.Step
    """
    world.cartItem_post_response_json = json.loads(world.cartItem_post_response.data)
    assert_equals(world.cartItem_post_response_json['status'], status)


@step('I should get "message" \'(.*)\'')
def and_I_should_get_message(step, message):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.cartItem_post_response_json['message'], message)


""" Get Cart Item sunny case """


@step("cart item \'(.*)\' is in the system")
def given_cart_item1_is_in_the_system(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.cart_item = world.app.get('/api/v1/cart_items/{}/'.format(id))
    world.resp = json.loads(world.cart_item.data)
    assert_equals(world.resp['status'], 'ok')


@step("I retrieve the cart item \'(.*)\'")
def when_I_retrieve_the_cart_item1(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/cart_items/{}/'.format(id))


@step("the following cart item details are returned:")
def then_the_following_cart_item_details_are_returned(step):
    """
    :type step: lettuce.core.Step
    """
    resp = json.loads(world.response.data)
    assert_equals(world.resp['entries'], resp['entries'])


""" Get Cart Item rainy case """


@step("I retrieve a cart item with resource url \'(.*)\'")
def given_I_retrieve_a_cart_item_with_resource_url(step, url):
    """
    :param url:
    :type step: lettuce.core.Step
    """
    world.cart_item_uri = url


@step("i retrieve JSON result")
def when_i_retrieve_JSON_result(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(world.cart_item_uri)


@step('it should have a field "count" 0')
def and_it_should_have_an_empty_field_count0(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.resp['count'], '0')


@step('it should have an empty field " entries "')
def and_it_should_have_an_empty_field_entries(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp['entries']), 0)


@step('I should get a message containing \'(.*)\'')
def and_it_should_get_a_message_No_entries_found(step, message):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['message'], message)

""" Create Cart sunny case and rainy case """


@step("I have the following cart details")
def given_I_have_the_following_cart_details(step):
    """
    :type step: lettuce.core.Step
    """
    world.cart1 = step.hashes[0]


@step("I Post the cart to resource_url  '/api/v1/carts/'")
def when_I_Post_the_cart_to_resource_url(step):
    """
    :type step: lettuce.core.Step
    """
    world.cart_post_uri = '/api/v1/carts/'
    world.cart_post_response = world.app.post(world.cart_post_uri, data=json.dumps(world.cart1))


@step("I should have a status code response \'(.*)\'")
def then_I_should_have_a_status_code_response(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.cart_post_response.status_code, int(expected_status_code))


@step("I should get a status \'(.*)\'")
def and_I_should_get_a_status_ok(step, status):
    """
    :type step: lettuce.core.Step
    """
    world.cart_post_response_json = json.loads(world.cart_post_response.data)
    assert_equals(world.cart_post_response_json['status'], status)


@step("I should get a message \'(.*)\'")
def and_I_should_get_a_message_ok(step, message):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.cart_post_response_json['message'], message)



""" Get Cart sunny case """


@step("cart \'(.*)\' is in the system")
def given_cart_is_in_the_system(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.cart = world.app.get('/api/v1/carts/{}/'.format(id))
    world.resp = json.loads(world.cart.data)
    assert_equals(world.resp['status'], 'ok')


@step("I retrieve the cart \'(.*)\'")
def when_I_retrieve_the_cart(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/carts/{}/'.format(id))


@step("the following details are returned :")
def and_the_following_details_are_returned(step):
    """
    :type step: lettuce.core.Step
    """
    resp = json.loads(world.response.data)
    assert_equals(world.resp['entries'], resp['entries'])


""" Get Cart rainy case """


@step("I retrieve a cart with resource url \'(.*)\'")
def given_I_retrieve_a_cart_with_resource_url(step, url):
    """
    :param url:
    :type step: lettuce.core.Step
    """
    world.cart_uri = url


@step("i retrieve a JSON result")
def when_i_retrieve_a_JSON_result(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(world.cart_uri)


@step('it should  have a field "count" 0')
def and_it_should_have_a_field_count0(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.resp['count'], '0')


@step('it should  have a field "message" \'(.*)\'')
def and_it_should_have_a_field_message_no_entries(step, message):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['message'], message)


@step('it should  have an empty field " entries "')
def and_it_should_have_an_empty_field_entries(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp['entries']), 0)



""" Create new order sunny case and rainy case"""


@step("I have the following order details")
def given_I_have_the_following_order_details(step):
    """
    :type step: lettuce.core.Step
    """
    world.order1 = step.hashes[0]


@step("I Post the order to resource_url  '/api/v1/orders/'")
def when_I_Post_the_order_to_resource_url(step):
    """
    :type step: lettuce.core.Step
    """
    world.order_post_uri = '/api/v1/orders/'
    world.order_post_response = world.app.post(world.order_post_uri, data=json.dumps(world.order1))


@step("I should get a status of \'(.*)\'")
def then_I_should_get_a_status_of(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.order_post_response.status_code, int(expected_status_code))


@step('I should get a "status" \'(.*)\'')
def and_I_should_get_a_status(step, status):
    """
    :type step: lettuce.core.Step
    """
    world.order_post_response_json = json.loads(world.order_post_response.data)
    assert_equals(world.order_post_response_json['status'], status)


@step('I should get a "message" \'(.*)\'')
def and_I_should_get_a_message(step, message):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.order_post_response.data)
    assert_equals(world.resp['message'], message)


"""Get Order ID sunny case """


@step("Order id \'(.*)\' is in the system")
def given_order_id1_is_in_the_system(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.order = world.app.get('/api/v1/orders/{}/'.format(id))
    world.resp = json.loads(world.order.data)
    assert_equals(world.resp['status'], 'ok')


@step("I retrieve the order \'(.*)\'")
def when_I_retrieve_the_order(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/orders/{}/'.format(id))


@step("the following orders are returned:")
def and_the_following_orders_are_returned(step):
    """
    :type step: lettuce.core.Step
    """
    resp = json.loads(world.response.data)
    assert_equals(world.resp['entries'], resp['entries'])


""" Get order ID rainy case """


@step("I retrieve an order with resource url \'(.*)\'")
def given_I_retrieve_an_order_with_resource_url(step, url):
    """
    :param url:
    :type step: lettuce.core.Step
    """
    world.order_uri = url


@step("I retrieve a  JSON result")
def when_I_retrieve_a_JSON_result(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(world.order_uri)


@step('It should  have a "message" "No entries found"')
def and_It_should_have_a_message_No_entries_found(step):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['message'], 'No entries found')


@step('It should  have a field "count" 0')
def and_It_should_have_a_field_count0(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.resp['count'], '0')


@step('It should  have an empty field " entries "')
def and_It_should_have_an_empty_field_entries(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp['entries']), 0)



""" Create order item sunny and rainy case """


@step("I have the following order item details")
def given_I_have_the_following_order_item_details(step):
    """
    :type step: lettuce.core.Step
    """
    world.order1 = step.hashes[0]


@step("I Post the order item to resource_url  '/api/v1/order_items/'")
def when_I_Post_the_order_item_to_resource_url(step):
    """
    :type step: lettuce.core.Step
    """
    world.order_post_uri = '/api/v1/order_items/'
    world.order_post_response = world.app.post(world.order_post_uri, data=json.dumps(world.order1))


@step("I should have a response \'(.*)\'")
def then_I_should_have_a_status(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.order_post_response.status_code, int(expected_status_code))


@step('I should have a "status" containing \'(.*)\'')
def and_I_should_have_a_status_containing_ok(step, status):
    """
    :type step: lettuce.core.Step
    """
    world.order_post_response_json = json.loads(world.order_post_response.data)
    assert_equals(world.order_post_response_json['status'], status)


@step('I should have a "message" containing \'(.*)\'')
def and_I_should_have_a_message_containing_ok(step, message):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.order_post_response_json['message'], message)


""" Get order item sunny case """


@step("order item id \'(.*)\' is in the system")
def given_order_item_id1_is_in_the_system(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.order = world.app.get('/api/v1/order_items/{}/'.format(id))
    world.resp = json.loads(world.order.data)
    assert_equals(world.resp['status'], 'ok')


@step("I retrieve the order item \'(.*)\'")
def when_I_retrieve_the_order_item(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/order_items/{}/'.format(id))


@step("the following order item details are returned:")
def and_the_following_order_item_details_are_returned(step):
    """
    :type step: lettuce.core.Step
    """
    resp = json.loads(world.response.data)
    assert_equals(world.resp['entries'], resp['entries'])


""" Get order item rainy case """


@step("I retrieve an order item with resource url '/api/v1/orders/2/'")
def given_I_retrieve_an_order_item_with_resource_url(step):
    """
    :type step: lettuce.core.Step
    """
    world.order_item_uri = '/api/v1/orders/2/'


@step("I retrieve the JSON result")
def when_I_retrieve_the_JSON_result(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(world.order_item_uri)


@step('It should have a field "count " 0')
def and_It_should_have_a_field_count0(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.resp['count'], '0')


@step('It should have an empty field " entries "')
def and_It_should_have_an_empty_field_entries(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp['entries']), 0)


@step('It should have a field "message " \'(.*)\'')
def and_It_should_have_a_field_message_No_entries_found(step, message):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['message'], message)


""" CREATE SUPPLIER sunny case"""


@step("I have the following supplier details")
def given_I_have_the_following_supplier_details(step):
    """
    :type step: lettuce.core.Step
    """
    world.supplier1 = step.hashes[0]


@step("I Post the supplier to resource_url  '/api/v1/suppliers/'")
def when_I_post_the_supplier_to_resource_url(step):
    """
    :type step: lettuce.core.Step
    """
    world.supplier_post_uri = '/api/v1/suppliers/'
    world.supplier_post_response = world.app.post(world.supplier_post_uri, data=json.dumps(world.supplier1))


@step("I should get a response \'(.*)\'")
def then_i_should_get_a_201_response(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.supplier_post_response.status_code, int(expected_status_code))


@step('I should get a "status" containing "ok"')
def and_i_should_get_a_status_containing_ok(step):
    """
    :type step: lettuce.core.Step
    """
    world.supplier_post_response_json = json.loads(world.supplier_post_response.data)
    print world.supplier_post_response_json
    assert_equals(world.supplier_post_response_json['status'], 'ok')


@step('I should get a "message" containing "ok"')
def and_i_should_get_a_message_containing_ok(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.supplier_post_response_json['message'], 'OK')


""" CREATE SUPPLIER sunny and rainy case"""


@step("I have the following supplier details")
def given_I_have_the_following_supplier_details(step):
    """
    :type step: lettuce.core.Step
    """
    world.supplier1 = step.hashes[0]


@step("I Post the supplier to resource_url  \'(.*)\'")
def when_I_post_the_supplier_to_resource_url(step, url):
    """
    :type step: lettuce.core.Step
    """
    world.supplier_post_uri = url
    world.supplier_post_response = world.app.post(world.supplier_post_uri, data=json.dumps(world.supplier1))


@step("I should get a response \'(.*)\'")
def then_i_should_get_a_201_response(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.supplier_post_response.status_code, int(expected_status_code))


@step('I should get a "status" containing \'(.*)\'')
def and_i_should_get_a_status_containing_ok(step, status):
    """
    :type step: lettuce.core.Step
    """
    world.supplier_post_response_json = json.loads(world.supplier_post_response.data)
    print world.supplier_post_response_json
    assert_equals(world.supplier_post_response_json['status'], status)


@step('I should get a "message" containing \'(.*)\'')
def and_i_should_get_a_message_containing_ok(step, message):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.supplier_post_response_json['message'], message)


"""GET SUPPLIER ID Sunny Case"""


@step("supplier \'(.*)\' is in the system")
def given_supplier1_is_in_the_system(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.supplier = world.app.get('/api/v1/suppliers/{}/'.format(id))
    world.resp = json.loads(world.supplier.data)
    assert_equals(world.resp['status'], 'ok')


@step("I retrieve the supplier \'(.*)\'")
def when_I_retrieve_the_supplier1(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/suppliers/{}/'.format(id))


@step("the following supplier details are returned:")
def and_the_following_supplier_details(step):
    """
    :type step: lettuce.core.Step
    """
    resp = json.loads(world.response.data)
    assert_equals(world.resp['entries'], resp['entries'])


""" END """

""" GET SUPPLIER ID Rainy case """


@step("I retrieve a supplier with resource url \'(.*)\'")
def given_I_retrieve_a_supplier2(step, url):
    """
    :param url:
    :type step: lettuce.core.Step
    """
    world.supplier_uri = url


@step("I get the JSON result")
def when_I_get_the_JSON_result(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(world.supplier_uri)


@step('It should have a field "message" \'(.*)\'')
def and_it_should_have_a_field_message_ok(step, message):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['message'], message)


@step('It should have a field "count" 0')
def and_it_should_have_a_field_count0(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.resp['count'], '0')


@step('It should have an empty field "entries"')
def and_it_should_have_an_empty_field_entries(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp['entries']), 0)

#
# @step("the supplier id 1 is in the database with the following details")
# def step_impl(step):
#     """
#     :type step: lettuce.core.Step
#     """
#     world.supplier_old = step.hashes[0]
#
#
# @step("the new supplier details for supplier id 1")
# def step_impl(step):
#     """
#     :type step: lettuce.core.Step
#     """
#     world.supplier_new = step.hashes[0]
#
#
# @step("I send a PUT request to the supplier resource url \'(.*)\'")
# def step_impl(step, url):
#     """
#     :type step: lettuce.core.Step
#     """
#     world.put_response = world.app.put(url, data=json.dumps(world.supplier_new))
#     world.put_response_json = json.loads(world.put_response.data)
#
#
# @step('I should get a "message" containing "OK"')
# def and_I_should_get_a_message_containing_ok(step):
#     """
#     :type step: lettuce.core.Step
#     """
#     assert_equals(world.put_response_json['status'], 'ok')
#
