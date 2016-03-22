import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import app
from webtest import TestApp


@before.all
def before_all():
    world.app = app.test_client()


""" Create order item sunny case """

@step("I have the following order item details")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.order1 = step.hashes[0]


@step("I Post the order item to resource_url  '/api/v1/order_items/'")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.order_post_uri = '/api/v1/order_items/'
    world.order_post_response = world.app.post(world.order_post_uri, data=json.dumps(world.order1))



@step("I should have a response \'(.*)\'")
def step_impl(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.order_post_response.status_code, int(expected_status_code))



@step('I should have a "status" containing "ok"')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.order_post_response_json = json.loads(world.order_post_response.data)
    assert_equals(world.order_post_response_json['status'], 'ok')



@step('I should have a "message" containing "ok"')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.order_post_response_json['message'], 'OK')


@step("order item id \'(.*)\' is in the system")
def order_item_id1_is_in_the_system(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.browser = TestApp(app)
    world.order = world.app.get('/api/v1/order_items/{}/'.format(id))
    world.resp = json.loads(world.order.data)
    assert_equals(world.resp['status'], 'ok')


@step("I retrieve the order item \'(.*)\'")
def step_impl(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/order_items/{}/'.format(id))


@step("the following user details are returned:")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    resp = json.loads(world.response.data)
    assert_equals(world.resp['entries'], resp['entries'])


@step("i should get a status_code \'(.*)\'")
def step_impl(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))



@step("I retrieve an order item with resource url '/api/v1/orders/2/'")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.order_item_uri = '/api/v1/orders/2/'


@step("I retrieve the JSON result")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(world.order_item_uri)


@step("I should get \'(.*)\' status code")
def step_impl(step, expected_status_code):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))


@step('It should have a field "status " "ok"')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['status'], 'ok')


@step('It should have a field "count " 0')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.resp['count'], '0')


@step('It should have an empty field " entries "')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp['entries']), 0)


@step('It should have a field "message " "No entries found"')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['message'], 'No entries found')

