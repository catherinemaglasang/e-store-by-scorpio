Feature: Get category details
  As an admin
  I want to get a category's details

  Scenario: Admin gets a category successfully
    Given category id 1 is an existing category
    When I try to get the details for category id 1
    Then the following category details are returned:
      | id | name | description | main_image | is_active | parent_category_id |
      | 1 | category1 | description1 | "static/image1.jpeg" | True | main1|
