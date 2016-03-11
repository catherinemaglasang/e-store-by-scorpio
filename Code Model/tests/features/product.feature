Feature: Handle storing, retrieving and deleting product details

  Scenario: Retrieve a product's details
    Given some products are in a system
    When I retrieve the product '1'
    Then I should get a '200' response
    And the following product details are returned:
      | id | sku | supplier_id | title | description | category_id | unit_price | on_hand | re_order_level | is_active |
      | 1 | 123 | 1            | Patata | Baked Potato | 1 | 10.0 | 100 | 10 | True |

