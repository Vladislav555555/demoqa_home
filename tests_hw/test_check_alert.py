from pages.alerts import Alerts
import time


def test_alert(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    alert_page.alert_btn_time.click()
    time.sleep(7)
    assert alert_page.alert().text == 'This alert appeared after 5 seconds'
    alert_page.alert().accept()
