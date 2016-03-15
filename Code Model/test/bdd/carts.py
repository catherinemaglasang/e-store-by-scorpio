import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import app
from app.views import CARTS


@before.all
def before_all():
    world.app = app.test_client()


@step("some carts are in a system")
def some_carts_are_in_a_system(step):
    """
    :type step: lettuce.core.Step
    """
    CARTS.update({'id': '1', 'session_id': '1', 'date_created': '2016-03-15', 'customer_id': '1', 'time_stamp': '2016-03-15 11:49:17'})


@step("I retrieve the cart \'(.*)\'")
def step_impl(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/carts/{}/'.format(id))


@step("I should get a \'(.*)\' response")
def then_i_should_get_a_200_response(step, expected_status_code):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))



@step("the following cart details are returned:")
def the_following_cart_details(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(step.hashes, [json.loads(world.response.data)])