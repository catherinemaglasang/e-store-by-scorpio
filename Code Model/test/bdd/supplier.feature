Feature: Create, Get and Update supplier details

#  Create Sunny Case
   Scenario: Create Supplier
      Given I have the following supplier details
      | id | name        | address  | phone   | fax         | email                | is_active |
      | 6  | supplier1   | address1 | 221-2277| 063-221-2277| supplier1@estore.com | True      |
      When I Post the supplier to resource_url  '/api/v1/suppliers/'
      Then I should get a response '200'
      And I should get a "status" containing 'ok'
      And I should get a "message" containing 'OK'

#   Create Rainy Case
   Scenario: Create duplicate supplier
     Given I have the following supplier details
       | id | name        | address  | phone   | fax         | email                | is_active |
       | 3  | supplier1   | address1 | 221-2277| 063-221-2277| supplier1@estore.com | True      |
     When I Post the supplier to resource_url  '/api/v1/suppliers/'
     Then I should get a response '200'
     And I should get a "status" containing 'ok'
     And I should get a "message" containing 'SUPPLIER EXISTS'

#  Get Sunny Case
  Scenario: Get a supplier
    Given supplier '1' is in the system
    When I retrieve the supplier '1'
    Then I should get a response '200'
    And the following supplier details are returned:
    | id | name     | address  | phone   | fax         | email                | is_active |
    | 1  | supplier1| address1 | 221-2277| 063-221-2277| supplier1@estore.com | True      |

#  Get Rainy Case
  Scenario: Get a supplier that doesn't exist
    Given I retrieve a supplier with resource url '/api/v1/suppliers/4/'
    When I get the JSON result
    Then I should get a response '200'
    And I should get a "status" containing 'ok'
    And It should have a field "message" 'No entries found'
    And It should have a field "count" 0
    And It should have an empty field "entries"

#  Scenario: Update Supplier
#    Given the supplier id 1 is in the database with the following details
#    | id | name     | address  | phone   | fax         | email                | is_active |
#    | 1  | supplier1| address1 | 221-2277| 063-221-2277| supplier1@estore.com | True      |
#    And the new supplier details for supplier id 1
#    | id | name     | address  | phone   | fax          | email                | is_active |
#    | 1  | supplier1| address1 | 221-2222| 063-221-2222 | supplier1@estore.com | True      |
#    When I send a PUT request to the supplier resource url 'api/v1/suppliers/1/'
#    Then I should get a response '200'
#    And I should get a "status" containing "ok"
