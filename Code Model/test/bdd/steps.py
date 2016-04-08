import json
from lettuce import *
from nose.tools import assert_equals
from app import create_app
from flask import Flask


@before.all
def before_all():
    app = create_app()
    world.app = app.test_client()


""" Create cart item sunny case and rainy case """





""" CREATE SUPPLIER sunny case"""


# @step("I have the following supplier details")
# def given_I_have_the_following_supplier_details(step):
#     """
#     :type step: lettuce.core.Step
#     """
#     world.supplier1 = step.hashes[0]
#
#
# @step("I Post the supplier to resource_url  '/api/v1/suppliers/'")
# def when_I_post_the_supplier_to_resource_url(step):
#     """
#     :type step: lettuce.core.Step
#     """
#     world.supplier_post_uri = '/api/v1/suppliers/'
#     world.supplier_post_response = world.browser.post(world.supplier_post_uri, data=json.dumps(world.supplier1))
#
#
# @step("I should get a response \'(.*)\'")
# def then_i_should_get_a_201_response(step, expected_status_code):
#     """
#     :param expected_status_code:
#     :type step: lettuce.core.Step
#     """
#     assert_equals(world.supplier_post_response.status_code, int(expected_status_code))
#
#
# @step('I should get a "status" containing "ok"')
# def and_i_should_get_a_status_containing_ok(step):
#     """
#     :type step: lettuce.core.Step
#     """
#     world.supplier_post_response_json = json.loads(world.supplier_post_response.data)
#     print world.supplier_post_response_json
#     assert_equals(world.supplier_post_response_json['status'], 'ok')
#
#
# @step('I should get a "message" containing "ok"')
# def and_i_should_get_a_message_containing_ok(step):
#     """
#     :type step: lettuce.core.Step
#     """
#     assert_equals(world.supplier_post_response_json['message'], 'OK')


""" CREATE SUPPLIER sunny and rainy case"""





"""GET SUPPLIER ID Sunny Case"""





""" END """

""" GET SUPPLIER ID Rainy case """




#
# @step("the supplier id 1 is in the database with the following details")
# def step_impl(step):
#     """
#     :type step: lettuce.core.Step
#     """
#     world.supplier_old = step.hashes[0]
#
#
# @step("the new supplier details for supplier id 1")
# def step_impl(step):
#     """
#     :type step: lettuce.core.Step
#     """
#     world.supplier_new = step.hashes[0]
#
#
# @step("I send a PUT request to the supplier resource url \'(.*)\'")
# def step_impl(step, url):
#     """
#     :type step: lettuce.core.Step
#     """
#     world.put_response = world.app.put(url, data=json.dumps(world.supplier_new))
#     world.put_response_json = json.loads(world.put_response.data)
#
#
# @step('I should get a "message" containing "OK"')
# def and_I_should_get_a_message_containing_ok(step):
#     """
#     :type step: lettuce.core.Step
#     """
#     assert_equals(world.put_response_json['status'], 'ok')
#