Feature: Handle storing and retrieving customer details
  Scenario: Retrieve a user details
    Given some users are in the system
    When I retrieve the user '1'
    Then I should get a '200' response
    And the following user details are returned:
    | id | username | password | is_admin |
    | 1  | user1 | pass1 | True |


  Scenario: Retrieve a user details not inside the database
    Given some users are in the system
    When I retrieve the user '2'
    Then I should get a '500' response