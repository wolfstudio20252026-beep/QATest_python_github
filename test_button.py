from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture()
def browser():
    chrome = webdriver.Chrome()
    return chrome

def test_button_exist(browser: webdriver.Chrome):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()

