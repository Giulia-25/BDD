# scenario
from assertpy import assert_that
from pytest_bdd import scenarios, given, when, then, parser, parsers

from pages.login_page import LoginPage
from pages.secure_page import SecurePage

scenarios('../features/test_login_page.feature')


@given('open the login page')
def open_page(browser):
   login_page = LoginPage(browser)
   login_page.load_page()


# @when("The user types username tomsmith")
# def type_username(browser):
#     login_page = LoginPage(browser)
#     login_page.insert_username_field("tomsmith")


# sau cu parametru
@when(parsers.cfparse('The user types username "{username}"'))
def type_username(browser, username):
    login_page = LoginPage(browser)
    login_page.insert_username_field(username)


# @when("The user types password SuperSecretPassword!")
# def type_password(browser):
#     login_page = LoginPage(browser)
#     login_page.insert_password_field("SuperSecretPassword!")


# sau cu parametru
@when(parsers.cfparse('The user types password "{password}"'))
def type_password(browser, password):
    login_page = LoginPage(browser)
    login_page.insert_password_field(password)


@when("The user clicks login button")
def click_login_button(browser):
    login_page = LoginPage(browser)
    login_page.click_login_button()


@then("The user is redirected to secure page")
def check_redirect_to_secure_page(browser):
    secure_page = SecurePage(browser)
    assert_that(secure_page.get_current_url()).ends_with("/secure")


@then("A message appears on page")
def check_message(browser):
    secure_page = SecurePage(browser)
    assert_that(secure_page.get_flash_message()).contains("You logged into a secure area!")


@then(parsers.cfparse('"{message}" error message appears on page'))
def check_error_message(browser,message):
    login_page = LoginPage(browser, message)
    assert_that(login_page.get_flash_message().contains(message))