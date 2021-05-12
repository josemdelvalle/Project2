Feature: MakeOrder

  Scenario:
    Given The user is logged in
    And The user is on the order page
    When The fills out an order
    And  The user clicks on the submit button
    Then The order gets added to the cart

