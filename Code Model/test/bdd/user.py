import json
from lettuce import step, world, before
from nose.tools import assert_equals
from webtest import TestApp
from app import app

@before.all
def before_all():
    world.app = app.test_client()

"""
Get User Sunny Case
"""


@step("user id \'(.*)\' is in the system")
def given_user_id_1_is_in_the_system(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.browser = TestApp(app)
    world.response = world.browser.get('/#/user/add')
    world.response.charset = 'utf8'
    assert_equals(world.response.status_code, 200)
    assert_equals(json.loads(world.response.text), {"status": "ok"})
    world.user = world.app.get('/api/v1/users/{}/'.format(id))
    world.resp = json.loads(world.user.data)
#    assert_equals(world.resp['status'], 'ok')

@step("I retrieve the user \'(.*)\'")
def step_impl(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/users/{}/'.format(id))


@step("I get \'(.*)\' response")
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


@step("I access the url \'(.*)\'")
def step_impl(step, url):
    """
    :type step: lettuce.core.Step
    """
    world.user_uri = url


@step("I retrieve the JSON results")
def when_i_retrieve_the_json_results(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(world.user_uri)


@step("it should have a field \'(.*)\' containing \'(.*)\'")
def step_impl(step, status, txt):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.load(world.response.data)
    assert_equals(world.resp[status], txt)


@step("it should have an empty field 'entries'")
def step_impl(step, entries):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp[entries], 0))