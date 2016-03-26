import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import app
from webtest import TestApp


@before.all
def before_all():
    world.app = app.test_client()



""" Create cart item sunny case """


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


@step('I should get "status" "ok"')
def and_I_should_get_status_ok(step):
    """
    :type step: lettuce.core.Step
    """
    world.cartItem_post_response_json = json.loads(world.cartItem_post_response.data)
    assert_equals(world.cartItem_post_response_json['status'], 'ok')


@step('I should get "message" "ok"')
def and_I_should_get_message_ok(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.cartItem_post_response_json['message'], 'OK')


""" Create cart item rainy case """


@step("I have already added the following cart item details")
def given_I_have_already_added_the_following_cart_item_details(step):
    """
    :type step: lettuce.core.Step
    """
    world.cartItem1 = step.hashes[0]


@step('I should get "message" "id exists"')
def and_I_should_get_a_message_id_exists(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.cartItem_post_response_json['message'], 'ID EXISTS')


""" Get Cart Item sunny case """


@step("cart item \'(.*)\' is in the system")
def given_cart_item1_is_in_the_system(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.browser = TestApp(app)
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


@step('it should have a field "message" "No entries found"')
def and_it_should_have_a_field_message_No_entries_found(step):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['message'], 'No entries found')

