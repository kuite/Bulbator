from lxml import etree
from selenium import webdriver
from OnetEmailCreator import OnetEmailCreator


def create_bulk(accounts_info):
    driver = webdriver.Chrome("C:\\Users\\kuite\\Desktop\\chromedriver.exe")

    accounts = accounts_info.getElementsByTagName('information')
    root = etree.Element('emails')

    for i in range(0, accounts.length):
        info = accounts[i]
        email_xml = create_mail_onet(driver, info)
        root.append(email_xml)

    xml = etree.tostring(root, pretty_print=True)

    # print("wygenerowano {} maili".format(num))
    return xml


def create_mail_onet(driver, info):
    email = OnetEmailCreator(driver)
    email.fill_inputs(info)
    if email.account_created:
        email_node = etree.Element('email')
        login_element = etree.Element('login')
        password_element = etree.Element('password')

        login_element.text = email.login
        password_element.text = email.password

        email_node.append(login_element)
        email_node.append(password_element)

        return email_node

    return "error"
