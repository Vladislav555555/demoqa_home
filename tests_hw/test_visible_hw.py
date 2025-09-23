from pages.accordion_page import AccordionPage
import time

def test_visible_section_text(browser):
    accordion_page = AccordionPage(browser)
    accordion_page.visit()
    assert accordion_page.section_text.is_displayed()

def test_visible_heading_text(browser):
    accordion_page = AccordionPage(browser)
    accordion_page.visit()
    assert accordion_page.heading_text.is_displayed()
    accordion_page.heading_text.click()
    time.sleep(2)
    assert not accordion_page.section_text.is_displayed()

def test_visible_section_text_default(browser):
    accordion_page = AccordionPage(browser)
    accordion_page.visit()
    assert not accordion_page.section_element_first.is_displayed()
    time.sleep(3)
    assert not accordion_page.section_element_second.is_displayed()
    time.sleep(3)
    assert not accordion_page.section_element_third.is_displayed()

