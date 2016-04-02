Feature: Get, Create & Update Attribute

  Scenario: Add Attributes for Product Type
    Given I have the following data
      | product_type_id | name | code | type   | is_required |
      | 1               | Book | P1   | string | true        |
    When I POST to the url "/api/v1/producttypes/1/attributes/"
    Then I get a "201" response
    And I get a field "status" containing "ok"
    And I get a field "message" containing "ok"

  Scenario: Update Attributes for Product Type
    Given I have a resource with the id "1"
    And I want to update its data to the following data
      | product_attribute_id | name     | code     | type     | is_required |
      | 1                    | New name | New Code | new type | true        |
    And I have the resource url "/api/v1/producttypes/1/attributes/1/"
    When I send a PUT request from client
    Then I get a "200" response
    And I get a field "status" containing "ok"
    And I get a field "message" containing "ok"