Feature: Create, Get and Update supplier details

   Scenario: Create Supplier
      Given I have the following supplier details
      | id | name        | address  | phone   | fax         | email                | is_active |
      | 1  | supplier1   | address1 | 221-2277| 063-221-2277| supplier1@estore.com | True      |
      When I Post the supplier to resource_url  '/api/v1/suppliers/'
      Then I should get a response '201'
       And I should get a "status" containing "ok"
       And I should get a "message" containing "ok"

  """ Sunny Case """
  Scenario: Get a supplier
    Given supplier '1' is in the system
    When I retrieve the supplier '1'
    Then I should get a '200' response
    And the following supplier details are returned:
    | id | name     | address  | phone   | fax         | email                | is_active |
    | 1  | supplier1| address1 | 221-2277| 063-221-2277| supplier1@estore.com | True      |

  """ Rainy Case """
  Scenario: Get a supplier that doesn't exist
    Given I retrieve a supplier with resource url '/api/v1/suppliers/2/'
    When I retrieve the JSON result
    Then I should get a status code '200'
    And It should have a field "status" "ok"
    And It should have a field "message" "No entries found"
    And It should have a field "count" 0
    And It should have an empty field "entries"

