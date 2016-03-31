import json
from lettuce import step, world, before
from nose.tools import assert_equals
from webtest import TestApp

from app import create_app


@before.all
def before_all():
    app = create_app()
    world.app = app.test_client()


"""
Get User Sunny Case
"""


@step("user id \'(.*)\' is in the system")
def given_user_id_1_is_in_the_system(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.user = world.app.get('/api/v1/users/{}/'.format(id))
    world.resp = json.loads(world.user.data)
    assert_equals(world.resp['status'], 'ok')


@step("I retrieve the user \'(.*)\'")
def step_impl(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/users/{}/'.format(id))


@step("I get the \'(.*)\' response")
def then_i_get_a_200_response(step, exp_status_code):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(exp_status_code))


@step("the following user details are shown:")
def and_the_following_user_details_are_returned(step):
    """
    :param step:
    """
    resp = json.loads(world.response.data)
    assert_equals(world.resp, resp)


"""
Get User Rainy Case
"""


@step("I access the user url \'(.*)\'")
def step_impl(step, url):
    """
    :type step: lettuce.core.Step
    """
    world.user_uri = url


@step("I retrieve the user JSON result")
def when_i_retrieve_the_json_results(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(world.user_uri)


@step("it should have a user field \'(.*)\' containing \'(.*)\'")
def step_impl(step, status, txt):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp[status], txt)


@step("it should have an empty field \'(.*)\'")
def step_impl(step, entries):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp[entries]), 0)


""" CREATE USER """


@step("I have the following user details:")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.user1 = step.hashes[0]


@step("I POST to the user url \'(.*)\'")
def step_impl(step, url):
    """
    :type step: lettuce.core.Step
    """
    world.user_post_uri = url
    world.user_post_response = world.app.post(world.user_post_uri, data=json.dumps(world.user1))


@step("I get the create \'(.*)\' response")
def step_impl(step, exp_status_code):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.user_post_response.status_code, int(exp_status_code))


@step("I should get a user field \'(.*)\' containing \'(.*)\'")
def step_impl(step, status, txt):
    """
    :type step: lettuce.core.Step
    """
    world.user_post_response_json = json.loads(world.user_post_response_json.data)
    assert_equals(world.user_post_response_json[status], txt)
