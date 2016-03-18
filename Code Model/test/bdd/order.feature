Feature: Create and Get Order

  """ Sunny Case """
  Scenario: Get Order
    Given Order id '1' is in the system
    When I retrieve the order '1'
    Then I should get '200' response
    And the following orders information are returned:
    | customer_id | payment_id | transaction_date | shipping_date | time_stamp          | transaction_status | total |
    | 1           | 1          | 2016-03-11       | 2016-03-11    | 2016-03-11 11:49:17 | Pending            | 100.0 |


#  """ Rainy Case """
  Scenario: Get an order that doesn't exist
    Given I retrieve an order with resource url '/api/v1/orders/2/'
    When I retrieve a  JSON result
    Then I should get a '200' status code
    And It should  have a field "status" "ok"
    And It should  have a field "message" "No entries found"
    And It should  have a field "count" 0
    And It should  have an empty field " entries "