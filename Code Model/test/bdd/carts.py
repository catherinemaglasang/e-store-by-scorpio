import json

from lettuce import step, world, before
from nose.tools import assert_equals

from webtest import TestApp

from app import create_app


@before.all
def before_all():
    app = create_app('testing')
    world.app = app.test_client()


""" Create Cart sunny case  """


@step("I have the following cart details")
def given_I_have_the_following_cart_details(step):
    """
    :type step: lettuce.core.Step
    """
    world.cart1 = step.hashes[0]


@step("I Post the cart to resource_url  '/api/v1/carts/'")
def when_I_Post_the_cart_to_resource_url(step):
    """
    :type step: lettuce.core.Step
    """
    world.cart_post_uri = '/api/v1/carts/'
    world.cart_post_response = world.app.post(world.cart_post_uri, data=json.dumps(world.cart1))


@step("I should have a status code response \'(.*)\'")
def then_I_should_have_a_status_code_response(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.cart_post_response.status_code, int(expected_status_code))


@step("I should get a status ok")
def and_I_should_get_a_status_ok(step):
    """
    :type step: lettuce.core.Step
    """
    world.cart_post_response_json = json.loads(world.cart_post_response.data)
    assert_equals(world.cart_post_response_json['status'], 'ok')


@step("I should get a message ok")
def and_I_should_get_a_message_ok(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.cart_post_response_json['message'], 'OK')


""" Create Cart rainy case """


@step("I have already added the cart details:")
def given_I_have_already_added_the_cart_details(step):
    """
    :type step: lettuce.core.Step
    """
    world.cart1 = step.hashes[0]


@step("I should get a message id exists")
def and_I_should_get_a_message_id_exists(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.cart_post_response_json['message'], 'ID EXISTS')


""" Get Cart sunny case """


@step("cart \'(.*)\' is in the system")
def given_cart_is_in_the_system(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.browser = TestApp(app)
    world.cart = world.app.get('/api/v1/carts/{}/'.format(id))
    world.resp = json.loads(world.cart.data)
    assert_equals(world.resp['status'], 'ok')


@step("I retrieve the cart \'(.*)\'")
def when_I_retrieve_the_cart(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/carts/{}/'.format(id))


@step("the following details are returned :")
def and_the_following_details_are_returned(step):
    """
    :type step: lettuce.core.Step
    """
    resp = json.loads(world.response.data)
    assert_equals(world.resp['entries'], resp['entries'])


""" Get Cart rainy case """


@step("I retrieve a cart with resource url \'(.*)\'")
def given_I_retrieve_a_cart_with_resource_url(step, url):
    """
    :param url:
    :type step: lettuce.core.Step
    """
    world.cart_uri = url


@step("i retrieve a JSON result")
def when_i_retrieve_a_JSON_result(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(world.cart_uri)


@step('it should  have a field "count" 0')
def and_it_should_have_a_field_count0(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.resp['count'], '0')


@step('it should  have a field "message" "No entries found"')
def and_it_should_have_a_field_message_no_entries(step):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['message'], 'No entries found')


@step('it should  have an empty field " entries "')
def and_it_should_have_an_empty_field_entries(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp['entries']), 0)
