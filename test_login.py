from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_unique_email

def test_login_via_personal_account():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.education-services.ru/')

    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

    wait = WebDriverWait(driver, 3)
    wait.until(EC.url_contains("login"))
    assert "login" in driver.current_url

    driver.quit()

def test_login_via_main_button():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.education-services.ru/')

    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

    wait = WebDriverWait(driver, 3)
    wait.until(EC.url_contains("login"))
    assert "login" in driver.current_url

    driver.quit()

def test_login_via_registration_form():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.education-services.ru/')

    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
    driver.find_element(By.LINK_TEXT, "Войти").click()

    wait = WebDriverWait(driver, 3)
    wait.until(EC.url_contains("login"))
    assert "login" in driver.current_url

    driver.quit()

def test_login_via_password_recovery_form():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.education-services.ru/')

    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
    driver.find_element(By.LINK_TEXT, "Войти").click()

    wait = WebDriverWait(driver, 3)
    wait.until(EC.url_contains("login"))
    assert "login" in driver.current_url

    driver.quit()

