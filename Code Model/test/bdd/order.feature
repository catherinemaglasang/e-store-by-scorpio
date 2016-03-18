Feature: Create and Get Order

  """ Sunny Case """
  Scenario: Get Order
    Given Order id '1' is in the system
    When I retrieve the order '1'
    Then I should get '200' response
    And the following orders information are returned:
    | customer_id | payment_id | transaction_date | shipping_date | time_stamp          | transaction_status | total |
    | 1           | 1          | 2016-03-11       | 2016-03-11    | 2016-03-11 11:49:17 | Pending            | 100.0 |

