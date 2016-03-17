Feature: Handle storing, retrieving and deleting product details

  Scenario: Retrieve a wishlist's details
    Given some wishlists are in a system
    When I retrieve the wishlist '1'
    Then I should get a '200' response
    And the following product details are returned:
      | id | 
      | 1 |