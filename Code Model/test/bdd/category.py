import json
from lettuce import step, world, before
from nose.tools import assert_equals
from app import app
from app.views import CATEGORIES

@before.all
def before_all():
    world.app = app.test_client()


@step("category id 1 is an existing category")
def given_category_id_1_is_a_valid_category(step):
    """
    :type step: lettuce.core.Step
    """
    pass


@step("I try to get the details for category id 1")
def when_i_try_to_get_the_details_for_category_id_1(step):
    """
    :type step: lettuce.core.Step
    """
    pass


@step("the following category details are returned:")
def then_the_following_category_details_are_returned(step):
    """
    :type step: lettuce.core.Step
    """