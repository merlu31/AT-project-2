import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

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
def test_reset_password(driver, username, password, firstname, middlename, lastname):
    login_page = LoginPage(driver)
    login_page.open_page("https://opensource-demo.orangehrmlive.com")
    login_page.click_forgot_password_link()
    login_page.enter_username(username)
    login_page.click_reset_password_button()
    time.sleep(2)
    try:
        assert "Reset Password link sent successfully" in driver.page_source, "Failed to send reset link"
        time.sleep(2)
        success_message = login_page.get_success_message()
        if success_message:
            print(f"Passed: {success_message}")
        else:
            print("Passed, but success message was not found.")
    except AssertionError as e:
        print("Failed")
        raise e
