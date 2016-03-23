from lettuce import before, world
from selenium import webdriver
import lettuce_webdriver.webdriver

@before.all
def setup_browser():
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    desired_capabilities['version'] = '12'
    desired_capabilities['platform'] = 'WINDOWS'
    desired_capabilities['name'] = 'Testing Selenium 2 with Lettuce'

    world.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://key:secret@hub.testingbot.com:4444/wd/hub"
    )