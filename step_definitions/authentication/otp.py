from behave import when
from selenium.webdriver.common.by import By

from step_definitions.common.forms import type_in_field, get_otp
from framework.form_interaction.form import Form


@when(u'I enter the OTP as "{profile}"')
def step_impl(context, profile):
    """
    Enters an OTP as long as the OTP dialog is visible. Uses the profile to dictate the username used for the obtaining
    the correct token

    :param context:
    :param profile:
    :return:
    """

    otp = get_otp(context, profile, 'form-login')

    type_in_field(context, 'otp_token', otp)

    form = Form(context, "#form-otp")
    form.submit()

    return
