from pages.demoqa import DemoQa

def test_check_title_demo(browser):
    demo_page = DemoQa(browser)
    demo_page.visit()
    assert browser.title == 'DEMOQA'