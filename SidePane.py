from selenium.webdriver.common.by import By

from utils.WebUtilities import WebUtilities


class SidePane:
    def __init__(self, driver):
        self.driver = driver
        self.web_util = WebUtilities(driver)
        self.ADMIN_SIDE_MENU = (
            By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Admin')]")

        self.PIM_SIDE_MENU = (
            By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'PIM')]")
        self.LEAVE_SIDE_MENU = (
            By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Leave')]")
        self.TIME_SIDE_MENU = (
            By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Time')]")
        self.RECRUITMENT_SIDE_MENU = (
            By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Recruitment')]")
        self.MY_INFO_SIDE_MENU = (
            By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'My Info')]")
        self.PERFORMANCE_SIDE_MENU = (
            By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Performance')]")
        self.DASHBOARD_SIDE_MENU = (
            By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Dashboard')]")
        self.DIRECTORY_SIDE_MENU = (
            By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Directory')]")
        self.MAINTENANCE_SIDE_MENU = (
            By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Maintenance')]")
        self.BUZZ_SIDE_MENU = (
            By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Buzz')]")

    def check_visibility_admin_side_pane(self):
        if self.web_util.is_element_displayed(self.ADMIN_SIDE_MENU):
            print(" Admin side pane is visible on the page.")
        else:
            raise AssertionError(" Admin side pane is not visible on the page.")

    def check_visibility_pim_side_pane(self):
        if self.web_util.is_element_displayed(self.PIM_SIDE_MENU):
            print(" PIM side pane is visible on the page.")
        else:
            raise AssertionError(" PIM side pane is not visible on the page.")

    def check_visibility_leave_side_pane(self):
        if self.web_util.is_element_displayed(self.LEAVE_SIDE_MENU):
            print(" Leave side pane is visible on the page.")
        else:
            raise AssertionError(" Leave side pane is not visible on the page.")

    def check_visibility_time_side_pane(self):
        if self.web_util.is_element_displayed(self.TIME_SIDE_MENU):
            print(" Time side pane is visible on the page.")
        else:
            raise AssertionError(" Time side pane is not visible on the page.")

    def check_visibility_recruitment_side_pane(self):
        if self.web_util.is_element_displayed(self.RECRUITMENT_SIDE_MENU):
            print(" Recruitment side pane is visible on the page.")
        else:
            raise AssertionError(" Recruitment side pane is not visible on the page.")

    def check_visibility_my_info_side_pane(self):
        if self.web_util.is_element_displayed(self.MY_INFO_SIDE_MENU):
            print(" My Info side pane is visible on the page.")
        else:
            raise AssertionError(" My Info side pane is not visible on the page.")

    def check_visibility_performance_side_pane(self):
        if self.web_util.is_element_displayed(self.PERFORMANCE_SIDE_MENU):
            print(" Performance side pane is visible on the page.")
        else:
            raise AssertionError(" Performance side pane is not visible on the page.")

    def check_visibility_dashboard_side_pane(self):
        if self.web_util.is_element_displayed(self.DASHBOARD_SIDE_MENU):
            print(" Dashboard side pane is visible on the page.")
        else:
            raise AssertionError(" Dashboard side pane is not visible on the page.")

    def check_visibility_directory_side_pane(self):
        if self.web_util.is_element_displayed(self.DIRECTORY_SIDE_MENU):
            print(" Directory side pane is visible on the page.")
        else:
            raise AssertionError(" Directory side pane is not visible on the page.")

    def check_visibility_buzz_side_pane(self):
        if self.web_util.is_element_displayed(self.BUZZ_SIDE_MENU):
            print(" Buzz side pane is visible on the page.")
        else:
            raise AssertionError(" Buzz side pane is not visible on the page.")

    def check_visibility_maintenance_side_pane(self):
        if self.web_util.is_element_displayed(self.MAINTENANCE_SIDE_MENU):
            print(" Maintenance side pane is visible on the page.")
        else:
            raise AssertionError(" Maintenance side pane is not visible on the page.")
