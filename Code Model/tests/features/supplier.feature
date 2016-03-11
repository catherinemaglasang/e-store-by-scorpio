Feature: Handle storing and retrieving supplier details

Scenario: Retrieve a supplier's details
  Given some suppliers are in a system
  When I retrieve the supplier '1'
  Then I should get a '200' response
  And the following supplier details are returned:
  | id | name  | address | phone    | fax      | email           | is_active |
  | 1  | sup1  | iligan  | 221-9999 | 222-2288 | sup1@estore.com | true      |