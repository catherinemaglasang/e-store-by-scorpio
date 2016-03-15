import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import app
from app.views import CART_DETAILS


@before.all
def before_all():
    world.app = app.test_client()


@step("some cart details are in a system")
def given_some_cart_details_are_in_a_system(step):
    """
    :type step: lettuce.core.Step
    """
CART_DETAILS.update({'cart_id': '1', 'product_id': '1', 'quantity': '1', 'time_stamp': '2016-03-11 11:49:17'})


@step("I retrieve the cart detail \'(.*)\'")
def when_I_retrieve_the_cart_detail1(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/cart_details/{}/'.format(id))


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