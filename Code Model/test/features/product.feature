Feature: Handle storing, retrieving and deleting product details

Scenario: Retrieve a product's details
Given some products are in a system
When I retrieve the product '1'
Then I should get a '200' response
And the following product details are returned:
| id | sku | title | description | unit_price | category_id | on_hand | re_order_level | is_active
| 1 | 123 | Patata | Baked Potato | 10 | 1 | 100 | 10 | true |