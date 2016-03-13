Feature: Get product details
  As an admin
  I want to get a product's details

  Scenario: Admin gets a product successfully
    Given product id 1 is an existing product
    When I try to get the details for product id 1
    Then the following product details are returned:
      | id | sku | supplier_id | title | description | category_id | unit_price | on_hand | re_order_level | is_active |
      | 1 | 123 | 1            | Patata | Baked Potato | 1 | 10.0 | 100 | 10 | True |
