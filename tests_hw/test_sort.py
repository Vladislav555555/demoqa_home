from pages.web_tables_page import WebTables
import time


def test_sort(browser):
    sort_page = WebTables(browser)
    sort_page.visit()
    sort_page.first_name_column.click()
    time.sleep(2)

    sort_page.first_name_column.click()
    time.sleep(2)

    sort_page.age_column.click()
    time.sleep(2)

    sort_page.email_column.click()
    time.sleep(2)

    sort_page.salary_column.click()
    time.sleep(2)

    sort_page.department_column.click()
    time.sleep(2)

    sort_page.action_column.click()
    time.sleep(2)