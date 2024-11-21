
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    def __init__(self, driver):

        self.dashboard_title_css = '.oxd-topbar-header-breadcrumb-module'
        self.upgrade_btn_css = '.orangehrm-upgrade-button'
        self.side_menu_xpath = '//ul[@class="oxd-main-menu"]'

        super().__init__(driver)

    def is_loaded(self):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.dashboard_title_css)))
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.upgrade_btn_css)))
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.XPATH, self.side_menu_xpath)))
