Feature: Get, Create & Update Product Type

  Scenario: Add Product Type
    Given I have the following data
      | name | description |
      | Book | Book Desc   |
    When I POST to the url "/api/v1/producttypes/"
    Then I get a "201" response
    And I get a field "status" containing "ok"
    And I get a field "message" containing "ok"

  Scenario: Update Product Type
    Given I have a resource with the id "1"
    And I want to update its data to the following data
      | product_type_id | name | description |
      | 1               | New  | New         |
    And I have the resource url "/api/v1/producttypes/1/"
    When I send a PUT request from client
    Then I get a "200" response
    And I get a field "status" containing "ok"
    And I get a field "message" containing "ok"
