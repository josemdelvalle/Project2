Feature: SubmitOrder

  Scenario:
    Given The user is logged in
    And The user is on the cart page
    And The user has items in the cart
    When The user clicks on submit order
    Then The item gets submitted


