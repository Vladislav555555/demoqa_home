from pages.web_tables_page import WebTables
import time


def test_sort(browser):
    sort_page = WebTables(browser)
    sort_page.visit()

    def check_sort(column):
        assert column.get_dom_attribute('class') == 'rt-resizable-header-content'
        column.click()
        time.sleep(2)
        assert column.get_dom_attribute('class') == 'rt-th rt-th--sorted-asc'

    check_sort(sort_page.first_name_column)
    check_sort(sort_page.last_name_column)
    check_sort(sort_page.age_column)
    check_sort(sort_page.email_column)
    check_sort(sort_page.salary_column)
    check_sort(sort_page.department_column)
    check_sort(sort_page.action_column)





