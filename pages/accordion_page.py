from pages.accordion import Accordion
from components.components import WebElement

class AccordionPage(Accordion):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)
        self.section_text = WebElement(driver, '#section1Content > p')
        self.heading_text = WebElement(driver, '#section1Heading')

        self.section_element_first = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section_element_second = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section_element_third = WebElement(driver, '#section3Content > p')
