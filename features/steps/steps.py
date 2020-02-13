"""
This file contains all imports containing the step definition classes/ files the behave tests needs to run.

Despite IDE's reporting unused imports, these are very much required by behave, and tests will fail if these
are removed.
"""
import step_definitions.common.forms
import step_definitions.common.inspection
import step_definitions.common.navigation
import step_definitions.common.modal
import step_definitions.common.workflow

import step_definitions.authentication.login
import step_definitions.authentication.signup
import step_definitions.authentication.otp
import step_definitions.authentication.privacy_policy
