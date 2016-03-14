Feature: Handle Creating and Retrieving Order information

  Scenario: Get Order Information
    Given some Orders are in the system
    When I retrieve the order '3'
    Then I should get a '200' response
    And the following orders information are returned:
    | id | customer_id | payment_id | transaction_date | shipping_date | time_stamp | transaction_status | total |
    | 3 | 8123 | 1239 | 2016-07-20 00:00:00 | 2016-08-15 00:00:00 | 2016-12-25 00:00:00 | blank | 121.99 |