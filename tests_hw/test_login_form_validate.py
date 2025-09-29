from pages.login_form_validate_page import LoginForm
import time


def test_login_form_validate(browser):
    login_form_validate = LoginForm(browser)
    login_form_validate.visit()
    assert login_form_validate.first_name.get_dom_attribute('placeholder') == 'First Name'
    time.sleep(2)
    assert login_form_validate.last_name.get_dom_attribute('placeholder') == 'Last Name'
    time.sleep(2)
    assert login_form_validate.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    time.sleep(2)
    pattern = login_form_validate.user_email.get_dom_attribute('pattern')
    assert pattern is not None
    assert '@' in pattern and '^' in pattern and '$' in pattern
    login_form_validate.submit_btn.scroll_to_element()
    time.sleep(2)
    login_form_validate.submit_btn.click()
    time.sleep(2)
    assert 'was-validated' in login_form_validate.user_form.get_dom_attribute('class')
