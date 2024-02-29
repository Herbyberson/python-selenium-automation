Feature: Target.com sign in

  Scenario: log out users can sign in
    Given Open Target main page
    When log out users click Sign In
    And log out users click Sign In on Side Navigation
    Then Verify "Sign into your Target account" message

    

