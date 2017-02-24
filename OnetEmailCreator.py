import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

class OnetEmailCreator:
    login_selector = 'login_user'

    inputs = {
        'fullname': 'f_nameSurname',
        # 'city_postalcode': 'f_postcodePlace',
        'password': 'f_password',
        'repeat_password': 'f_confirmPassword',
        # 'alternative_contact': 'f_phonesEmails'
    }
    checkboxes_selectors = {
        'gender_woman': '#f_gender_K',
        # 'gender_man': 'f_gender_M',
        'agreements': 'f_confirm',
        # 'captcha': 'recaptcha-anchor > div.recaptcha-checkbox-checkmark'
    }
    dropdowns_selectors = {
        'birthDate_day': '//*[@id="f_birthDate_day"]',
        'birthDate_month': '//*[@id="registerForm"]/div/div[3]/div[2]/fieldset/div/div/ul/li[2]/select[2]',
        'birthDate_year': '//*[@id="registerForm"]/div/div[3]/div[2]/fieldset/div/div/ul/li[2]/select[3]',
        # 'country': 'f_country'
    }
    buttons = {
        1: '//*[@id="registerForm"]/div/div[3]/div[2]/fieldset/div/div/ul/li/div/div[2]/span/input',
        2: '//*[@id="registerForm"]/div/div[4]/span/input'
    }

    check_login_button = '//*[@id="registerForm"]/div/div[3]/div[1]/fieldset/div/div/ul/li/div/div[2]/span/input'

    account_created = False
    solved_captcha = False
    login = str()
    password = str()

    def __init__(self, driver):
        self.webdriver = driver
        driver.get("https://konto.onet.pl/register-email.html?app_id=poczta.onet.pl.front")
        wait = ui.WebDriverWait(driver, 10)

    def fill_inputs(self, info):
        login = info.getElementsByTagName('login')[0].firstChild.data
        login_node = self.webdriver.find_element_by_id(self.login_selector)
        login_node.send_keys(login)

        check_login = self.webdriver.find_element_by_xpath(self.check_login_button)
        check_login.click()

        wait = WebDriverWait(self.webdriver, 10)
        validated = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.checkedFullEmail")))

        for text_field in self.inputs:
            print(text_field + ': ' + self.inputs[text_field])
            try:
                value = info.getElementsByTagName(text_field)[0].firstChild.data
                node = self.webdriver.find_element_by_id(self.inputs[text_field])
                node.send_keys(value)
            except NoSuchElementException:
                print("error: {0}".format(NoSuchElementException))
                self.account_created = False

        for dropdown in self.dropdowns_selectors:
            print(dropdown + ': ' + self.dropdowns_selectors[dropdown])
            try:
                value = info.getElementsByTagName(dropdown)[0].firstChild.data
                node = self.webdriver.find_element_by_xpath(self.dropdowns_selectors[dropdown])
                for option in node.find_elements_by_tag_name('option'):
                    if option.text == value:
                        option.click()
                        break
            except NoSuchElementException:
                print("error: {0}".format(NoSuchElementException))
                self.account_created = False

        for chkbx in self.checkboxes_selectors:
            print(chkbx + ': ' + self.checkboxes_selectors[chkbx])
            try:
                node = self.webdriver.find_element_by_id(self.checkboxes_selectors[chkbx])
                node.click()
            except NoSuchElementException:
                print("error: {0}".format(NoSuchElementException))
                self.account_created = False

        self.wait_for_captcha()


        self.account_created = True
        self.login = login
        self.password = info.getElementsByTagName('password')[0].firstChild.data

    def wait_for_captcha(self):
        return True
        for i in range(0, 14):
            time.sleep(2)
            if self.solved_captcha:
                return True

        return False
