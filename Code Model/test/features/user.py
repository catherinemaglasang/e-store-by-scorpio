import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import app
from app.views import USERS

@before.all
def before_all():
    world.app = app.test_client()

@step("some users are in the system")
def Given_some_users_are_in_the_system(step):
    """
    :type step: lettuce.core.Step
    """
    USERS.update({'1': {'user_id': '1', 'username': 'king', 'password': 'test', 'is_active': 'true'}})


@step("I retrieve the user \'(.*)\'")
def When_I_retrieve_the_user1(step, user_id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/users/{}'.format(user_id))

@step("I should get a \'(.*)\' response")
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