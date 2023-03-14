from behave import *
from configuration.config import TestData
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage


@given(u'Launch the browser')
def launch_browser(context):
    if TestData.Browser == 'chrome':
        # context.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        context.driver = webdriver.Chrome()
    elif TestData.Browser == 'firefox':
        context.driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    else:
        raise ValueError('Browser Not Supported')


@when(u'Open the https://www.saucedemomm.com/ website')
def open_login_page(context):
    try:
        context.driver.get(TestData.URL)
        context.loginPage = LoginPage(context.driver)
        # context.dashboardpage = DashboardPage(context.driver)
    except:
        context.driver.close()
        assert False, "Test Failed , in Open Login Page"


@then(u'The login portal has been opened')
def validate_login_page(context):
    try:
        # time.sleep(60)
        context.loginPage.validateTitle()
    except:
        context.driver.close()
        assert False, "Test is failed in validate login page title"


@then(u'Provide the username "{user}" and password "{pwd}"')
def enter_login_creds(context, user, pwd):
    try:
        context.loginPage.enter_login_credentials(user, pwd)
    except:
        context.driver.close()
        assert False, "Test failed in enter credentials"


@then(u'Click on the Login button')
def enter_login(context):
    try:
        context.loginPage.enter_login()
    except:
        context.driver.close()
        assert False, "Test is failed in enter login"


@then(u'Login is successful and dashboard is opened')
def validate_dashboard_page(context):
    context.DashboardPage = DashboardPage(context.driver)
    context.DashboardPage.validatePageLoaded()


@then(u'Close the browser')
def close_browser(context):
    context.driver.close()
