Feature: Create and Get Order

#  Create Sunny Case
  Scenario: Create order
    Given I have the following order details
    |id| customer_id | payment_id | transaction_date | shipping_date | time_stamp          | transaction_status | total |
    |4 | 3           | 3          | 2016-03-11       | 2016-03-11    | 2016-03-11 11:49:17 | Pending            | 100.0 |
    When I Post the order to resource_url  '/api/v1/orders/'
    Then I should get a status of '200'
    And I should get a "status" 'ok'
    And I should get a "message" 'OK'

#  Create Rainy Case
  Scenario: Create a duplicate order
    Given I have the following order details
     |id| customer_id | payment_id | transaction_date | shipping_date | time_stamp          | transaction_status | total |
     |1 | 1           | 1          | 2016-03-11       | 2016-03-11    | 2016-03-11 11:49:17 | Pending            | 100.0 |
    When I Post the order to resource_url  '/api/v1/orders/'
    Then I should get a status of '200'
    And I should get a "status" 'ok'
    And I should get a "message" 'ID EXISTS'


#  Get Sunny Case
  Scenario: Get Order
    Given Order id '1' is in the system
    When I retrieve the order '1'
    Then I should get a status of '200'
    And the following orders are returned:
    | customer_id | payment_id | transaction_date | shipping_date | time_stamp          | transaction_status | total |
    | 1           | 1          | 2016-03-11       | 2016-03-11    | 2016-03-11 11:49:17 | Pending            | 100.0 |


#  Get Order Rainy Case
  Scenario: Get an order that doesn't exist
    Given I retrieve the order '2'
    When I retrieve a  JSON result
    Then I should get a status of '200'
    And I should get a "status" 'ok'
    And It should  have a "message" "No entries found"
    And It should  have a field "count" 0
    And It should  have an empty field " entries "


#  Scenario: Update order
#   Given the order id 1 is in the database with the following details:
#     |id| customer_id | payment_id | transaction_date | shipping_date | time_stamp          | transaction_status | total |
#     |1 | 1           | 1          | 2016-03-11       | 2016-03-11    | 2016-03-11 11:49:17 | Pending            | 100.0 |
#    And the new order details for order id 1:
#     |id| customer_id | payment_id | transaction_date | shipping_date | time_stamp          | transaction_status | total |
#     |1 | 1           | 1          | 2016-03-11       | 2016-03-11    | 2016-03-11 11:49:17 | Pending            | 100.0 |
#    When I send a PUT request to the order resource url 'api/v1/orders/1/'
#    Then I should get a 200 response in the update request
#    And I should get a field for "status" containing "ok" for update request