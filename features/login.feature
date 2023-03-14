Feature: Validate the login feature

  Background:
    Given Launch the browser
    When Open the https://www.saucedemomm.com/ website
    Then The login portal has been opened

  @valid_login
  Scenario: Login with valid credentials
    And Provide the username "standard_user" and password "secret_sauce"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Close the browser