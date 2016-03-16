import json
from lettuce import step, world, before
from nose.tools import assert_equals
from app import app
from app.views import SUPPLIERS


@before.all
def before_all():
    world.app = app.test_client()


"""GET SUPPLIER ID """


@step("supplier \'(.*)\' is in the system")
def given_supplier1_is_in_the_system(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.supplier = world.app.get('/api/v1/suppliers/{}/'.format(id))
    world.resp = json.loads(world.supplier.data)


@step("I retrieve the supplier \'(.*)\'")
def when_I_retrieve_the_supplier1(step, id):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get('/api/v1/suppliers/{}/'.format(id))


@step("I should get a \'(.*)\' response")
def then_i_should_get_a_200_response(step, expected_status_code):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(world.response.status_code, int(expected_status_code))


@step("the following supplier details are returned:")
def and_the_following_supplier_details(step):
    """
    :type step: lettuce.core.Step
    """
    assert_equals(step.hashes, [json.loads(world.response.data)])


""" END """

""" CREATE SUPPLIER """


@step("I am at the add supplier page with url  \'([^\']*)\'")
def given_I_am_at_the_add_supplier_page_with_url(step, url):
    """
    :type step: lettuce.core.Step
    """
    world.response = world.app.get(url)


@step("I add new supplier \'([^\']*)\' \'([^\']*)\' \'([^\']*)\' \'([^\']*)\' \'([^\']*)\' \'([^\']*)\' \'([^\']*)\'")
def when_i_add_new_supplier(step, id, name, address, phone, fax, email, is_active):

    """
    :param is_active:
    :param email:
    :param fax:
    :param name:
    :param id:
    :param address:
    :param phone:
    :type step: lettuce.core.Step
    """

    # for row in step.hashes:
    #     world.id = row["id"]
    #     world.name = row["name"]
    #     world.address = row["address"]
    #     world.phone = row["phone"]
    #     world.fax = row["fax"]
    #     world.email = row["email"]
    #     world.is_active = row["is_active"]

    world.response = world.app.post('/api/v1/suppliers/',
                                    data=dict(id=id, name=name, address=address, phone=phone, fax=fax, email=email,
                                              is_active=is_active), follow_redirects=True)


# @step("I should get a \'(.*)\' response")
# def then_i_should_get_a_202_response(step, expected_status_code):
#     """
#     :param expected_status_code:
#     :type step: lettuce.core.Step
#     """
#     assert_equals(world.response.status_code, int(expected_status_code))


@step("it will return the following")
def and_it_will_return_the_following(step):
    """
    :type step: lettuce.core.Step
    """
    pass


""" END """

