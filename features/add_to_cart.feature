Feature: AddToCart

  Scenario:
    Given The user is logged in
    And The user is on the productOverview page
    When The user fills out an order
    And  The user clicks on the submit button
    Then The product gets added to the cart

