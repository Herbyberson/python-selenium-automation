# Created by 12396 at 2/1/2024
Feature: Target.com search tests

  Scenario: User can search for coffee on target
    Given Open Target main page
    When Search for coffee
    Then Search results for coffee are shown
    Then Page URL has search term coffee

