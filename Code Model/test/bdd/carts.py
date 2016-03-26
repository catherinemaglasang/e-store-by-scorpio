import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import app
from webtest import TestApp


@before.all
def before_all():
    world.app = app.test_client()


""" Get Cart sunny case """
@step("cart \'(.*)\' is in the system")
def step_impl(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.browser = TestApp(app)
    world.cart = world.app.get('/api/v1/carts/{}/'.format(id))
    world.resp = json.loads(world.cart.data)
    assert_equals(world.resp['status'], 'ok')


@step("I retrieve the cart \'(.*)\'")
def step_impl(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/carts/{}/'.format(id))


@step("I should get a \'(.*)\' response")
def then_i_should_get_a_200_response(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))


@step("the following details are returned :")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    resp = json.loads(world.response.data)
    assert_equals(world.resp['entries'], resp['entries'])


""" Get Cart rainy case """
@step("I retrieve a cart with resource url \'(.*)\'")
def step_impl(step, url):
    """
    :param url:
    :type step: lettuce.core.Step
    """
    world.cart_uri = url


@step("i retrieve a JSON result")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(world.cart_uri)


@step("i should get a \'(.*)\' status code")
def step_impl(step, expected_status_code):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))


@step('it should  have a field "status" "ok"')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['status'], 'ok')


@step('it should  have a field "count" 0')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.resp['count'], '0')


@step('it should  have an empty field " entries "')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp['entries']), 0)


@step('it should  have a field "message" "No entries found"')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['message'], 'No entries found')


""" Create Cart sunny case  """


@step("I have the following cart details")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.cart1 = step.hashes[0]


@step("I Post the cart to resource_url  '/api/v1/carts/'")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.cart_post_uri = '/api/v1/carts/'
    world.cart_post_response = world.app.post(world.cart_post_uri, data=json.dumps(world.cart1))


@step("I should have a status code response \'(.*)\'")
def step_impl(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.cart_post_response.status_code, int(expected_status_code))


@step("I should get a status ok")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.cart_post_response_json = json.loads(world.cart_post_response.data)
    assert_equals(world.cart_post_response_json['status'], 'ok')


@step("I should get a message ok")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.cart_post_response_json['message'], 'OK')


""" Create Cart rainy case """


@step("I have already added the cart details:")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.cart1 = step.hashes[0]


@step("I should get a message id exists")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.cart_post_response_json['message'], 'ID EXISTS')