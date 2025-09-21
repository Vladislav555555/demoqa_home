from pages.modal_dialogs_page import ModalDialogsPage
import time
def test_modal_elements(browser):
    modal_dialogs = ModalDialogsPage(browser)
    modal_dialogs.visit()
    modal_dialogs.btn_submenu.click()
    assert modal_dialogs.btn_submenu.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialogs = ModalDialogsPage(browser)
    modal_dialogs.visit()
    modal_dialogs.refresh()
    modal_dialogs.main_icon.click()
    time.sleep(3)
    browser.back()
    time.sleep(3)
    browser.set_window_size(900, 400)
    assert modal_dialogs.equal_url()
    browser.forward()
    time.sleep(3)
    time.sleep(3)
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)




