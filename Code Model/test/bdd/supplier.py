import json

from lettuce import step, world, before
from nose.tools import assert_equals

from app import app
from app.views import SUPPLIERS


@before.all
def before_all():
    world.app = app.test_client()


"""GET SUPPLIER ID """


@step("supplier \'(.*)\' is in a system")
def given_supplier1_is_in_the_system(step, id):
    """
    :type step: lettuce.core.Step
    """
    SUPPLIERS.update({'id': '1', 'name': 'supplier1', 'address': 'address1', 'phone': '221-2277', 'fax': '063-221-2277',
                      'email': 'supplier1@estore.com', 'is_active': 'True'})


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


""" END """

""" CREATE SUPPLIER """


@step("I am at the add supplier page with url  '/api/v1/suppliers/'")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    pass


@step("I add new supplier with the following details")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    pass


@step("it will return the following")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    pass


""" END """
