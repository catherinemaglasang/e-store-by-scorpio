Feature: Handle storing and retrieving supplier details

Scenario: Get supplier
  Given some suppliers are in a system
  When I retrieve the supplier '1'
  Then I should get a '200' response
  And the following supplier details are returned:
  | id | name     | address  | phone   | fax         | email                | is_active |
  | 1  | supplier1| address1 | 221-2277| 063-221-2277| supplier1@estore.com | True      |