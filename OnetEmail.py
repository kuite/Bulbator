class OnetEmail:
    inputs = {
        'full name': '#f_nameSurname',
        'login': '#login_user'
    }
    account_created = False

    def __init__(self, webdriver):
        self.webdriver = webdriver
        webdriver.get("https://konto.onet.pl/register-email.html?app_id=poczta.onet.pl.front")
        print("jestesmy w onetemail konstruktor")

    def fill_inputs(self, info):
        login = info.getElementsByTagName('login')[0].firstChild.data
        print("login: " + login)
