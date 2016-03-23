Feature: Get, Create & Update Products
  In order to track inventory and stocks,
  I want to create, update and get any product

  """ Test the behavior of all endpoints when we make a GET request """
  Scenario Outline: Retrieve resource
    Given I access the url "<url>"
    Then I get a "<status_code>" response
    And I get an "<status>" status
    And I get an "<message>" message

  Examples:
    | url                                   | status_code | status | message              |
    | /                                     | 200         | ok     | ok                   |
    | /api/v1/producttypes/                 | 200         | ok     | ok                   |
    | /api/v1/producttypes/1/               | 200         | ok     | ok                   |
    | /api/v1/producttypes/1/attributes/    | 200         | ok     | ok                   |
    | /api/v1/producttypes/1/attributes/1/  | 200         | ok     | ok                   |

    | /api/v1/categories/                   | 200         | ok     | ok                   |
    | /api/v1/categories/1/                 | 200         | ok     | ok                   |

    | /api/v1/products/                     | 200         | ok     | ok                   |
    | /api/v1/products/1/                   | 200         | ok     | ok                   |
    | /api/v1/products/1/categories/        | 200         | ok     | ok                   |
    | /api/v1/products/1/categories/1/      | 200         | ok     | ok                   |
    | /api/v1/products/1/attributes/        | 200         | ok     | ok                   |
    | /api/v1/products/1/attributes/1/      | 200         | ok     | ok                   |
    | /api/v1/products/1/images/            | 200         | ok     | ok                   |
    | /api/v1/products/1/images/1/          | 200         | ok     | ok                   |
#    | /api/v1/products/1/stocks/            | 200         | ok     | ok                   |
#    | /api/v1/products/1/stocks/1/          | 200         | ok     | ok                   |

    | /api/v1/products/1909/                | 200         | ok     | No entries found     |
    | /api/v1/producttypes/1909/            | 200         | ok     | No entries found     |
    | /api/v1/categories/1909/              | 200         | ok     | No entries found     |

    | /api/v1/products/1/categories/999/      | 200         | ok     | No entries found                   |
    | /api/v1/products/1/attributes/999/      | 200         | ok     | No entries found                   |
    | /api/v1/products/1/images/999/          | 200         | ok     | No entries found                   |

    # """ Test the behavior when we make a POST request"""

    Scenario: Add Product
      Given I have the following data
      | title | description | supplier_id | category_id | site_id | product_type_id | on_hand | re_order_level |
      | 1     | 1           | 1           | 1           | 1       | 1               | 1       | 1              |
      When I POST to the url "/api/v1/products/"
      Then I get a "201" response
      And I get a field "status" containing "ok"
      And I get a field "message" containing "ok"

    Scenario: Add Product Type
      Given I have the following data
      | name      | description |
      | Book      | Book Desc   |
      When I POST to the url "/api/v1/producttypes/"
      Then I get a "201" response
      And I get a field "status" containing "ok"
      And I get a field "message" containing "ok"

    Scenario: Add Category
      Given I have the following data
      | name  | description | image         |
      | 1     | 1           | 1             |
      When I POST to the url "/api/v1/categories/"
      Then I get a "201" response
      And I get a field "status" containing "ok"
      And I get a field "message" containing "ok"

      Scenario: Add Attributes for Product Type
      Given I have the following data
        | product_type_id | name | code | type    | is_required |
        | 1               | Book | P1   | string  | true      |
      When I POST to the url "/api/v1/producttypes/1/attributes/"
      Then I get a "201" response
      And I get a field "status" containing "ok"
      And I get a field "message" containing "ok"

  """ Test the behavior when we make a PUT request"""
    Scenario: Update Product Type
      Given I have a resource with the id "1"
      And I want to update its data to the following data
      | product_type_id | name     | description |
      | 1               | New      | New          |
      And I have the resource url "/api/v1/producttypes/1/"
      When I send a PUT request from client
      Then I get a "200" response
      And I get a field "status" containing "ok"
      And I get a field "message" containing "ok"

    Scenario: Update Product
      Given I have a resource with the id "1"
      And I want to update its data to the following data
      | product_id | title | description | supplier_id | category_id | site_id | product_type_id | on_hand | re_order_level |
      | 1          | 1     | 1           | 1           | 1           | 1       | 1               | 1       | 1              |
      And I have the resource url "/api/v1/products/1/"
      When I send a PUT request from client
      Then I get a "200" response
      And I get a field "status" containing "ok"
      And I get a field "message" containing "ok"

    Scenario: Update Category
      Given I have a resource with the id "1"
      And I want to update its data to the following data
      | category_id |  name | description | image       |
      | 1           | 1     | 1           | 1           |
      And I have the resource url "/api/v1/categories/1/"
      When I send a PUT request from client
      Then I get a "200" response
      And I get a field "status" containing "ok"
      And I get a field "message" containing "ok"

    Scenario: Update Product Attribute
      Given I have a resource with the id "1"
      And I want to update its data to the following data
      | product_attribute_id  |  name        | code         | type          | is_required |
      | 1                     | New name     | New Code     | new type      | true         |
      And I have the resource url "/api/v1/producttypes/1/attributes/1/"
      When I send a PUT request from client
      Then I get a "200" response
      And I get a field "status" containing "ok"
      And I get a field "message" containing "ok"