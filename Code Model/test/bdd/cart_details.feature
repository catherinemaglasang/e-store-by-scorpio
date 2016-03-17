Feature: Handle storing and retrieving cart details


  """ Sunny Case """
  Scenario: Get cart detail
    Given cart detail '1' is in the system
    When I retrieve the cart detail '1'
    Then I should get a '200' response
    And the following cart details are returned:
      | cart_id | product_id | quantity   | time_stamp         |
      | 1       | 1          | 1          | 2016-03-15 11:49:17|


#  """ Rainy Case """
  Scenario: Get cart detail that doesn't exist
    Given I retrieve a cart detail with resource url '/api/v1/cart_details/2/'
    When i retrieve JSON result
    Then i should get a status code '200'
    And it should have a field "status" "ok"
    And it should have a field "message" "No entries found"
    And it should have a field "count" 0
    And it should have an empty field " entries "