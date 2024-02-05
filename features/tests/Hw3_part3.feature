# Created by 12396 at 2/3/2024
Feature: Test scenarios sign in functionality for Target

  Scenario: Sign out users can click on sign in icon
    Given Target webpage opened
    When Sign out users click sign on
    Then Verify sign in form is opened