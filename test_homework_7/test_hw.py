from test_homework_7.demoqa_hw import DemoQa
from test_homework_7.elements_page_hw import ElementsPage

class TestDemoQa:

    def test_footer_text(self, browser):
        demo_page = DemoQa(browser)
        demo_page.open()
        footer_text = demo_page.footer.get_text()
        assert footer_text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.', \
               f"Результат: '{footer_text}'"

    def test_elements_page_center_text(self, browser):
        demo_page = DemoQa(browser)
        demo_page.open()
        demo_page.btn_elements.click()

        elements_page = ElementsPage(browser)
        center_text = elements_page.central_text.get_text()
        assert center_text == 'Please select an item from left to start practice.', \
               f"Результат: '{center_text}'"