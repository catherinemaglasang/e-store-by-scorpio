Feature: Get product details
  As an admin
  I want to get a product's details

  Scenario: Admin retrieves a product successfully
    Given product id 1 is an existing product
    When I try to get the details for product id 1
    Then i get a 200 response
    And the following product details are returned:
      | category_id | date_added | description | is_active | on_hand | ordering | product_id | product_type_id | re_order_level | site_id | supplier_id | title |
      | 1           | Tue, 15 Mar 2016 18:40:08 GMT | NEW  Product Description | true | 100 | 0 | 1         | 1               | 10             | 1       | 1           | NEWNEW Product Name |
