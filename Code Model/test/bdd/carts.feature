Feature: Create, Get, Delete and Update Cart

  """ Sunny Case """
  Scenario: Get cart
    Given cart '1' is in the system
    When I retrieve the cart '1'
    Then I should get a '200' response
    And the following details are returned :
      | session_id | date_created| customer_id| is_active |
      | 1          | 2016-03-15  | 1          | True      |


#  """ Rainy Case """
  Scenario: Get a cart that doesn't exist
    Given I retrieve a cart with resource url '/api/v1/carts/2/'
    When i retrieve a JSON result
    Then i should get a '200' status code
    And it should  have a field "status" "ok"
    And it should  have a field "message" "No entries found"
    And it should  have a field "count" 0
    And it should  have an empty field " entries "