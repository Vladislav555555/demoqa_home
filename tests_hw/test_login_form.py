from pages.login_form_validate_page import LoginForm
from selenium.webdriver.common.keys import Keys
import time


def test_login_form(browser):
    test_login = LoginForm(browser)
    test_login.visit()
    test_login.select_state_btn.scroll_to_element()
    test_login.select_state_btn.click()
    time.sleep(2)
    test_login.inp_state.send_keys(Keys.PAGE_DOWN)
    test_login.inp_state.send_keys(Keys.ENTER)
