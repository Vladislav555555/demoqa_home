from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver,self.base_url)

        self.central_text = WebElement(driver, 'div.col-12.mt-4.col-md-6')
        self.icon = WebElement(driver, 'header > a > img')
        self.btn_sidebar_first = WebElement(driver,'li#item-0')
        self.btn_sidebar_first_textbox = WebElement(driver,'li#item-0 > span')

        self.text_elements = WebElement(driver,'div.col-12:nth-child(2')

        self.btns_sidebar_first_menu = WebElement(driver, 'div:nth-child(1) > div > ul > li')

