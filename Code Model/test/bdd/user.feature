Feature: Handle storing and retrieving customer details
  Scenario: Retrieve a user detail
    Given user id '1' is in the system
    When I retrieve the user '1'
    Then I should get a '200' response
    And the following user details are returned:
    | id | username | password | is_admin |
    | 1  | user1 | pass1 | True |


  Scenario: Retrieving a user detail not inside the database
    Given user id '2' is not in the system
    When I retrieve the user '2'
    Then I should get a '500' response