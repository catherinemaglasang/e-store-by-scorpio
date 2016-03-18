Feature: Create, Get, Delete and Update Cart

  """ Sunny Case """
  Scenario: Get cart
    Given cart '1' is in the system
    When I retrieve the cart '1'
    Then I should get a '200' response
    And the following details are returned :
      | session_id | date_created| customer_id| is_active |
      | 1          | 2016-03-15  | 1          | True      |