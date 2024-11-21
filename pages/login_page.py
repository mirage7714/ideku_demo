
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        self.valid_username = 'Admin'
        self.valid_password = 'admin123'
        self.invalid_username = 'User'
        self.invalid_password = 'user123'

        self.username_field = 'username'
        self.password_field = 'password'
        self.login_btn_css = '.orangehrm-login-button'

        self.required_msg_css = ".oxd-input-field-error-message"

        self.invalid_msg_css = '.oxd-alert-content-text'
        self.invalid_icon_css = '.oxd-alert-content-icon'
        self.invalid_login_msg = 'Invalid credentials'

        super().__init__(driver)

    def type_username(self, username):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.NAME, self.username_field)))
        element = self.driver.find_element(By.NAME, self.username_field)
        element.click()
        element.clear()
        element.send_keys(username)

    def type_password(self, password):
        element = self.driver.find_element(By.NAME, self.password_field)
        element.click()
        element.clear()
        element.send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.login_btn_css)))
        element = self.driver.find_element(By.CSS_SELECTOR, self.login_btn_css)
        element.click()

    def check_invalid_login_toast(self):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.invalid_icon_css)))
        element = self.driver.find_element(By.CSS_SELECTOR, self.invalid_msg_css)
        assert element.text == self.invalid_login_msg

    def check_error_toast(self):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.required_msg_css)))
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.required_msg_css)
        for ele in elements:
            assert ele.text == 'Required'

    def login_invalid_credential(self):
        self.type_username(self.invalid_username)
        self.type_password(self.invalid_password)
        self.click_login_button()

    def login_correct_credential(self) -> DashboardPage:
        self.type_username(self.valid_username)
        self.type_password(self.valid_password)
        self.click_login_button()
        return DashboardPage(self.driver)

    def verify_product_info(self):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.result_query_sn_css)))
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.result_dl_css)))
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.result_image_css)))
        sn = self.driver.find_element(By.CSS_SELECTOR, self.result_query_sn_css)
        assert sn.text == self.valid_sn
        element = self.driver.find_element(By.CSS_SELECTOR, self.result_dl_css)
        dd = element.find_elements(By.XPATH, './/dd')
        for m in range(len(dd)):
            assert dd[m].text == self.correct_product_info[m]
        img = self.driver.find_element(By.CSS_SELECTOR, self.result_image_css)
        assert img.get_attribute('src') == self.correct_product_img_url
