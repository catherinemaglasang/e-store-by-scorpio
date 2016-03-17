Feature: Handle storing and retrieving cart details


  """ Sunny Case """
  Scenario: Get cart detail
  Given cart detail '1' is in the system
  When I retrieve the cart detail '1'
  Then I should get a '200' response
  And the following cart details are returned:
  | cart_id | product_id | quantity   | time_stamp         |
  | 1       | 1          | 1         | 2016-03-15 11:49:17|