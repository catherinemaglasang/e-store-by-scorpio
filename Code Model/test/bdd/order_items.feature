Feature: Create and get order item


#  Create Sunny Case
  Scenario: Create order item
    Given I have the following order item details
    | id | order_id | product_id | unit_price | discount | quantity |
    | 1  | 1        | 1          | 100.0      | 0.1      | 20       |
    When I Post the order item to resource_url  '/api/v1/order_items/'
    Then I should have a response '200'
    And I should have a "status" containing "ok"
    And I should have a "message" containing "ok"

#  Create Rainy Case
  Scenario: Create a duplicate order item
    Given I have already added the following order item details:
     | id | order_id | product_id | unit_price | discount | quantity |
     | 1  | 1        | 1          | 100.0      | 0.1      | 20       |
    When I Post the order item to resource_url  '/api/v1/order_items/'
    Then I should have a response '200'
    And I should have a "status" containing "ok"
    And I should get a field message containing "id exists"


#  Get Sunny Case
  Scenario: Get an order item
    Given order item id '1' is in the system
    When I retrieve the order item '1'
    Then I should have a response '200'
    And the following order item details are returned:
    | id | order_id | product_id | unit_price | discount | quantity |
    | 1  | 1        | 1          | 100.0      | 0.1      | 20       |

#   Get Rainy Case
  Scenario: Get an order item that doesn't exist
    Given I retrieve an order item with resource url '/api/v1/orders/2/'
    When I retrieve the JSON result
    Then I should have a response '200'
    And I should have a "status" containing "ok"
    And It should have a field "message " "No entries found"
    And It should have a field "count " 0
    And It should have an empty field " entries "