Feature: Create and get order item

  """ Sunny Case """
  Scenario: Get an order item
    Given order item id '1' is in the system
    When I retrieve the order item '1'
    Then i should get a status_code '200'
    And the following user details are returned:
    | id | order_id | product_id | unit_price | discount | quantity |
    | 1  | 1 | 1 | 100.0 | 0.1 | 20 |

#    """ Rainy Case """
  Scenario: Get an order item that doesn't exist
    Given I retrieve an order item with resource url '/api/v1/orders/2/'
    When I retrieve the JSON result
    Then I should get '200' status code
    And It should have a field "status " "ok"
    And It should have a field "message " "No entries found"
    And It should have a field "count " 0
    And It should have an empty field " entries "