import json
from lettuce import step, world, before
from nose.tools import assert_equals

from app import create_app


@before.all
def before_all():
    world.app = create_app('testing')
    world.browser = world.app.test_client()


"""
Get User Sunny Case
"""


