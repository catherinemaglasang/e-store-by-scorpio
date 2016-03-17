Feature: Handle storing and retrieving supplier details

  Scenario: Get supplier
    Given supplier '1' is in the system
    When I retrieve the supplier '1'
    Then I should get a '200' response
    And the following supplier details are returned:
    | id | name     | address  | phone   | fax         | email                | is_active |
    | 1  | supplier1| address1 | 221-2277| 063-221-2277| supplier1@estore.com | True      |


    Scenario: Create Suppler
      Given I am at the add supplier page with url  '/api/v1/suppliers/'
      When I add new supplier '3' 'supplier3' 'address3' '221-2233' '063-221-2233' 'supplier3@estore.com' 'True'
      #| id | name        | address  | phone   | fax         | email                | is_active |
      #| 1  | supplier1   | address1 | 221-2277| 063-221-2277| supplier1@estore.com | True      |
#      Then I should get a '200' response
      And it will return the following
      | status | message   |
	  | ok     |           |

