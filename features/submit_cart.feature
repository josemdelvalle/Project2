Feature: SubmitOrder

  Scenario:
    Given The user is logged in
    And The user has items in the cart
    And The user is on the cart page
    When The user clicks on submit order
    Then The item gets submitted


