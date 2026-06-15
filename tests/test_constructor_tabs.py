import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConstructorTabs:

    @pytest.mark.parametrize("tab_name", ["Булки", "Соусы", "Начинки"])
    def test_constructor_tabs(self, driver, tab_name):
        driver.get('https://stellarburgers.education-services.ru/')

        tab = driver.find_element(By.XPATH, f".//span[text()='{tab_name}']")
        driver.execute_script("arguments[0].click();", tab)

        wait = WebDriverWait(driver, 3)
        active_tab = wait.until(EC.visibility_of_element_located(
            (By.XPATH, f".//div[contains(@class, 'tab_tab_type_current')]//span[text()='{tab_name}']")
        ))
        assert active_tab.is_displayed()