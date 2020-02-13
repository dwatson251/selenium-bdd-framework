from __future__ import absolute_import

import json
from time import sleep

import requests
from behave import when
from selenium.webdriver.common.by import By

from step_definitions.common.profile import Profile
from framework.form_interaction.form import Form
from framework.form_interaction.field_input import FieldInput


@when(u'I type "{text}" in to "{field}"')
def type_in_field(context, field, text):
    """
    Defines a step definition for typing text in to a field selected by name

    :param context:
    :param field:
    :param text:
    :return:
    """

    field = FieldInput(context, "[ng-reflect-name='{field}'], [name='{field}'], [formcontrolname='{field}']"
                       .format(field=field))
    field.input(text)
    return


@when(u'I check {checkbox_field}')
def check_field(context, field_name):
    field = FieldInput(context, "[ng-reflect-name='{field}'], [name='{field}'], [formcontrolname='{field}']"
                       .format(field=field_name))
    field.input_select(True)
    return


@when(u'I fill out {form_name} as {profile_name}')
def fill_out_form(context, form_name, profile_name):
    """
    Given a profile and a form name, fills out the entire field using the keys and values from that given
    profile

    :param profile_name:
    :param context:
    :param form_name: The name of the class of the element directly parenting a <form> element.
                      required until forms have some sort of notable class/ ID for selection
    :return:
    """

    profile = Profile(profile_name)
    profile = profile.get_profile()

    form_selector = "#" + form_name

    form = Form(context, form_selector, profile)
    form.fill(form_name)
    form.submit()

    return


def get_otp(context, profile_name, form_name='form-login'):
    """
    Makes an API call to the specified API endpoint and attempts to obtain the OTP for the specified username

    :param profile_name:
    :param context:
    :param form_name:
    :return:
    """

    profile = Profile(profile_name)
    profile = profile.get_profile()

    username = profile[form_name]['username'].format(timestamp=context.timestamp)

    otp_response = requests.get(context.api_url + '/automation/otp/{username}'.format(username=username))
    otp_response_json = otp_response.json()

    return otp_response_json['otp']


def submit_without_form(context):
    context.navigator.wait_for_element((By.CSS_SELECTOR, "[type='submit']"))
    submit = context.navigator.browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()
