Feature: Customer Login

  Scenario Outline: Login Home Page
    Given The User is on the LogIn Page
    When The user types the <username> in the username bar
    And The user types the <password> in the password bar
    And Presses the login button
    Then Redirected to Store Page

        Examples:
      |username | password|
      | jose  | 12345 |
      | serene| 12345 |
#      |Alex     |Al       | Logged in |
#      |Joe      |Williams | Logged in |
