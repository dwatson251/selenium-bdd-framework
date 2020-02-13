Feature: Registration

    Scenario: Register (With OTP)
        Given We are on the "register" page
        When I sign up as "columba_tinklee.client"
        Then I see "We've sent you a One Time Passcode"
        When I enter the OTP as "columba_tinklee.client"
        Then I see "Passcode successfully verified"
        Then I see "Privacy Policy & Terms and Conditions"

    Scenario: Accept Terms and Conditions
        Given We are on the "privacy-policy" page
        When I agree to the terms and conditions
        Then I see "My Details"

    Scenario: Logout
        Given we are on any page
        When I click "nav-logout"
        Then I should see "Workflow is not completed"
        When I confirm modal
        Then I should be taken to the "Login" page
