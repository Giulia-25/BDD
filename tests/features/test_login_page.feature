#def test_successful_login(browser):
#    login_page = LoginPage(browser)
#    secure_page = SecurePage(browser)
#    login_page.load_page()
#    login_page.login("tomsmith", "SuperSecretPassword!")
#    assert_that(secure_page.get_current_url()).ends_with("/secure")
#    assert_that(secure_page.get_flash_message()).contains("You logged into a secure area!")

Feature: Test login functionality

  Background: before tests
    Given open the login page

  Scenario: Test successful login

    When the user types username "tomsmith"
    And the user types password "SuperSecretPassword!"
    And the user clicks login
    Then the user is redirected to secure page
    And a message appears on page

  Scenario: Test negative for password

    When the user types username "tomsmith"
    And the user types password "egegs"
    And the user clicks login
    Then "Your password is invalid!" error message appears on page

  Scenario: Test negative for username

    When the user types username "egagge"
    And the user types password "egegs"
    And the user clicks login
    Then "Your username is invalid!" error message appears on page


  Scenario Outline: Test negative scenarios
    When the user types username "<username>"
    And the user types password "<password>"
    And the user clicks login
    Then "<error>" error message appears on page


    Examples: username, password and error
       | username| password| error |
       | tomsmith |   dsfdf | Your password is invalid! cbvcnbnn|
       | fdsfd    |   SuperSecretPassword!  | Your username is invalid! |
       | TOMSMITH   |  SuperSecretPassword!  | Your username is invalid! |