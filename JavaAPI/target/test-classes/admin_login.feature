Feature: The Administrator User can log in successfully

  Scenario: The Admin User logs in
    Given The User is on the login page
    When The User inputs their username and password
    When The User clicks on the login button
    Then The User is on the Administrator page
    And The User can see the most popular product to order