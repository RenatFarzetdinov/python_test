from selenium.webdriver.common.by import By



class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea#currentAddress')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea#permanentAddress')
    SUBMIT = (By.ID, 'submit' )

    # created form

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.XPATH, '//button[@title="Expand all"]')
    CHECKBOX_HOME = (By.XPATH, '//span[text()="Home"]/preceding-sibling::span[@class="rct-checkbox"]')
    HOME_TOGGLE_BUTTON = (By.XPATH, '//span[text()="Home"]/ancestor::label/button')
    COLLAPSE_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Collapse all"]')
    CHECKBOX_WORKSPACE = (By.XPATH, '//span[text() = "WorkSpace"]/preceding-sibling::span[@class="rct-checkbox"]')
    CHECKBOX_WORKSPACE_BUTTON = (By.XPATH, '//span[text() = "WorkSpace"]/ancestor::label/button')
    CHECKBOX_REACT_BUTTON  = (By.XPATH, '//span[text() = "React"]/preceding-sibling::span[@class="rct-checkbox"]')
    CHECKBOX_ANGULAR = (By.XPATH, '//span[text() = "Angular"]/preceding-sibling::span[@class="rct-checkbox"]')
    CHECKBOX_DOCUMENT = (By.XPATH, '//span[text() = "Documents"]/preceding-sibling::span[@class ="rct-checkbox"]')
    CHECKBOX_DOWNLOADS = (By.XPATH, '//span[text() = "Downloads"]/preceding-sibling::span[@class="rct-checkbox"]')

    RESULT_BLOCK = (By.CSS_SELECTOR, '#result')

class RadioButtonLocators:
    YES_RADIO = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
    IMPRESSIVE_RADIO = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
    NO_RADIO = (By.CSS_SELECTOR, 'label[for="noRadio"]')

    RESULT_TEXT = (By.CSS_SELECTOR, 'span.text-success')

class ButtonLocators:
    DOUBLE_CLICK = (By.XPATH, '//button[@id="doubleClickBtn"]')
    RIGHT_CLICK = (By.XPATH, '//button[@id="rightClickBtn"]')
    CLICK_ME = (By.XPATH, '//button[text()="Click Me"]')

    RESULT_DOUBLE = (By.CSS_SELECTOR, '#doubleClickMessage')
    RESULT_RIGHT = (By.CSS_SELECTOR, '#rightClickMessage')
    RESULT_CLICK = (By.CSS_SELECTOR, '#dynamicClickMessage')


class WebTablesLocators:
    ADD_BUTTON = (By.XPATH, '//*[@id="addNewRecordButton"]')
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="submit"]')
    SEARCH_BOX = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#basic-addon2')
    FIRST_EDIT = (By.XPATH, '//*[@id="edit-record-1"]')
    FIRST_DELETE = (By.XPATH, '//*[@id="delete-record-1"]')

    TABLE_ROWS = (By.CSS_SELECTOR, '.rt-tbody .rt-tr-group')
    TABLE_CELL = (By.CSS_SELECTOR, '.rt-td')




