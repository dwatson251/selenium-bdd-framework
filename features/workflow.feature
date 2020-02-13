Feature: Workflow

    Scenario: Login
        Given We are on the "login" page
        When I enter credentials as "columba_tinklee.client"
        Then I see "My Details"

    Scenario: Complete Workflow
        Given We are on the "home" page
        When I complete a workflow as "columba_tinklee.client"
        Then I should see "My Details"