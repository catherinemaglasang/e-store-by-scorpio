import json
from lettuce import step, world, before
from nose.tools import assert_equals
from webtest import TestApp
from app import create_app


@before.all
def before_all():
    app = create_app()
    world.app = app.test_client()


@step("customer id \'(.*)\' is in the system")
def step_impl(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.customer = world.app.get('/api/v1/customers/{}/'.format(id))
    world.resp = json.loads(world.customer.data)
    assert_equals(world.resp['status'], 'ok')


@step("I retrieve the customer id \'(.*)\'")
def step_impl(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/customers/{}/'.format(id))


@step("I get the customer \'(.*)\' response")
def then_i_get_a_200_response(step, exp_status_code):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(exp_status_code))


@step("the following customer details are shown:")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    resp = json.loads(world.response.data)
    assert_equals(world.resp, resp)


@step("I access the customer url \'(.*)\'")
def step_impl(step, url):
    """
    :type step: lettuce.core.Step
    """
    world.customer_uri = url


@step("I retrieve the customer JSON result")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(world.customer_uri)


@step("it should have a customer field \'(.*)\' containing \'(.*)\'")
def step_impl(step, status, txt):
    """
    :type step: lettuce.core.Step
    """
    world.resp = json.loads(world.response.data)
    assert_equals(world.resp[status], txt)


@step("it should have an empty customer field \'(.*)\'")
def step_impl(step, entries):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(len(world.resp[entries]), 0)
