from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_unique_email
from pages.locators import StellarLocators
from urls import BASE_URL


class TestRegistration:

    def test_registration_success(self, driver):
        driver.get(BASE_URL)
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        email = generate_unique_email()

        driver.find_element(*StellarLocators.NAME_INPUT).send_keys("Валентина")
        driver.find_element(*StellarLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*StellarLocators.PASSWORD_INPUT).send_keys("123456")

        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()

        wait = WebDriverWait(driver, 3)
        wait.until(EC.url_contains("login"))
        assert "login" in driver.current_url

    def test_registration_short_password_error(self, driver):
        driver.get(BASE_URL)
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

        driver.find_element(*StellarLocators.NAME_INPUT).send_keys("Валентина")
        driver.find_element(*StellarLocators.EMAIL_INPUT).send_keys("test@ya.ru")
        driver.find_element(*StellarLocators.PASSWORD_INPUT).send_keys("123")

        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()

        error = driver.find_element(*StellarLocators.PASSWORD_ERROR)
        assert error.is_displayed()

    
