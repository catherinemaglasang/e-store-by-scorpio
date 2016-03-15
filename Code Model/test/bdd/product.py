import json
from lettuce import step, world, before
from nose.tools import assert_equals
from app import app
from app.views import PRODUCTS

@before.all
def before_all():
    world.app = app.test_client()


@step("product id 1 is an existing product")
def given_product_id_1_is_a_valid_product(step):
    """
    :type step: lettuce.core.Step
    """
    world.product = world.app.get('/api/v1/products/1/')
    world.resp = json.loads(world.product.data)
    assert_equals(world.resp['status'], 'ok')


@step("I try to get the details for product id 1")
def when_i_try_to_get_the_details_for_product_id_1(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/products/1/')

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
