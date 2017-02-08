import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select


class OnetEmailCreator:
    login_selector = 'login_user'

    inputs = {
        'fullname': 'f_nameSurname',
        'city_postalcode': 'f_postcodePlace',
        'password': 'f_password',
        'repeat_password': 'f_confirmPassword',
        # 'alternative_contact': 'f_phonesEmails'
    }
    checkboxes_selectors = {
        'gender_woman': '#f_gender_K',
        'gender_man': '#f_gender_M',
        'agreements': 'f_confirm',
        'captcha': 'recaptcha-anchor > div.recaptcha-checkbox-checkmark'
    }
    dropdowns_selectors = {
        'birthdate_day': 'f_birthDate_day',
        'birthdate_month': '//*[@id="registerForm"]/div/div[3]/div[1]/fieldset/div/div/ul/li[3]/select[2]',
        'birthdate_year': 'registerForm > div > div.fieldsetWrap > div:nth-child(1) > fieldset > div > div > ul > '
                          'li:nth-child(3) > select.yearSelect',
        'country': 'f_country'
    }
    buttons = {
        1: '//*[@id="registerForm"]/div/div[3]/div[2]/fieldset/div/div/ul/li/div/div[2]/span/input',
        2: '//*[@id="registerForm"]/div/div[4]/span/input'
    }

    check_login_button = '//*[@id="registerForm"]/div/div[3]/div[1]/fieldset/div/div/ul/li/div/div[2]/span/input'

    account_created = False

    def __init__(self, driver):
        self.webdriver = driver
        driver.get("https://konto.onet.pl/register-email.html?app_id=poczta.onet.pl.front")
        wait = ui.WebDriverWait(driver, 10)
        print("jestesmy w onetemail konstruktor")

    def fill_inputs(self, info):
        login = info.getElementsByTagName('login')[0].firstChild.data
        login_node = self.webdriver.find_element_by_id(self.login_selector)
        login_node.send_keys(login)

        check_login = self.webdriver.find_element_by_xpath(self.check_login_button)
        check_login.click()

        for text_field in self.inputs:
            print(text_field + ': ' + self.inputs[text_field])
            value = info.getElementsByTagName(text_field)[0].firstChild.data
            node = self.webdriver.find_element_by_id(self.inputs[text_field])
            node.send_keys(value)

        for dropdown in self.dropdowns_selectors:
            print(dropdown + ': ' + self.dropdowns_selectors[dropdown])
            value = info.getElementsByTagName(dropdown)[0].firstChild.data
            node = self.webdriver.find_element_by_id(self.inputs[text_field])
            Select(node).select_by_value(value)



    def solve_captcha(self):

        print("solved")
