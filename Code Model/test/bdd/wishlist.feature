Feature: Get Wishlist



  Scenario: Get Wishlist - sunny case
    Given wishlist '1' is in the system
    When I retrieve the wishlist '1'
    Then I should have a status code response '200'
    And the following details are returned :
      |id |
      | 1 |  


  Scenario: Get a wishlist that doesn't exist - rainy case
    Given I retrieve a wishlist with id '2'
    When I retrieve the JSON result
    Then I should have a status code response '200'
    And I should get the status says 'ok'
    And it should  have a field message saying 'No entries found'
    And it should  have a field count '0'
    And it should  have an empty field 'entries'

