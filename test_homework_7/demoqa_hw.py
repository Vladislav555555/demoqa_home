from test_homework_7.base_page_hw import BasePage
from test_homework_7.components_hw import WebElement

class DemoQa(BasePage):
    def __init__(self, driver):
        base_url = 'https://demoqa.com/'
        super().__init__(driver, base_url)
        self.footer = WebElement(driver, 'footer')
        self.btn_elements = WebElement(driver, 'div.top-card:nth-child(1)')


