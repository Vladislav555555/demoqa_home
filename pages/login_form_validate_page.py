from pages.text_box_hw import TextBox
from components.components import WebElement

class LoginForm(TextBox):
    def __init__(self, driver):
        base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, base_url)
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.submit_btn = WebElement(driver, '#submit')
        self.user_form = WebElement(driver, '#userForm')
        self.select_state_btn = WebElement(driver, '#state')
        self.inp_state = WebElement(driver, '#react-select-3-input')