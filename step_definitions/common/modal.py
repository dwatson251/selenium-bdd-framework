"""
Defines step definitions for modal control
"""

from __future__ import absolute_import

from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from framework.navigator.mouse import Mouse


@when(u'I confirm modal')
def step_impl(context):
    mouse = Mouse(context, '[aria-label="Action"]')
    mouse.click()
    return


@when(u'I cancel modal')
@when(u'I close modal')
def step_impl(context, navigation_id):
    mouse = Mouse(context, '[aria-label="Close"]')
    mouse.click()
    return
