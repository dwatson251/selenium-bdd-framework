"""
The file contains functions necessary for configuration the chrome driver, as well as configuration options defined
in behave.ini.
"""
from __future__ import absolute_import
from selenium import webdriver
import time

from framework.navigator.navigator import Navigator
from framework.navigator.routes import Routes


def get_web(browser):
    """
    Defines the web driver for the automated tests, as well as additional options.

    :param browser:
    :return:
    """

    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        return Navigator(webdriver.Chrome(chrome_options=chrome_options))


def before_all(context):
    """
    Runs prior to all running tests.

    Defines "global" configuration options defined from the behave.ini file

    :param context:
    :return:
    """

    # Defines the driver (Chrome in this case)
    context.navigator = get_web('chrome')

    # Defines the API url in which all API related calls will be made to
    context.api_url = context.config.userdata['api_url']

    # Defines the front end URL, in which selenium will use as a base for all routes
    context.base_url = context.config.userdata['frontend_url']

    # Defines the file used for defining the routes.
    context.routes = Routes(context, 'resources/routes.json')

    # Used to store the timestamp of the currently running test. Can be used to create a unique username
    context.timestamp = int(time.time())


def after_all(context):
    """
    Defines all tasks to be ran after all tests have been ran in the current scenario

    Currently set to only close the browser.

    :param context:
    :return:
    """
    context.navigator.browser.close()
    return
