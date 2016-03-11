Feature: Handle storing and retrieving supplier details

Scenario: Retrieve a supplier's details
  Given some suppliers are in a system
  When I retrieve the supplier '2'
  Then I should get a '200' response
  And the following supplier details are returned:
  | id | name  | address | phone | fax | email           | is_active |
  | 2  | sup2  | iligan  | 2     | 2   | sup2@estore.com | True      |