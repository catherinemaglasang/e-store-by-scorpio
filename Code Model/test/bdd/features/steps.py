import json
from lettuce import *
from nose.tools import assert_equals
from app import create_app

@before.all
def before_all():
    app = create_app('testing')
    world.app = app.test_client()


# ----------------------------------------------------------------
# Common steps for retrieving data in any of the tables. We want to check its status, and fields.
@step('I access the url "(?P<url>.+)"')
def given_i_access_the_url_url(step, url):
    world.response = world.app.get(url)
    world.response_data = json.loads(world.response.data)


@step('I get a "(?P<status_code>.+)" response')
def i_get_a_response(step, status_code):
    assert_equals(world.response.status_code, int(status_code))


@step('I get an "(?P<status>.+)" status')
def i_get_a_status(step, status):
    assert_equals(world.response_data['status'], status)


@step('I get an "(?P<message>.+)" message')
def i_get_a_message(step, message):
    assert_equals(world.response_data['message'], message)


# ----------------------------------------------------------------
# Common steps for adding data in any of the tables. We want to check its status, and fields.
@step("I have the following data")
def give_i_have_the_following_data(step):
    world.data = step.hashes[0]


@step('I POST to the url "(.*)"')
def i_post_to_the_url_url(step, url):
    world.response = world.app.post(url, data=json.dumps(world.data))
    world.response_data = json.loads(world.response.data)


@step('I get a field "(.*)" containing "(.*)"')
def i_get_a_field_field_containing_value(step, field, field_value):
    assert_equals(world.response_data[field], field_value)
# ----------------------------------------------------------------
# Common steps for updating data in any of the tables.


@step('I have a resource with the id "(.*)"')
def i_have_a_resource_with_id_id(step, id):
    world.resource_id = id


@step("I want to update its data to the following data")
def i_want_to_update_its_data(step):
    world.new_resource_data = step.hashes[0]


@step('I have the resource url "(.*)"')
def i_have_the_resource_url(step, resource_url):
    world.resource = resource_url


@step("I send a PUT request from client")
def i_send_a_put_request_from_client(step):
    world.response = world.app.put(world.resource, data = json.dumps(world.new_resource_data))
    world.response_data = json.loads(world.response.data)

# The rest of the field checking steps are already implemented

