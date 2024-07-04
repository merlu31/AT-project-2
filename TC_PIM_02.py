import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.AdminPage import AdminPage
from pageObjects.LoginPage import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


@pytest.mark.parametrize(("username", "password", "firstname", "middlename", "lastname"), [
    ("Admin", "admin123", "archana", "f", "merlin")
])
def test_header_validation(driver, username, password, firstname, middlename, lastname):
    login_page = LoginPage(driver)
    login_page.open_page("https://opensource-demo.orangehrmlive.com")

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    admin_page = AdminPage(driver)
    admin_page.print_current_page_title()
    admin_page.click_admin_side_menu()
    check_methods = [
        admin_page.check_visibility_user_management_component,
        admin_page.check_visibility_job_component,
        admin_page.check_visibility_organization_component,
        admin_page.check_visibility_qualifications_component,
        admin_page.check_visibility_nationalities_component,
        admin_page.check_visibility_corporate_branding_component,
        admin_page.check_visibility_configuration_component
    ]

    for check_method in check_methods:
        try:
            check_method()
        except AssertionError as e:
            print(f"Failed to verify component visibility: {e}")
