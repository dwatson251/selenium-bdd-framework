Feature: Login Form

    Scenario: Unsuccessful Login
        Given We are on the "login" page
        When I enter credentials as "non_existent.client"
        Then I see "Incorrect username or password"