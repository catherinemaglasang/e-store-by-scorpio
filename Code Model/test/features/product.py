from lettuce import step, world, before
from nose.tools import assert_equals

from app import app
from app.views import PRODUCTS

@before.all
def before_all():
    world.app = app.test_client()

@step("some products are in a system")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    PRODUCTS.update({'1': {'id': '', 'sku': '', 'title': '', 'description': '', 'unit_price': '','category_id': '', 'on_hand': '', 're_order_level': '', 'is_active': ''}})


@step("I retrieve the product '1'")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    pass


@step("I should get a '200' response")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    pass

@step("the following product details are returned:")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    pass