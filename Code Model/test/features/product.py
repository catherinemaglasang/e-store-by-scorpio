import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import app
from app.views import PRODUCTS

@before.all
def before_all():
    world.app = app.test_client()

@step("some products are in a system")
def given_some_products_are_in_the_system(step):
    """
    :type step: lettuce.core.Step
    """
    PRODUCTS.update({'1': {'id': '1', 'sku': '123', 'title': 'Patata', 'description': 'Baked Potato', 'unit_price': '10','category_id': '1', 'on_hand': '100', 're_order_level': '10', 'is_active': 'true'}})


@step("I retrieve the product \'(.*)\'")
def when_i_retrieve_the_product1(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/products/{}/'.format(id))


@step("I should get a \'(.*)\' response")
def then_i_should_get_a_200_response(step, expected_status_code):
    """
    :param expected_status_code:
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))

@step("the following product details are returned:")
def the_following_product_details(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(step.hashes, [json.loads(world.response.data)])
