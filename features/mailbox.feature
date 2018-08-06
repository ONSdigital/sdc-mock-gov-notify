Feature: Mailbox
  As a developer
  In order to test full user journeys
  I want to be able to emulate Gov Notify's email behaviour

  Scenario: Check all emails
    Given an email is sent to Gov Notify to "matt@example.com"
    And an email is sent to Gov Notify to "tom@example.com"
    When I check the global email inbox
    Then I should see 2 email sent to "matt@example.com"

  Scenario: Check personal email
    Given an email is sent to Gov Notify to "tom@example.com"
    And an email is sent to Gov Notify to "matt@example.com"
    And an email is sent to Gov Notify to "tom@example.com"
    When I check the email inbox for "tom@example.com"
    Then I should see 2 email sent to "tom@example.com"

  Scenario: Clear mailbox
    Given an email is sent to Gov Notify to "tom@example.com"
    When I clear the email inbox
    Then there should be no emails in the inbox

