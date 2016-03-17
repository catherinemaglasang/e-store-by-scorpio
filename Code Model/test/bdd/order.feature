Feature: Handle Creating and Retrieving Order information

  Scenario: Get Order Information
    Given some Orders are in the system
    When I retrieve the order '1'
    Then I should get a '200' response
    And the following orders information are returned:
    | id | customer_id | payment_id | transaction_date | shipping_date | time_stamp | transaction_status | total |
    | 1 | 1 | 1 | 2016-03-11 | 2016-03-11 | 2016-03-11 11:49:17 | Pending | 100.0 |

  Scenario: Get Order Information not in the database
    Given some Orders are in the system
    When I retrieve the order '2'
    Then I should get a '500' response
    | 3 | 8123 | 1239 | 2016-07-20 00:00:00 | 2016-08-15 00:00:00 | 2016-12-25 00:00:00 | blank | 121.99 |
