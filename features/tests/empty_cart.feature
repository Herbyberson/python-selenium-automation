Feature: Target.com cart verification

  Scenario: "Your cart is empty" message is shown for empty cart
    Given Open Target main page
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown
