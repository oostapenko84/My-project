__author__ = 'olga.ostapenko'


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("public_site_login").click()
        wd.find_element_by_id("login_login").click()
        wd.find_element_by_id("login_login").clear()
        wd.find_element_by_id("login_login").send_keys(username)
        wd.find_element_by_id("login_password").click()
        wd.find_element_by_id("login_password").clear()
        wd.find_element_by_id("login_password").send_keys(password)
        wd.find_element_by_id("login_submit").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_id("header_logout").click()
