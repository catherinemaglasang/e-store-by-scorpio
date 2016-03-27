import json

from lettuce import step, world, before
from nose.tools import assert_equals

from webtest import TestApp

from app import create_app


@before.all
def before_all():
    app = create_app('testing')
    world.app = app.test_client()


""" Create new order sunny case """


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


@step('I should get a "status" "ok"')
def and_I_should_get_a_status_ok(step):
    """
    :type step: lettuce.core.Step
    """
    world.order_post_response_json = json.loads(world.order_post_response.data)
    assert_equals(world.order_post_response_json['status'], 'ok')


@step('I should get a "message" "ok"')
def and_I_should_get_a_message_ok(step):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.order_post_response.data)
    assert_equals(world.resp['message'], 'OK')


""" Create order rainy case """


@step("I have already added the following order details:")
def given_I_have_already_added_the_following_order_details(step):
    """
    :type step: lettuce.core.Step
    """
    world.order1 = step.hashes[0]


@step('I should get a message containing "id exists"')
def and_I_should_get_a_message_containing_id_exists(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.order_post_response_json['message'], 'ID EXISTS')


"""Get Order ID sunny case """


@step("Order id \'(.*)\' is in the system")
def given_order_id1_is_in_the_system(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.browser = TestApp(app)
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
