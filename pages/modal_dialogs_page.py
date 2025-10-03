from pages.modal_dialogs import ModalDialogs
from components.components import WebElement

class ModalDialogsPage(ModalDialogs):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver,self.base_url)
        self.btn_submenu = WebElement(driver, '#item-0, #item-1, #item-2, #item-3, #item-4')
        self.main_icon = WebElement(driver, '#app > header > a > img')
        self.small_modal = WebElement(driver, '#showSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.modal_window = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.close_btn_large = WebElement(driver, '#closeLargeModal')
        self.close_btn_small = WebElement(driver, '#closeSmallModal')