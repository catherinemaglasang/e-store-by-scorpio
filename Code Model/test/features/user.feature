Feature: Handle storing, retrieving and deleting customer details
  Scenario: Retrieve a customers details
    Given some users are in the system
    When I retrieve the user '1'
    Then I should get a '200' response
    And the following user details are returned:
    | user_id | username | password | is_admin |
    | 1 | king | test | true |