"""
Defines step definitions for normal inspection tasks. Usually to check if something is there when it should be.
"""

from __future__ import absolute_import

from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@then(u'the title should include "{text}"')
def check_title_includes(context, text):
    """
    Checks that the title of the application currently loaded in the browser matches all or part of the specified
    name.

    :param text:
    :param context:
    :return:
    """

    print(text)

    try:
        WebDriverWait(context.navigator.browser, 60).until(
            EC.title_contains(text)
        )
    finally:
        assert EC.title_contains(text)


@then(u'I see "{text_to_witness}"')
@then(u'I should see "{text_to_witness}"')
def step(context, text_to_witness):
    """
    Checks that the body of the document currently loaded contains the specified text

    :param context:
    :param text_to_witness:
    :return:
    """

    context.navigator.web_driver_wait.until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), text_to_witness)
    )
    assert EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), text_to_witness)
