Feature: Handle storing and retrieving customer details
  Scenario: Retrieve a user detail
    Given user id '1' is in the system
    When I retrieve the user '1'
    Then I get '200' response
    And the following user details are shown:
    | id | username | password | is_admin |
    | 1  | user1 | pass1 | True |


  Scenario: Retrieving a user detail not inside the database
    Given I access the url '/api/v1/users/13/'
    When I retrieve the JSON results
    Then I get '200' response
    And it should have a field 'status' containing 'ok'
    And it should have a field 'message' containing 'no entries found'
    And it should have a field 'count' containing '0'
    And it should have an empty field 'entries'
