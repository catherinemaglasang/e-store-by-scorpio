import json

from lettuce import step, world, before
from nose.tools import assert_equals

from webtest import TestApp

from app import create_app


@before.all
def before_all():
    app = create_app()
    print app.config
    world.app = app.test_client()


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
