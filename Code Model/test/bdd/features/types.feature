Feature: Get, Create & Update Types

  Background:
    Given a resource url called "/api/v1/types/"

  Scenario Outline: Retrieve resource
    Given I access the url "<url>"
    Then I get a "<status_code>" response
    And I get an "<status>" status
    And I get an "<message>" message

    Examples:
      | url                           | status_code | status | message |
      | /                             | 200         | ok     | ok      |
      | /api/v1/types/1/              | 200         | ok     | ok      |
      | /api/v1/types/2/attributes/1/ | 200         | ok     | No entries found      |

  Scenario: Add Type
    Given I have the following data
      | type_name | type_description |
      | name      | description      |
    When I save the data
    Then I get a "201" response
    And I get a field "status" containing "ok"
    And I get a field "message" containing "ok"

  Scenario: Update Type
      Given I have a resource with the id "1"
      And I want to update its data to the following data
      | type_name | type_description |
      | name      | description      |
      When I update the data
      Then I get a "200" response
      And I get a field "status" containing "ok"
      And I get a field "message" containing "ok"
