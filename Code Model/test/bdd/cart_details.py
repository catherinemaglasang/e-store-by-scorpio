import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import app
from webtest import TestApp


@before.all
def before_all():
    world.app = app.test_client()


@step("cart detail \'(.*)\' is in the system")
def given_cart_detail1_is_in_the_system(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.browser = TestApp(app)
    world.response = world.browser.get('/#/dashboard/cart_details/add')
    world.response.charset = 'utf8'
    assert_equals(world.response.status_code, 200)
    assert_equals(json.loads(world.response.text), {"status": "ok"})
    world.cart_detail = world.app.get('/api/v1/cart_details/{}/'.format(id))
    world.resp = json.loads(world.cart_detail.data)
    assert_equals(world.resp['status'], 'ok')


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
    resp = json.loads(world.response.data)
    assert_equals(world.resp['entries'], resp['entries'])


# """ """
@step("I retrieve a cart detail with resource url \'(.*)\'")
def step_impl(step, url):
    """
    :param url:
    :type step: lettuce.core.Step
    """
    world.cart_detail_uri = url


@step("i retrieve JSON result")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(world.cart_detail_uri)

@step("i should get a status code \'(.*)\'")
def step_impl(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """

    assert_equals(world.response.status_code, int(expected_status_code))


@step('it should have a field "status" "ok"')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['status'], 'ok')



@step('it should have a field "count" 0')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.resp['count'], '0')


@step('it should have an empty field " entries "')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp['entries']), 0)


@step('it should have a field "message" "No entries found"')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['message'], 'No entries found')

# """ """