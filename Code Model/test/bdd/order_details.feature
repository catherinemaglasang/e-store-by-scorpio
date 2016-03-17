Feature: Handle storing and retrieving order details
  Scenario: Retrieve an order detail
    Given order detail id '1' is filled
    When I retrieve the order detail '1'
    Then I should get a '200' response
    And the following user details are returned:
    | id | order_id | product_id | unit_price | discount | quantity |
    | 1  | 1 | 1 | 100.0 | 0.1 | 20 |

  Scenario: Retrieving an order detail not inside the database
    Given order detail id '2' is not filled
    When I retrieve the order detail '2'
    Then I should get a '500' response