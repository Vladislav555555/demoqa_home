from pages.web_tables_page import WebTables
import time
from selenium.webdriver.common.keys import Keys


def test_web_tables(browser):
    web_tables = WebTables(browser)
    web_tables.visit()
    web_tables.rows_btn.scroll_to_element()
    web_tables.rows_btn.click()
    time.sleep(2)
    web_tables.rows_btn.send_keys(Keys.PAGE_UP)
    web_tables.rows_btn.send_keys(Keys.ENTER)
    assert web_tables.rows_count.check_count_elements(count=5 )
    time.sleep(2)
    assert web_tables.next_btn.get_dom_attribute('disabled') is not None
    time.sleep(2)
    assert web_tables.previous_btn.get_dom_attribute('disabled') is not None
    time.sleep(2)

    for i in range(3):
        web_tables.add_btn.click_force()
        time.sleep(2)
        web_tables.first_name.send_keys('Ivan')
        web_tables.last_name.send_keys('Ivanov')
        web_tables.email.send_keys('dsvsv@gmail.com')
        web_tables.age.send_keys('30')
        web_tables.salary.send_keys('50')
        web_tables.department.send_keys('IT')
        web_tables.submit_btn.click()
        time.sleep(6)

    assert web_tables.total_page.get_text() == '2'
    web_tables.next_btn.click()
    time.sleep(2)
    web_tables.previous_btn.click()

