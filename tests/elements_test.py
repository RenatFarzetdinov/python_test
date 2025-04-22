import time
from pages.base_page import BasePage
from pages.elements_page import TextBoxPage



class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page  = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_felds()
            time.sleep(6)

    # assert driver.title == "Google"  # Пример проверки
