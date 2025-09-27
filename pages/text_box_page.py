from pages.text_box_hw import TextBox
from components.components import WebElement

class TextBoxPage(TextBox):
    def __init__(self, driver):
        base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, base_url)
        self.full_name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress')
        self.submit_btn = WebElement(driver, '#submit')
        self.name = WebElement(driver, '#name')
        self.address = WebElement(driver, '#currentAddress')
