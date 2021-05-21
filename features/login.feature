Feature: Customer Login

  Scenario Outline: Login Home Page
    Given The User is on the Project 1 LogIn Page
    When The user types the <username> in the username bar
    And The user types the <password> in the password bar
    And Presses the login button
    Then The Logged in <message> appears

        Examples:
      |username | password| message   |
      | jose  | 12345 | Logged in |
      | serene| 12345 | Logged in |
#      |Alex     |Al       | Logged in |
#      |Joe      |Williams | Logged in |
