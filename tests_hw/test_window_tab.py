import time
from pages.links import Links


def test_links(browser):
    links_page = Links(browser)
    links_page.visit()
    assert links_page.home.text == 'Home'
    href = links_page.home.get_dom_attribute('href')
    assert href == 'https://demoqa.com'
    time.sleep(2)
    assert len(browser.window_handles) == 1
    links_page.home.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
    time.sleep(2)
    browser.switch_to_window(browser.window_handles[1])
    assert browser.current_url == 'https://demoqa.com'
