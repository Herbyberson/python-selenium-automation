# Created by 12396 at 2/3/2024
Feature: Test scenarios for cart icon functionality on target website

  Scenario: User can click on cart icon to view items
    Given Target main page
    When User click cart icon
    Then Verify cart is empty