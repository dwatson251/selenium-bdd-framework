"""
Provides step definitions for various navigational tasks
"""

from __future__ import absolute_import
from behave import given, when, then

from step_definitions.common.inspection import check_title_includes
from framework.navigator.mouse import Mouse


@given(u'We are on the "{route_name}" page')
def step_impl(context, route_name):
    """
    Step definition for navigation along pages, defined by their route name in the routes.json file

    :param context:
    :param route_name:
    :return:
    """
    context.navigator.open(context.routes.get_route(route_name))
    return


@given(u'We are using "{brand}" "{environment}"')
def step_impl(context, brand, environment):
    """
    Using the standard Embark environment/ brand convention, allows navigation to a specific Embark customer.

    :param context:
    :param brand:
    :param environment:
    :return:
    """
    context.navigator.open('https://{}-{}.paylinksolutions.co.uk'.format(brand, environment))

    # When I click logout
    # Then I should be taken to the "login" page


@given(u'We are on any page')
def step_impl(context):
    """
    Does nothing. For story description only

    :param context:
    :return:
    """
    return


@when(u'I click "{navigation_id}"')
def step_impl(context, navigation_id):
    mouse = Mouse(context, '#{navigation_id}'.format(navigation_id=navigation_id))
    mouse.click()
    return


@then(u'I should be taken to the "{page}" page')
def step_impl(context, page):
    check_title_includes(context, page)
    return
