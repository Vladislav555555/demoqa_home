from pages.text_box_page import TextBoxPage
import time


def test_text_box_page(browser):
    text_box_page = TextBoxPage(browser)
    text_box_page.visit()
    text_box_page.full_name.send_keys('Maksimov Ivan Sergeevich')
    text_box_page.current_address.send_keys('St. Petersburg, st. Ivana Fomina, building 5, apartment 500')
    text_box_page.submit_btn.click()
    text_box_page.name.scroll_to_element()
    time.sleep(2)
    assert text_box_page.name.get_text() == 'Name:Maksimov Ivan Sergeevich'
    time.sleep(2)
    assert text_box_page.address.get_text() == 'Current Address :St. Petersburg, st. Ivana Fomina, building 5, apartment 500'



