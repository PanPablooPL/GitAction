from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_search_functionality():
    driver = webdriver.Chrome()
    driver.get("http://demo-store.seleniumacademy.com/")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("phone")
    search_box.submit()

    assert "Search results for: 'phone'" in driver.page_source

    driver.quit()
