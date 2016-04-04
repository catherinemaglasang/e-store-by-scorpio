Feature: Get, Create & Update Products
  In order to track inventory and stocks,
  I want to create, update and get any product

  """ Test the behavior of all endpoints when we make a GET request """

  Scenario Outline: Retrieve resource
    Given I access the url "<url>"
    Then I get a "<status_code>" response
    And I get an "<status>" status
    And I get an "<message>" message

    Examples:
      | url              | status_code | status | message |
      | /                | 200         | ok     | ok      |
      | /api/v1/items/   | 200         | ok     | ok      |
      | /api/v1/items/1/ | 200         | ok     | ok      |

  """ Test the behavior when we make a POST request"""
  Scenario: Add Site
    Given I have the following data
      | owner_id | name | business_code | domain |
      | 1        | test | test          | test   |
    When I POST to the url "/api/v1/sites/"
    Then I get a "201" response
    And I get a field "status" containing "ok"
    And I get a field "message" containing "ok"

  Scenario: Add Item
    Given I have the following data
      | item_id | site_id | serial_no | tax_class_id | type_id | name  | description | date_added     | date_updated   | is_taxable | unit_cost | is_active | has_variations |
      | 1       | 1       | SN0142    | 1            | 1       | Apple | Apple Item  | 1/1/1 00:00:00 | 1/1/1 00:00:00 | true       | 10.01     | true      | true           |
    When I POST to the url "/api/v1/items/"
    Then I get a "201" response
    And I get a field "status" containing "ok"
    And I get a field "message" containing "ok"

#    Scenario: Add Product Type
#      Given I have the following data
#      | name      | description |
#      | Book      | Book Desc   |
#      When I POST to the url "/api/v1/producttypes/"
#      Then I get a "201" response
#      And I get a field "status" containing "ok"
#      And I get a field "message" containing "ok"
#
#    Scenario: Add Category
#      Given I have the following data
#      | name  | description | image         |
#      | 1     | 1           | 1             |
#      When I POST to the url "/api/v1/categories/"
#      Then I get a "201" response
#      And I get a field "status" containing "ok"
#      And I get a field "message" containing "ok"
#
#      Scenario: Add Attributes for Product Type
#      Given I have the following data
#        | product_type_id | name | code | type    | is_required |
#        | 1               | Book | P1   | string  | true      |
#      When I POST to the url "/api/v1/producttypes/1/attributes/"
#      Then I get a "201" response
#      And I get a field "status" containing "ok"
#      And I get a field "message" containing "ok"

  """ Test the behavior when we make a PUT request"""
#    Scenario: Update Product Type
#      Given I have a resource with the id "1"
#      And I want to update its data to the following data
#      | product_type_id | name     | description |
#      | 1               | New      | New          |
#      And I have the resource url "/api/v1/producttypes/1/"
#      When I send a PUT request from client
#      Then I get a "200" response
#      And I get a field "status" containing "ok"
#      And I get a field "message" containing "ok"

#    Scenario: Update Item
#      Given I have a resource with the id "1"
#      And I want to update its data to the following data
#      | item_id | site_id | serial_no | tax_class_id | type_id | name | description | date_added | date_updated | is_taxable | unit_cost | is_active | has_variations |
#      | 1    | 1    | SN0142      | 1       | 1    | Apple | Apple Item | 1/1/1 00:00:00       | 1/1/1 00:00:00         | true       | 10.01     | true      | true           |
#      And I have the resource url "/api/v1/items/1/"
#      When I send a PUT request from client
#      Then I get a "200" response
#      And I get a field "status" containing "ok"
#      And I get a field "message" containing "ok"
#
#    Scenario: Update Category
#      Given I have a resource with the id "1"
#      And I want to update its data to the following data
#      | category_id |  name | description | image       |
#      | 1           | 1     | 1           | 1           |
#      And I have the resource url "/api/v1/categories/1/"
#      When I send a PUT request from client
#      Then I get a "200" response
#      And I get a field "status" containing "ok"
#      And I get a field "message" containing "ok"
#
#    Scenario: Update Product Attribute
#      Given I have a resource with the id "1"
#      And I want to update its data to the following data
#      | product_attribute_id  |  name        | code         | type          | is_required |
#      | 1                     | New name     | New Code     | new type      | true         |
#      And I have the resource url "/api/v1/producttypes/1/attributes/1/"
#      When I send a PUT request from client
#      Then I get a "200" response
#      And I get a field "status" containing "ok"
#      And I get a field "message" containing "ok"


  """ Test the behaviour during forms submission in client """