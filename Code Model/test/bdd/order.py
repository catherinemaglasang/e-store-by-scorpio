import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import app
from webtest import TestApp

@before.all
def before_all():
    world.app = app.test_client()


@step("Order id \'(.*)\' is in the system")
def given_some_orders_are_in_the_system(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.browser = TestApp(app)
    world.order = world.app.get('/api/v1/orders/{}/'.format(id))
    world.resp = json.loads(world.order.data)
    assert_equals(world.resp['status'], 'ok')


@step("I retrieve the order \'(.*)\'")
def step_impl(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/orders/{}/'.format(id))


@step(u"I should get a \'(.*)\' response")
def then_i_should_get_a_200_response(step, expected_status_code):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))


@step("the following orders information are returned:")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    resp = json.loads(world.response.data)
    assert_equals(world.resp['entries'], resp['entries'])
