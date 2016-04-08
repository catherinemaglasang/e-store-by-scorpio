Feature: Get, Create & Update Wishlist Item

  Background:
    Given a resource url called "/api/v1/wishlists/1/items/"

  Scenario Outline: Retrieve resource
    Given I access the url "<url>"
    Then I get a "<status_code>" response
    And I get an "<status>" status
    And I get an "<message>" message

    Examples:
      | url                          | status_code | status | message |
      | /                            | 200         | ok     | ok      |
      | /api/v1/wishlists/1/items/   | 200         | ok     | ok      |
      | /api/v1/wishlists/1/items/1/ | 200         | ok     | ok      |

  Scenario: Add Wishlist Item
    Given I have the following data
      | wishlist_item_id | wishlist_id | item_id | time_stamp  |
      | 1                | 1           | 1       | 1/1/1 1:1:1 |
    When I save the data
    Then I get a "201" response
    And I get a field "status" containing "ok"
    And I get a field "message" containing "ok"

  Scenario: Update Wishlist Item
    Given I have a resource with the id "1"
    And I want to update its data to the following data
      | wishlist_item_id | wishlist_id | item_id | time_stamp  |
      | 1                | 1           | 1       | 1/1/1 1:1:1 |
    When I update the data
    Then I get a "200" response
    And I get a field "status" containing "ok"
    And I get a field "message" containing "ok"
