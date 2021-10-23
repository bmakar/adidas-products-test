Feature: Product
  # In scope of feature will be covered API test cases of "product" functionality

  Scenario: GET all products
    Given 1 products created
    When user requests GET "/product"
    Then response with status code 200
    And body contains 1 products with next fields
      | key         |
      | id          |
      | name        |
      | description |
      | currency    |
      | price       |

  Scenario: GET product by id
    Given 1 products created
    When user requests GET "/product/0"
    Then response with status code 200
    And body contains product with next fields and values
      | key         | value           |
      | id          | 0               |
      | name        | product 0       |
      | description | product descr 0 |

  Scenario: POST Create product
    When user requests POST "/product" with params
      | key         | value     |
      | id          | 1         |
      | name        | test      |
      | description | desc test |
    Then response with status code 200
    And user requests GET "/product/1"
    Then response with status code 200
    And body contains product with next fields and values
      | key         | value     |
      | id          | 1         |
      | name        | test      |
      | description | desc test |

  Scenario: PUT Update product
    Given user requests POST "/product" with params
      | key         | value     |
      | id          | 1         |
      | name        | test      |
      | description | desc test |
    When user requests PUT "/product/1" with params
      | key  | value |
      | name | test2 |
    Then response with status code 200
    And user requests GET "/product/1"
    And body contains product with next fields and values
      | key         | value     |
      | id          | 1         |
      | name        | test2     |
      | description | desc test |

  Scenario: DELETE Remove product
    Given user requests POST "/product" with params
      | key         | value     |
      | id          | 1         |
      | name        | test      |
      | description | desc test |
    When user requests Delete "/product/1"
    Then response with status code 200
    And user requests GET "/product/1"
    And body contains product with next fields and values
      | key     | value                            |
      | message | product with id 1 doesn't exists |