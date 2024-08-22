from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_homepage_loads():
    driver = webdriver.Chrome()
    driver.get("http://demo-store.seleniumacademy.com/")

    assert "Madison Island" in driver.title

    driver.quit()


def test_homepage_navigation():
    driver = webdriver.Chrome()
    driver.get("http://demo-store.seleniumacademy.com/")

    link = driver.find_element(By.LINK_TEXT, "SALE")
    link.click()

    assert "Sale" in driver.title

    driver.quit()
