from __future__ import absolute_import

from behave import when
from step_definitions.common.forms import fill_out_form


@when(u'I sign up as "{profile}"')
def step_impl(context, profile):
    """
    Shortcut for filling out the sign up form. Test must be on new user page

    :param context:
    :param profile:
    :return:
    """
    
    fill_out_form(context, 'form-signup', profile)
    return
