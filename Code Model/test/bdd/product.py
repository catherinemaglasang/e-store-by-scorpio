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
    pass


@step("I try to get the details for product id 1")
def when_i_try_to_get_the_details_for_product_id_1(step):
    """
    :type step: lettuce.core.Step
    """
    pass


@step("the following product details are returned:")
def then_the_following_product_details_are_returned(step):
    """
    :type step: lettuce.core.Step
    """
    pass


