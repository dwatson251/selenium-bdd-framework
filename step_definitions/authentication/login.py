from __future__ import absolute_import

from behave import when
from step_definitions.common.forms import fill_out_form


@when(u'I enter credentials as "{profile}"')
def step_impl(context, profile):
    """
    Step definitions for filling out an entire form with a specific profile from the JSON file

    :param context:
    :param profile:
    :return:
    """

    fill_out_form(context, 'form-login', profile)
    return
