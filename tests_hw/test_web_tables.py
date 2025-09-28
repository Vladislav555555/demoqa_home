from pages.web_tables_page import WebTables
import time


def test_web_tables(browser):
    web_tables = WebTables(browser)
    web_tables.visit()
    web_tables.add_btn.click_force()
    time.sleep(2)
    web_tables.submit_btn.click_force()
    assert web_tables.first_name.is_displayed()
    time.sleep(2)
    web_tables.first_name.send_keys('Ivan')
    web_tables.last_name.send_keys('Ivanov')
    web_tables.email.send_keys('dsvsv@gmail.com')
    web_tables.age.send_keys('30')
    web_tables.salary.send_keys('50')
    web_tables.department.send_keys('IT')
    web_tables.submit_btn.click()
    time.sleep(2)
    web_tables.edit_btn.click_force()
    assert web_tables.first_name.get_dom_attribute('value') == 'Ivan'
    web_tables.first_name.clear()
    web_tables.first_name.send_keys('Maxim')
    web_tables.submit_btn.click_force()
    time.sleep(2)
    assert web_tables.first_name_field.get_text() == 'Maxim'
    web_tables.refresh()
    time.sleep(2)
    web_tables.delete_btn.click_force()

