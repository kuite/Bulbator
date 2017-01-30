class OnetEmailCreator:
    inputs_selectors = {
        'full name': '#f_nameSurname',
        'login': '#login_user',
        'city_postalcode': '#f_postcodePlace',
        'password': '#f_password',
        'repeat_password': '#f_confirmPassword',
        'alternative_contact': '#f_phonesEmails'
    }
    checkboxes_selectors = {
        'gender_woman': '#f_gender_K',
        'gender_man': '#f_gender_M',
        'agreements': '#f_confirm',
        'captcha': '#recaptcha-anchor > div.recaptcha-checkbox-checkmark'
    }
    dropdowns_selectors = {
        'birthdate_day': '#f_birthDate_day',
        'birthdate_month': '#registerForm > div > div.fieldsetWrap > div:nth-child(1) > fieldset > div > div > ul > '
                           'li:nth-child(3) > select.monthSelect',
        'birthdate_year': '#registerForm > div > div.fieldsetWrap > div:nth-child(1) > fieldset > div > div > ul > '
                          'li:nth-child(3) > select.yearSelect',
        'country': '#f_country'
    }
    account_created = False

    def __init__(self, webdriver):
        self.webdriver = webdriver
        webdriver.get("https://konto.onet.pl/register-email.html?app_id=poczta.onet.pl.front")
        print("jestesmy w onetemail konstruktor")

    def fill_inputs(self, info):
        login = info.getElementsByTagName('login')[0].firstChild.data
        print("login: " + login)

    def solve_captcha(self):

        print("solved")
