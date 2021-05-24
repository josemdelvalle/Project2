Feature: RemoveOrder

  Scenario:
    Given The user is logged in
    And The user is on the cart page
    And The user has items in the cart
    When The user clicks on remove order
    Then The item gets removed from the cart


