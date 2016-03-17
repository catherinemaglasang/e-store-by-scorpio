import json
from lettuce import step, world, before
from nose.tools import assert_equals
from app import app
from webtest import TestApp


@before.all
def before_all():
    world.app = app.test_client()


""" CREATE SUPPLIER """


@step("I have the following supplier details")
def given_I_have_the_following_supplier_details(step):
    """
    :type step: lettuce.core.Step
    """
    world.supplier1 = step.hashes[0]


@step("I Post the supplier to resource_url  '/api/v1/suppliers/'")
def when_I_post_the_supplier_to_resource_url(step):
    """
    :type step: lettuce.core.Step
    """
    world.supplier_post_uri = '/api/v1/suppliers/'
    world.supplier_post_response = world.app.post(world.supplier_post_uri, data=json.dumps(world.supplier1))


@step("I should get a response \'(.*)\'")
def then_i_should_get_a_201_response(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.supplier_post_response.status_code, int(expected_status_code))


@step('I should get a "status" containing "ok"')
def and_i_should_get_a_status_containing_ok(step):
    """
    :type step: lettuce.core.Step
    """
    world.supplier_post_response_json = json.loads(world.supplier_post_response.data)
    assert_equals(world.supplier_post_response_json['status'], 'ok')


@step('I should get a "message" containing "ok"')
def and_i_should_get_a_message_containing_ok(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.supplier_post_response_json['message'], 'ok')

""" END """


"""GET SUPPLIER ID Sunny Case"""


@step("supplier \'(.*)\' is in the system")
def given_supplier1_is_in_the_system(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.browser = TestApp(app)
    world.response = world.browser.get('/#/dashboard/suppliers/add')
    world.response.charset = 'utf8'
    assert_equals(world.response.status_code, 200)
    assert_equals(json.loads(world.response.text), {"status": "ok"})
    world.supplier = world.app.get('/api/v1/suppliers/{}/'.format(id))
    world.resp = json.loads(world.supplier.data)
    assert_equals(world.resp['status'], 'ok')


@step("I retrieve the supplier \'(.*)\'")
def when_I_retrieve_the_supplier1(step, id):
    """
    :param id:
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/suppliers/{}/'.format(id))


@step("I should get a \'(.*)\' response")
def then_i_should_get_a_200_response(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))


@step("the following supplier details are returned:")
def and_the_following_supplier_details(step):
    """
    :type step: lettuce.core.Step
    """
    resp = json.loads(world.response.data)
    assert_equals(world.resp['entries'], resp['entries'])


""" END """


""" GET SUPPLIER ID Rainy case """

@step("I retrieve a supplier with resource url \'(.*)\'")
def given_I_retrieve_a_supplier2(step, url):
    """
    :param url:
    :type step: lettuce.core.Step
    """
    world.supplier_uri = url


@step("I retrieve the JSON result")
def when_I_retrieve_the_JSON_result(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(world.supplier_uri)


@step("I should get a status code \'(.*)\'")
def then_I_should_get_a_status_code(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))


@step('It should have a field "status" "ok"')
def and_it_should_have_a_field_status_ok(step):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['status'], 'ok')


@step('It should have a field "message" "No entries found"')
def and_it_should_have_a_field_message_ok(step):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['message'], 'No entries found')


@step('It should have a field "count" 0')
def and_it_should_have_a_field_count0(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.resp['count'], '0')


@step('It should have an empty field "entries"')
def and_it_should_have_an_empty_field_entries(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp['entries']), 0)


