Feature: Handle storing and retrieving order details
  Scenario: Retrieve an order details
    Given some order details are in the system
    When I retrieve the order detail '1'
    Then I should get a '200' response
    And the following user details are returned:
    | id | order_id | product_id | unit_price | discount | quantity |
    | 1  | 1 | 1 | 100.0 | 0.1 | 20 |

  Scenario: Retrieve an order details not inside the database
    Given some order details are in the system
    When I retrieve the order detail '2'
    Then I should get a '500' response