import json

from lettuce import step, world, before
from nose.tools import assert_equals

from flask import current_app as app
from app.views import CATEGORIES


from app import create_app

@before.all
def before_all():
    world.app = create_app('testing')
    world.client = world.app.test_client()

@step("some categories are in a system")
def given_some_categories_are_in_the_system(step):
    """
    :type step: lettuce.core.Step
    """
    CATEGORIES.update({'id': '3', 'name': 'pro gear', 'description': 'signature team gear', 'main_image': 'team gear.jpg', 'parent_category_id': '1', 'is_actice': 'True'})


@step("I retrieve the category \'(.*)\'")
def when_I_retrieve_the_category1(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/product_categories/'.format(id))


@step("I should get a \'(.*)\' response")
def then_i_should_get_a_200_response(step, expected_status_code):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))


@step("the following category details are returned:")
def the_following_category_details(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(int(step.hashes[0]['id']), int([json.loads(world.response.data)][0]['entries'][0]['id']))
    assert_equals(step.hashes[0]['name'], [json.loads(world.response.data)][0]['entries'][0]['name'])
    assert_equals(step.hashes[0]['description'], [json.loads(world.response.data)][0]['entries'][0]['description'])
