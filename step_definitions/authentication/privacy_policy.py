from __future__ import absolute_import

from behave import when
from selenium.webdriver.common.by import By

from step_definitions.common.forms import fill_out_form, type_in_field, check_field, submit_without_form


@when(u'I agree to the terms and conditions')
def step_impl(context):
    """
    Step definitions for agreeing to the terms and conditions

    :param context:
    :return:
    """

    context.navigator.wait_for_element((By.CSS_SELECTOR, '.privacy-policy'))
    type_in_field(context, 'accept-terms', True)
    submit_without_form(context)

    return
