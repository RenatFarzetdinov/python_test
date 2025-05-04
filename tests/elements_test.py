import time
from pages.base_page import BasePage
from pages.elements_page import TextBoxPage
from pages.elements_page import CheckBoxPage
from pages.elements_page import RadioButtonPage
from pages.elements_page import ButtonPage
from selenium.webdriver.common.action_chains import ActionChains
from pages.elements_page import WebTablesPage


class TestElements:
    # class TestTextBox:
    #
    #     def test_text_box(self, driver):
    #         text_box_page  = TextBoxPage(driver, 'https://demoqa.com/text-box')
    #         text_box_page.open()
    #         full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
    #
    #         assert driver.title == "DEMOQA" # Пример проверки
    #         assert full_name == "Name:test"
    #         assert email == "Email:test@test.tt"
    #         assert current_address == 'Current Address :test test'
    #         assert permanent_address == 'Permananet Address :test test test'
    #
    #     def test_text_box_empty_name(self, driver):
    #         text_box_page = TextBoxPage(driver,'https://demoqa.com/text-box')
    #         text_box_page.open()
    #         submit_button = text_box_page.element_is_visible(text_box_page.locators.SUBMIT)
    #         text_box_page.go_to_element(submit_button)
    #         submit_button.click()
    #         try:
    #             element = text_box_page.element_is_present(text_box_page.locators.CREATED_FULL_NAME)
    #             is_displayed = element.is_displayed()
    #         except:
    #             is_displayed = False
    #
    #         assert is_displayed is False
    #
    #
    # class TestCheckBox:
    #     def test_click_checkbox_home(self, driver):
    #         checkbox_page =  CheckBoxPage(driver,'https://demoqa.com/checkbox' )
    #         checkbox_page.open()
    #         checkbox_page.click_checkbox(checkbox_page.locators.CHECKBOX_HOME)
    #         result = checkbox_page.get_result_text()
    #         print("DEBUG result =", result)
    #         assert 'home' in result

        #
        # def test_click_documents_checkbox(self, driver):
        #     checkbox_page = CheckBoxPage(driver,'https://demoqa.com/checkbox')
        #     checkbox_page.open()
        #     checkbox_page.click_checkbox(checkbox_page.locators.EXPAND_ALL_BUTTON)
        #     checkbox_page.click_checkbox(checkbox_page.locators.CHECKBOX_DOCUMENT)
        #     result = checkbox_page.get_result_text()
        #     assert 'workspace', 'office' in result

        # def test_toggle_checkbox_angular(self, driver):
        #     checkbox_page = CheckBoxPage(driver,'https://demoqa.com/checkbox')
        #     checkbox_page.open()
        #     checkbox_page.click_checkbox(checkbox_page.locators.EXPAND_ALL_BUTTON)
        #     checkbox_page.click_checkbox(checkbox_page.locators.CHECKBOX_ANGULAR)
        #     result_click_checkbox = checkbox_page.get_result_text()
        #     assert 'angular' in result_click_checkbox
        #
        #     checkbox_page.click_checkbox(checkbox_page.locators.CHECKBOX_ANGULAR)
        #     time.sleep(2)
        #     result_after_click = checkbox_page.get_result_text()
        #     assert 'angular' not in result_after_click
        #
        # def test_click_radio_yes(self, driver):
        #     radio_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
        #     radio_page.open()
        #     radio_page.click_radio_button(radio_page.locators.YES_RADIO)
        #     result = radio_page.get_result_text()
        #     assert 'yes' in result
        #
        #
        # def test_click_radio_no(self, driver):
        #     radio_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
        #     radio_page.open()
        #     radio_page.click_radio_button(radio_page.locators.NO_RADIO)
        #     result = radio_page.get_result_text()
        #     assert 'no' not in result

    #
    # class TestButton:
    #
    #
    #     def test_button_click(self,driver):
    #         button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
    #         button_page.open()
    #         button_page.click_button(button_page.locators.CLICK_ME)
    #         result = button_page.get_result_text_click()
    #         print("DEBUG result =", result)
    #         assert 'you have done a dynamic click' in result
    #
    #     def test_double_click(self,driver):
    #         button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
    #         button_page.open()
    #         button_page.double_click(button_page.locators.DOUBLE_CLICK)
    #         result = button_page.get_result_text_double()
    #         assert 'you have done a double click' in result
    #
    #     def test_right_click(self, driver):
    #         button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
    #         button_page.open()
    #         button_page.right_click(button_page.locators.RIGHT_CLICK)
    #         result = button_page.get_result_text_right()
    #         assert 'you have done a right click' in result

    class TestWebTables:
        def test_add_user(self, driver):
            webtables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            webtables_page.open()
            webtables_page.add_user(
                first_name='Alice',
                last_name='Smith',
                email='alice@example.com',
                age='28',
                salary='4000',
                department='QA'
            )
            all_users = webtables_page.get_table_user_data()
            print("DEBUG all_users =", all_users)
            assert ['Alice', 'Smith', '28', 'alice@example.com', '4000', 'QA'] in all_users

