import json

from lettuce import step, world, before
from nose.tools import assert_equals

from flask import current_app as app
from app.views import ORDER

from app import create_app

@before.all
def before_all():
    world.app = create_app('testing')
    world.client = world.app.test_client()

@step("Order id \'(.*)\' is in the system")
def given_some_orders_are_in_the_system(step, id):
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


@step("Order id \'(.*)\' is not in the system")
def step_impl(step, id):
    """
    :type step: lettuce.core.Step
    """
    ORDER.update()