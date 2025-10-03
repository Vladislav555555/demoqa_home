from pages.modal_dialogs_page import ModalDialogsPage
from selenium.common.exceptions import WebDriverException
import time
import pytest


def test_check_modal(browser):
    modal_page = ModalDialogsPage(browser)
    try:
        modal_page.visit()
    except WebDriverException:
        pytest.skip("Страница недоступна")

    modal_page.small_modal.click()
    assert modal_page.modal_window.exist()
    modal_page.close_btn_small.click()
    time.sleep(2)
    modal_page.large_modal.click()
    assert modal_page.modal_window.exist()
    modal_page.close_btn_large.click()
    time.sleep(2)