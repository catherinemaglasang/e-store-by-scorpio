Feature: Get, Create & Update Category

  Scenario: Add Category
    Given I have the following data
      | name | description | image |
      | 1    | 1           | 1     |
    When I POST to the url "/api/v1/categories/"
    Then I get a "201" response
    And I get a field "status" containing "ok"
    And I get a field "message" containing "ok"

  Scenario: Update Category
    Given I have a resource with the id "1"
    And I want to update its data to the following data
      | category_id | name | description | image |
      | 1           | 1    | 1           | 1     |
    And I have the resource url "/api/v1/categories/1/"
    When I send a PUT request from client
    Then I get a "200" response
    And I get a field "status" containing "ok"
    And I get a field "message" containing "ok"