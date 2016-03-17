Feature: Handle storing and retrieving cart

Scenario: Get carts
  Given some carts are in a system
  When I retrieve the cart '1'
  Then I should get a '200' response
  And the following cart details are returned:
  | id | session_id | date_created| customer_id| is_active |
  | 1  | 1          | 2016-03-15  | 1          | True      |