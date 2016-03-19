import json
from lettuce import step, world, before
from nose.tools import assert_equals

from flask import current_app as app
from app.config import config
from app import create_app

@before.all
def before_all():
    world.app = create_app('testing')
    world.client = world.app.test_client()

# SCENARIO 1
@step("product id 1 is an existing product")
def given_product_id_1_is_a_valid_product(step):
    """
    :type step: lettuce.core.Step
    """

    world.product = world.client.get('/api/v1/products/1/')
    world.resp = json.loads(world.product.data)
    assert_equals(world.resp['status'], 'ok')


@step("I try to get the details for product id 1")
def when_i_try_to_get_the_details_for_product_id_1(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.client.get('/api/v1/products/1/')

@step("i get a 200 response")
def then_i_get_a_200_response(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, 200)

@step("the following product details are returned:")
def and_the_following_product_details_are_returned(step):
    """
    :type step: lettuce.core.Step
    """
    resp = json.loads(world.response.data)
    assert_equals(world.resp['entries'], resp['entries'])


# SCENARIO 2
@step("I access the resource url \'(.*)\'")
def give_i_access_the_product_resource_url(step, url):
    """
    :type step: lettuce.core.Step
    """
    world.product_uri = url


@step("I retrieve the JSON results")
def when_i_retrieve_the_json_results(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.client.get(world.product_uri)


@step("the status code should be 200")
def then_the_status_code_should_be_200(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, 200)


@step('it should have a field "status" containing "ok"')
def and_it_should_have_a_field_status_ok(step):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp['status'], 'ok')

@step('it should have a field "message" containing "No entries found"')
def and_it_should_have_a_field_message_contaning_no_entries_found(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.resp['message'], 'No entries found')

@step('it should have a field "count" containing 0')
def and_it_should_have_a_field_count_0(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.resp['count'], '0')


@step('it should have an empty field "entries"')
def it_should_have_an_empty_field_entries(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp['entries']), 0)


# SCENARIO 3: Create a new product
@step("I have the following product details:")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.product1 = step.hashes[0]


@step('I should get a field "message" containing "ok"')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.product_post_response_json = json.loads(world.product_post_response.data)
    assert_equals(world.product_post_response_json['message'], 'ok')

# SCENARIO 4
@step("I have already added the product details:")
def i_have_already_added_product_1(step):
    """
    :type step: lettuce.core.Step
    """
    world.product1 = step.hashes[0]


@step("I POST to the product resource url '/api/v1/products/'")
def when_i_post_to_the_product_resource_url(step):
    """
    :type step: lettuce.core.Step
    """
    world.product_post_uri = '/api/v1/products/'
    world.product_post_response = world.client.post(world.product_post_uri, data=json.dumps(world.product1))

@step("I should get a 201 response")
def then_i_should_get_a_201_response(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.product_post_response.status_code, 201)


@step('I should get a field "status" containing "ok"')
def and_i_should_get_a_field_status_containing_ok(step):
    """
    :type step: lettuce.core.Step
    """
    world.product_post_response_json = json.loads(world.product_post_response.data)
    assert_equals(world.product_post_response_json['status'], 'ok')


@step('I should get a field "message" containing "id exists"')
def and_i_should_get_a_field_message_containing_id_exists(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.product_post_response_json['message'], 'id exists')

# Scenario 5: Get newly created product
@step("the new product id 99 details that i recently added")
def given_the_new_product_99_details_recently_added(step):
    """
    :type step: lettuce.core.Step
    """
    world.product3 = step.hashes


@step("I access to the product resource url '/api/v1/products/99/' to get the new product id 99")
def when_i_access_the_resource_url_for_product_99(step):
    """
    :type step: lettuce.core.Step
    """
    world.product3_response = world.client.get('/api/v1/products/99/')
    world.product3_json = json.loads(world.product3_response.data)


@step("I should get a 200 response in product id 99 resource")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.product3_response.status_code, 200)

@step('I should receive a field "status" containing "ok" in product id 99 json response')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.product3_json['status'], 'ok')

@step('I should receive a field "message" containing "ok" in product id 99 json response')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.product3_json['message'], 'ok')


@step("I should get a length of 1 in entries of product id 99 json response")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.product3_json['entries']), 1)


@step("I should get an entry with a product id 99")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.product3_json['entries'][0]['product_id'], 99)

# Scenario 6: Update a product
@step("the new product id 99 in database with the following details:")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.product4_old = step.hashes[0]

@step("the new product details for product id 99:")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.product4_new = step.hashes[0]



@step("I send a PUT request to the product resource url 'api/v1/products/99/'")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.put_response = world.client.put('/api/v1/products/99/', data=json.dumps(world.product4_new))
    world.put_response_json = json.loads(world.put_response.data)

@step("I should get a 200 response in the update request")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.put_response.status_code, 200)


@step('I should get a field for "status" containing "ok" for update request')
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.put_response_json['status'], 'ok')
