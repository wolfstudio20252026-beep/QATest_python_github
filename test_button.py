from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome = webdriver.Chrome(options=options)
    return chrome

def test_button_exist(browser: webdriver.Chrome):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()

def test_button_exist_2(browser: webdriver.Chrome):
    browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    assert browser.find_element(By.PARTIAL_LINK_TEXT, 'Click').is_displayed()

