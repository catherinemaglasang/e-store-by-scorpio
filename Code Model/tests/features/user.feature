Feature: Handle storing, retrieving and deleting customer details
  Scenario: Retrieve a user details
    Given some users are in the system
    When I retrieve the user '2'
    Then I should get a '200' response
    And the following user details are returned:
    | id | username | password | is_admin |
    | 2  | rebel | test2 | True |