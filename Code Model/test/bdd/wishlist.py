import json
from lettuce import step, world, before
from nose.tools import assert_equals
from app import app
from app.views import WISHLISTS

@before.all
def before_all():
    world.app = app.test_client()


@step("some wishlists are in a system")
def given_some_wishlists_are_in_the_system(step):
    """
    :type step: lettuce.core.Step
    """
    WISHLISTS.update({'id': '1'})


@step("I retrieve the wishlist \'(.*)\'")
def when_i_retrieve_the_wishlist1(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/wishlist/'.format(id))


@step(u"I should get a \'(.*)\' response")
def then_i_should_get_a_200_response(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))


@step("the following wishlist details are returned:")
def the_following_wishlist_details(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(int(step.hashes[0]['id']), [json.loads(world.response.data)][0]['entries'][0]['id'])
