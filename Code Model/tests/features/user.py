from lettuce import step, world, before
from nose.tools import assert_equals
from flask import json
from app import app
from app.views import USERS

@before.all
def before_all():
    world.app = app.test_client()

@step("some users are in the system")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    USERS.update({'1': {'user_id': '1', 'username': 'king', 'password': 'test', 'is_active': 'true'}})


@step("I retrieve the user \'(.*)\'")
def step_impl(step, user_id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/users/{}'.format(user_id))


@step("the following user details are returned:")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(step.hashes, [json.loads(world.response.data)])