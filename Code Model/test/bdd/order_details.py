import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import app
from app.views import ORDER_DETAILS

@before.all
def before_all():
    world.app = app.test_client()


@step("order detail id \'(.*)\' is filled")
def give_some_order_details_are_in_the_system(step,id):
    """
    :type step: lettuce.core.Step
    """
    ORDER_DETAILS.update()


@step("I retrieve the order detail \'(.*)\'")
def when_i_retrieve_the_order_detail1(step, order_details_id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/order_details/{}/'.format(order_details_id))


@step(u"I should get a \'(.*)\' response")
def then_i_should_get_a_200_response(step, expected_status_code):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))

@step("the following user details are returned:")
def and_the_following_user_details_are_returned(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(step.hashes, [json.loads(world.response.data)])


@step("order detail id \'(.*)\' is not filled")
def step_impl(step,id):
    """
    :type step: lettuce.core.Step
    """
    ORDER_DETAILS.update()