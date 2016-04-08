Feature: Get and Create Wishlist



  Scenario: Get Wishlist - sunny case
    Given wishlist '1' is in the system
    When I retrieve the wishlist '1'
    Then I should have a status code response '200'
    And the following details are returned :
      |id |
      | 1 |  


  Scenario: Get a wishlist that doesn't exist - rainy case
    Given I retrieve a wishlist with id '2'
    When I retrieve the wishlist JSON result
    Then I should have a status code response '200'
    And I should get the status says 'ok'
    And it should  have a field message saying 'No entries found'
    And it should  have a field count '0'
    And it should  have an empty field 'entries'


  Scenario: Create Wishlist - sunny case
    Given I have the details of wishlist
    |id |
    | 1 |
    When I POST to url '/api/v1/wishlist/' the wishlist
    Then I should get '200' status code response
    And I should get 'ok' status
    And I should get 'ok' message


  Scenario: Create a duplicate wishlist - rainy case
    Given I have the details of wishlist
    |id |
    | 1 |
    When I POST to url '/api/v1/wishlist/' the wishlist
    Then I should get '200' status code response
    And I should get 'ok' status
    And I should get 'ID EXISTED' message



  

