Feature: Handle storing and retrieving supplier details

Scenario: Get category
  Given some categories are in a system
  When I retrieve the supplier '1'
  Then I should get a '200' response
  And the following category details are returned:
  | id | name  | description | main_image | parent_category_id | is_active|
  | 3  | pro gear | signature team gear | team gear.jpg | 1 | True |