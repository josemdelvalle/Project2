Feature: Customer Login

  Scenario: Login Home Page
    Given The user is on the login home page
    When The user inputs their username into the username field
    And  The user inputs their password into the password field
    And  The user clicks on the login button
    Then The user should login successfully