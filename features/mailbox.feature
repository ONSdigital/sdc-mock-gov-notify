Feature: Mailbox
  As a developer
  In order to test full user journeys
  I want to be able to emulate Gov Notify's email behaviour

  Scenario: Receiving an email
    Given an email is sent to Gov Notify to "matt@example.com"
    When I check the email inbox
    Then I should see 1 email sent to "matt@example.com"

  Scenario: Clear mailbox
    Given an email is sent to Gov Notify to "tom@example.com"
    When I clear the email inbox
    Then then there should be 0 emails in the inbox