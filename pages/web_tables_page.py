from pages.base_page import BasePage
from components.components import WebElement

class WebTables(BasePage):
    def __init__(self, driver):
        base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, base_url)
        self.add_btn = WebElement(driver, '#addNewRecordButton')
        self.first_name = WebElement(driver, '#firstName-label')
        self.last_name = WebElement(driver, '#lastName-label')
        self.email = WebElement(driver, '#userEmail-label')
        self.age = WebElement(driver, '#age-label')
        self.salary = WebElement(driver, '#salary-label')
        self.department = WebElement(driver, '#department-label')
        self.submit_btn = WebElement(driver, '#submit')
        self.edit_btn = WebElement(driver, '#edit-record-4 > svg')
        self.first_name_field = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.delete_btn = WebElement(driver, '#delete-record-4 > svg > path')

        self.rows_btn = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select')
        self.rows_count = WebElement(driver, '.rt-table .rt-tbody .rt-tr')
        self.next_btn = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')
        self.previous_btn = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button')
        self.total_page = WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > span')

        self.first_name_column = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(1) > div.rt-resizable-header-content')
        self.last_name_column = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(2) > div.rt-resizable-header-content')
        self.age_column = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(3) > div.rt-resizable-header-content')
        self.email_column = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(4) > div.rt-resizable-header-content')
        self.salary_column = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div.rt-th.rt-resizable-header.-sort-asc.-cursor-pointer > div.rt-resizable-header-content')
        self.department_column = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div.rt-th.rt-resizable-header.-sort-asc.-cursor-pointer > div.rt-resizable-header-content')
        self.action_column = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(7) > div.rt-resizable-header-content')