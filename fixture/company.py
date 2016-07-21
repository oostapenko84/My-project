__author__ = 'olga.ostapenko'

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CompanyHelper:
    def __init__(self, app):
        self.app = app

    def create(self, company):
        wd = self.app.wd
        # [0] - need to refer to any (1-st) element in the array to call function click()
        wd.find_elements_by_xpath("//a[contains(text(), 'Companies')]")[0].click()
        # add CAD
        WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'ADD NEW')]")))
        WebDriverWait(wd, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.popup-loader")))
        wd.find_elements_by_xpath("//button[contains(text(), 'ADD NEW')]")[0].click()
        wd.find_element_by_id('inputCompanyName').send_keys(company.Company_Name)
        wd.find_element_by_id("inputFirstName").send_keys(company.CAD_First_Name)
        wd.find_element_by_id("inputFirstName").send_keys(company.CAD_Last_Name)
        wd.find_element_by_id("inputLogin").send_keys(company.Email)
        wd.find_element_by_id('inputPhone').send_keys(company.Phone)
        # add Location (Address)
        wd.find_element_by_xpath("//div[@class='form-horizontal']//span[.='+ add address']").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[1]/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[1]/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[1]/div[2]/input").send_keys(company.Address)
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[2]/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[2]/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[2]/div[2]/input").send_keys(company.City)
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[4]/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[4]/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[4]/div[2]/input").send_keys(company.Zip_Code)
        wd.find_element_by_xpath("//div[@class='modal-content']//button[.='ADD']").click()
        wd.find_element_by_id('inputSite').send_keys(company.Web_Site)
        wd.find_element_by_id('inputDescription').send_keys(company.Description)
        wd.find_element_by_id('inputPoints').send_keys(company.Points)
        # upload Avatar
        WebDriverWait(wd, 10).until(EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, "div.fade modal-backdrop ng-animate ng-leave ng-leave-active")))
        #wd.find_element_by_css_selector("input.btn-upload").click()
        wd.find_element_by_class_name("btn-upload").send_keys("C:/Users/olga.ostapenko/Desktop/Pics/test2.jpg")
        WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located ((By.CSS_SELECTOR, "div.modal-footer")))
        wd.find_element_by_xpath("//div[@class='modal-footer']//button[.='OK']").click()
        # save CAD
        WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'SAVE & EXIT')]")))
        WebDriverWait(wd, 10).until(EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, "div.fade modal-backdrop ng-animate ng-leave ng-leave-active")))
        wd.find_element_by_xpath("//div[@class='nav-bar-button']//button[@type='submit']").click()
        WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((By.ID, "header_logout")))
        WebDriverWait(wd, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.popup-loader")))
