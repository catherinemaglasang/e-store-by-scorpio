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
    PRODUCTS.update({'sku': '123', 'category_id': '1', u'description': u'Baked Potato', u'title': u'Patata', u'is_active': u'True', u'unit_price': u'10.0', u'supplier_id': u'1', u'on_hand': u'100', u're_order_level': u'10'})


@step("I retrieve the product \'(.*)\'")
def when_i_retrieve_the_product1(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/products/{}/'.format(id))


@step(u"I should get a \'(.*)\' response")
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
