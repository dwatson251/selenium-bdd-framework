"""
Provides step definitions for various navigational tasks
"""

from __future__ import absolute_import
from behave import given, when, then

from step_definitions.common.inspection import check_title_includes
from step_definitions.common.profile import Profile
from framework.navigator.mouse import Mouse
from framework.workflow import Workflow


@when(u'I complete a workflow as "{profile}"')
def step_impl(context, profile):

    workflow = Workflow(context, profile)
    workflow.complete()

    return
