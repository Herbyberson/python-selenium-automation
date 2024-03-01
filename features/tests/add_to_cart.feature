Feature: Add a product to cart tests

  Scenario: User can add Stanly Cup product on target
    Given Open Target main page
    When Search for Stanley Cup
    Then Add to cart first result of product
