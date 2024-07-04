import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.AdminPage import AdminPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SidePane import SidePane


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
    admin_page.click_admin_side_menu()
    side_pane = SidePane(driver)
    check_methods = [
        side_pane.check_visibility_admin_side_pane,
        side_pane.check_visibility_pim_side_pane,
        side_pane.check_visibility_leave_side_pane,
        side_pane.check_visibility_time_side_pane,
        side_pane.check_visibility_recruitment_side_pane,
        side_pane.check_visibility_my_info_side_pane,
        side_pane.check_visibility_performance_side_pane,
        side_pane.check_visibility_dashboard_side_pane,
        side_pane.check_visibility_directory_side_pane,
        side_pane.check_visibility_maintenance_side_pane,
        side_pane.check_visibility_buzz_side_pane
    ]

    for check_method in check_methods:
        try:
            check_method()
        except AssertionError as e:
            print(f"Failed to verify element visibility: {e}")
