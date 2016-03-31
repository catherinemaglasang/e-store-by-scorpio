import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import create_app


@before.all
def before_all():
    app = create_app()
    world.app = app.test_client()


""" Get Wishlist - sunny case """


@step("wishlist \'(.*)\' is in the system")
def given_wishlist_is_in_the_system(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """

    world.resp = world.app.get('/api/v1/wishlist/'.format(id))
    data = json.loads(world.resp.data)
    #raise Exception(json.loads(world.resp.data))
    assert_equals(data['status'], 'ok')


@step("I retrieve the wishlist \'(.*)\'")
def when_I_retrieve_the_wishlist(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/wishlist/'.format(id))


@step("I should have a status code response \'(.*)\'")
def then_i_should_have_a_status_code_response_200(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))



@step("the following details are returned :")
def and_the_following_details_are_returned(step):
    """
    :type step: lettuce.core.Step
    """
    resp = world.response.data
    #raise Exception(json.loads(world.response.data))
    assert_equals(world.resp.data, resp)


""" Get Wishlist - rainy case """


@step("I retrieve a wishlist with resource url \'(.*)\'")
def given_I_retrieve_a_wishlist_with_resource_url(step, url):
    """
    :param url:
    :type step: lettuce.core.Step
    """
    world.wishlist_uri = url


@step("i retrieve a JSON result")
def when_i_retrieve_a_JSON_result(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(world.wishlist_uri)


@step("I should have a status code response \'(.*)\'")
def step_impl(step, expected_status_code):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))


@step("I should get a status 'ok'")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    # world.categories = world.app.get('/api/v1/categories/<category_id>/'.format(id))
    world.resp = world.response.data
    #raise Exception(json.loads(world.response.data))
    assert_equals(world.resp['status'], 'ok')


@step("it should  have a field count '0'")
def and_it_should_have_a_field_count0(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.resp['count'], '0')


@step("it should  have a field message 'No entries found'")
def and_it_should_have_a_field_message_no_entries(step):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['message'], 'No entries found')


@step("it should  have an empty field 'entries'")
def and_it_should_have_an_empty_field_entries(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp['entries']), 0)
