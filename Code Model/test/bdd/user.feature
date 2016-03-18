Feature: Handle storing and retrieving customer details
  Scenario: Get User
    Given user id '1' is in the system
    When I retrieve the user '1'
    Then I get the '200' response
    And the following user details are shown:
    | id | username | password | is_admin |
    | 1  | user1 | pass1 | True |


  Scenario: Get User not in the Database
    Given I access the user url '/api/v1/users/2/'
    When I retrieve the user JSON result
    Then I get the '200' response
    And it should have a user field 'status' containing 'ok'
    And it should have a user field 'message' containing 'No entries found'
    And it should have a user field 'count' containing '0'
    And it should have an empty field 'entries'
