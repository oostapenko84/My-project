__author__ = 'olga.ostapenko'

from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.vendor import VendorHelper
from fixture.company import CompanyHelper

# from fixture.contact import CompanyHelper


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.vendor = VendorHelper(self)
        self.company = CompanyHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://qa.espresa.com")

    def destroy(self):
        self.wd.quit()
