from selenium.webdriver.common.by import By

from utils.WebUtilities import WebUtilities


class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.web_util = WebUtilities(driver)
        self.ADMIN_SIDE_MENU = (
            By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Admin')]")
        self.USER_MANAGEMENT_COMPONENT = (
            By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item'][contains(.,'User Management')]")
        self.JOB_COMPONENT = (By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item'][contains(.,'Job')]")
        self.ORGANIZATION_COMPONENT = (By.XPATH, "//span[contains(.,'Organization')]")
        self.QUALIFICATIONS_COMPONENT = (By.XPATH, "//span[contains(.,'Qualifications')]")
        self.NATIONALITIES_COMPONENT = (By.XPATH, "//a[contains(.,'Nationalities')]")
        self.CORPORATE_BRANDING_COMPONENT = (By.XPATH, "//a[contains(.,'Corporate Branding')]")
        self.CONFIGURATION_COMPONENT = (By.XPATH, "//span[contains(.,'Configuration')]")

    def click_admin_side_menu(self):
        self.web_util.click_element(self.ADMIN_SIDE_MENU)

    def print_current_page_title(self):
        print(f"Current Page Title: {self.driver.title}")

    def check_visibility_user_management_component(self):
        if self.web_util.is_element_displayed(self.USER_MANAGEMENT_COMPONENT):
            print("User Management component is visible on the page.")
        else:
            raise AssertionError("User Management component is not visible on the page.")

    def check_visibility_job_component(self):
        if self.web_util.is_element_displayed(self.JOB_COMPONENT):
            print(" Job component is visible on the page.")
        else:
            raise AssertionError("User Job component is not visible on the page.")

    def check_visibility_organization_component(self):
        if self.web_util.is_element_displayed(self.ORGANIZATION_COMPONENT):
            print(" Organization component is visible on the page.")
        else:
            raise AssertionError("User Organization component is not visible on the page.")

    def check_visibility_qualifications_component(self):
        if self.web_util.is_element_displayed(self.QUALIFICATIONS_COMPONENT):
            print(" Qualifications component is visible on the page.")
        else:
            raise AssertionError("User Qualifications component is not visible on the page.")

    def check_visibility_nationalities_component(self):
        if self.web_util.is_element_displayed(self.NATIONALITIES_COMPONENT):
            print(" Nationalities component is visible on the page.")
        else:
            raise AssertionError("User Nationalities component is not visible on the page.")

    def check_visibility_corporate_branding_component(self):
        if self.web_util.is_element_displayed(self.CORPORATE_BRANDING_COMPONENT):
            print(" Corporate Branding component is visible on the page.")
        else:
            raise AssertionError("User Corporate Branding component is not visible on the page.")

    def check_visibility_configuration_component(self):
        if self.web_util.is_element_displayed(self.CONFIGURATION_COMPONENT):
            print(" Configuration component is visible on the page.")
        else:
            raise AssertionError(" Configuration component is not visible on the page.")


