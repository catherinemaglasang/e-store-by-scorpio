import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import app
from app.views import SUPPLIERS


@before.all
def before_all():
    world.app = app.test_client()


@step("some suppliers are in a system")
def given_some_suppliers_are_in_the_system(step):
    """
    :type step: lettuce.core.Step
    """
    SUPPLIERS.update({'id': '2', 'name': 'sup2', 'address': 'iligan', 'phone': '2', 'fax': '2', 'email': 'sup2@estore.com', 'is_active': 'True'})


@step("I retrieve the supplier \'(.*)\'")
def when_I_retrieve_the_supplier1(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/suppliers/{}/'.format(id))


@step("I should get a \'(.*)\' response")
def then_i_should_get_a_202_response(step, expected_status_code):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))


@step("the following supplier details are returned:")
def the_following_supplier_details(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(step.hashes, [json.loads(world.response.data)])