import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import app
from app.views import ORDER

@before.all
def before_all():
    world.app = app.test_client()

@step("some Orders are in the system")
def given_some_orders_are_in_the_system(step):
    """
    :type step: lettuce.core.Step
    """
    ORDER.update()


@step("I retrieve the order \'(.*)\'")
def step_impl(step, id):
    """
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
    assert_equals(step.hashes, [json.loads(world.response.data)])