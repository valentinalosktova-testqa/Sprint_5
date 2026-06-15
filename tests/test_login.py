from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.locators import StellarLocators
from urls import BASE_URL


class TestLogin:

    def test_login_via_personal_account(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*StellarLocators.LOGIN_LINK).click()
        wait = WebDriverWait(driver, 3)
        wait.until(EC.url_contains("login"))
        assert "login" in driver.current_url

    def test_login_via_main_button(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        wait = WebDriverWait(driver, 3)
        wait.until(EC.url_contains("login"))
        assert "login" in driver.current_url

    def test_login_via_registration_form(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*StellarLocators.LOGIN_LINK).click()
        driver.find_element(*StellarLocators.REGISTER_LINK).click()
        driver.find_element(*StellarLocators.LOGIN_LINK_ON_FORM).click()
        wait = WebDriverWait(driver, 3)
        wait.until(EC.url_contains("login"))
        assert "login" in driver.current_url

    def test_login_via_password_recovery_form(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*StellarLocators.LOGIN_LINK).click()
        driver.find_element(*StellarLocators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*StellarLocators.LOGIN_LINK_ON_FORM).click()
        wait = WebDriverWait(driver, 3)
        wait.until(EC.url_contains("login"))
        assert "login" in driver.current_url