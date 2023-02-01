Feature: when user login and Provited id and password
  Background: Comman Steps
    Given Open Chrome Browser
    When Open ZoomVenues.com site
    And Click Sign In
    Then enter id is "omworld01@gmail.com" and enter password is "12345678"
    And click log in
    Then select vanue

  Scenario: login cust acc then Search bar use
    And search bar use
