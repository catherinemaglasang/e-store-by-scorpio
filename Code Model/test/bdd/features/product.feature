Feature: Get, Create & Update Products
  In order to track inventory and stocks,
  I want to create, update and get any product

  Scenario Outline: Check api status
    Given I access the url <url>
    Then I get a <status_code> response
    And I get an <status> status
    And I get an <message> message
    Examples:
    | url                     | status_code | status | message |
    | /                       | 200         | ok     | ok      |
    | /api/v1/products/       | 200         | ok     | ok      |
    | /api/v1/products/1/     | 200         | ok     | ok      |
    | /api/v1/producttypes/   | 200         | ok     | ok      |
    | /api/v1/producttypes/1/ | 200         | ok     | ok      |

#  Scenario Outline: Add product
#    Given I have a <product_id>, <title>, <description>, <supplier_id>, <category_id>, <site_id>, <product_type_id>, <on_hand>, <re_order_level>
#
#    Examples:
#      | product_id | title | description | supplier_id | category_id | site_id | product_type_id | on_hand | re_order_level |
#      | 1          | title | desc        | 1           | 1           | 1       | 1               | 100     | 10             |



#  Scenario: Admin retrieves a product successfully
#    Given product id 1 is an existing product
#    When I try to get the details for product id 1
#    Then i get a 200 response
#    And the following product details are returned:
#      | category_id | date_added | description | is_active | on_hand | ordering | product_id | product_type_id | re_order_level | site_id | supplier_id | title |
#      | 1           | Tue, 15 Mar 2016 18:40:08 GMT | NEW  Product Description | true | 100 | 0 | 1         | 1               | 10             | 1       | 1           | NEWNEW Product Name |
#
#  Scenario: Get a product that doesn't exist
#    Given I access the resource url '/api/v1/products/2/'
#    When I retrieve the JSON results
#    Then the status code should be 200
#    And it should have a field "status" containing "ok"
#    And it should have a field "message" containing "No entries found"
#    And it should have a field "count" containing 0
#    And it should have an empty field "entries"
#
#  Scenario: Create a new product
#    Given I have the following product details:
#      | category_id | date_added | description | is_active | on_hand | ordering | product_id | product_type_id | re_order_level | site_id | supplier_id | title |
#      | 1           | Tue, 15 Mar 2016 18:40:08 GMT | NEW  Product Description | true | 100 | 0 | 99        | 1               | 10             | 1       | 1           | NEWNEW Product Name |
#    When I POST to the product resource url '/api/v1/products/'
#    Then I should get a 201 response
#    And I should get a field "status" containing "ok"
#    And I should get a field "message" containing "ok"
#
#  Scenario: Create a duplicate product
#    Given I have already added the product details:
#      | category_id | date_added | description | is_active | on_hand | ordering | product_id | product_type_id | re_order_level | site_id | supplier_id | title |
#      | 1           | Tue, 15 Mar 2016 18:40:08 GMT | NEW  Product Description | true | 100 | 0 | 99        | 1               | 10             | 1       | 1           | NEWNEW Product Name |
#    When I POST to the product resource url '/api/v1/products/'
#    Then I should get a 201 response
#    And I should get a field "status" containing "ok"
#    And I should get a field "message" containing "id exists"
#
#  Scenario: Get newly created product
#    Given the new product id 99 details that i recently added:
#      | category_id | date_added | description | is_active | on_hand | ordering | product_id | product_type_id | re_order_level | site_id | supplier_id | title |
#      | 1           | Tue, 15 Mar 2016 18:40:08 GMT | NEW  Product Description | true | 100 | 0 | 99        | 1               | 10             | 1       | 1           | NEWNEW Product Name |
#    When I access to the product resource url '/api/v1/products/99/' to get the new product id 99
#    Then I should get a 200 response in product id 99 resource
#    And I should receive a field "status" containing "ok" in product id 99 json response
#    And I should receive a field "message" containing "ok" in product id 99 json response
#    And I should get a length of 1 in entries of product id 99 json response
#    And I should get an entry with a product id 99
#
#  Scenario: Update a product
#    Given the new product id 99 in database with the following details:
#      | category_id | date_added | description | is_active | on_hand | ordering | product_id | product_type_id | re_order_level | site_id | supplier_id | title |
#      | 1           | Tue, 15 Mar 2016 18:40:08 GMT | NEW  Product Description | true | 100 | 0 | 99        | 1               | 10             | 1       | 1           | NEWNEW Product Name |
#    And the new product details for product id 99:
#      | category_id | date_added | description | is_active | on_hand | ordering | product_id | product_type_id | re_order_level | site_id | supplier_id | title |
#      | 1           | Tue, 15 Mar 2016 18:40:08 GMT | New formal product description | true | 100 | 0 | 99        | 1               | 10             | 1       | 1           | Formal new product name |
#    When I send a PUT request to the product resource url 'api/v1/products/99/'
#    Then I should get a 200 response in the update request
#    And I should get a field for "status" containing "ok" for update request

#  Scenario: Get updated product
#    Given the updated product id 99 in database with the following new details:
#      | category_id | date_added | description | is_active | on_hand | ordering | product_id | product_type_id | re_order_level | site_id | supplier_id | title |
#      | 1           | Tue, 15 Mar 2016 18:40:08 GMT | New formal product description | true | 100 | 0 | 99        | 1               | 10             | 1       | 1           | Formal new product name |
#    And the updated product's old details are the following:
#      | category_id | date_added | description | is_active | on_hand | ordering | product_id | product_type_id | re_order_level | site_id | supplier_id | title |
#      | 1           | Tue, 15 Mar 2016 18:40:08 GMT | NEW  Product Description | true | 100 | 0 | 99        | 1               | 10             | 1       | 1           | NEWNEW Product Name |
#    When I request the product id's resource url '/api/v1/products/99/'
#    Then i should get an entries field with the new product details.