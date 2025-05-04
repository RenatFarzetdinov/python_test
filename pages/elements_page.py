import time

from selenium.webdriver.support.wait import WebDriverWait

from locations.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
from locations.elements_page_locators import CheckBoxPageLocators
from locations.elements_page_locators import RadioButtonLocators
from locations.elements_page_locators import ButtonLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from locations.elements_page_locators import WebTablesLocators
from selenium.webdriver.common.by  import By

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self,):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('test')
        self.element_is_visible(self.locators.EMAIL).send_keys('test@test.tt')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('test test')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('test test test')
        submit_button = self.element_is_visible(self.locators.SUBMIT)
        self.go_to_element(submit_button)
        submit_button.click()

        #Возвращаем текст результата
        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text
        permanent_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text
        print(self.driver.page_source)
        return full_name, email, current_address, permanent_address

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def click_checkbox(self, checkbox_locators):
        checkbox = self.element_is_visible(checkbox_locators)
        self.go_to_element(checkbox)
        checkbox.click()

    def get_result_text(self):
        try:
            result = self.element_is_visible(self.locators.RESULT_BLOCK)
            return result.text.lower()
        except:
            return ''

class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def click_radio_button(self, radiobutton_locators):
        radio_button = self.element_is_visible(radiobutton_locators)
        self.go_to_element(radio_button)
        radio_button.click()

    def get_result_text(self):
        try:
            result = self.element_is_visible(self.locators.RESULT_TEXT)
            return result.text.lower()
        except:
            return ''


class ButtonPage(BasePage):
    locators = ButtonLocators()

    def click_button(self, button_locators):
        button_click = self.element_is_clickable(button_locators)
        self.go_to_element(button_click)
        button_click.click()

    def double_click(self, locator):
        element = self.element_is_clickable(locator)
        self.go_to_element(element)
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, locator):
        element = self.element_is_clickable(locator)
        self.go_to_element(element)
        ActionChains(self.driver).context_click(element).perform()

    def get_result_text_double(self):
        result = self.element_is_visible(self.locators.RESULT_DOUBLE)
        return result.text.lower()

    def get_result_text_right(self):
        result = self.element_is_visible(self.locators.RESULT_RIGHT)
        return result.text.lower()

    def get_result_text_click(self):
        result = self.element_is_visible(self.locators.RESULT_CLICK)
        return result.text.lower()


class WebTablesPage(BasePage):
    locators = WebTablesLocators

    def add_user(self, first_name, last_name, email, age, salary, department):
        self.element_is_clickable(self.locators.ADD_BUTTON).click()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SALARY).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
        self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()


    def get_table_user_data(self):
        rows = self.elements_are_visible(self.locators.TABLE_ROWS)
        all_data = []
        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, '.rt-td')
            cell_texts = [cell.text.strip() for cell in cells if cell.text.strip()]
            if cell_texts:
                all_data.append(cell_texts)

        return all_data
