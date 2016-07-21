__author__ = 'olga.ostapenko'

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class VendorHelper:
    def __init__(self, app):
        self.app = app

    def create(self, vendor):
        wd = self.app.wd
        # [0] - need to refer to any (1-st) element in the array to call function click()
        wd.find_elements_by_xpath("//a[contains(text(), 'Vendors')]")[0].click()
        # add VAD
        WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'ADD NEW')]")))
        WebDriverWait(wd, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.popup-loader")))
        wd.find_elements_by_xpath("//button[contains(text(), 'ADD NEW')]")[0].click()
        wd.find_element_by_id('inputCompanyName').send_keys(vendor.Company_Name)
        wd.find_element_by_id('inputPhone').send_keys(vendor.Phone)
        # add Location (Address)
        wd.find_element_by_xpath("//div[@class='form-horizontal']//span[.='+ add address']").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[1]/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[1]/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[1]/div[2]/input").send_keys(vendor.Address)
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[2]/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[2]/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[2]/div[2]/input").send_keys(vendor.City)
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[4]/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[4]/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[4]/div[2]/input").send_keys(vendor.Zip_Code)
        wd.find_element_by_xpath("//div[@class='modal-content']//button[.='ADD']").click()
        wd.find_element_by_id('inputWebSite').send_keys(vendor.Web_Site)
        wd.find_element_by_id('inputDescription').send_keys(vendor.Description)

        # enter Administration Staff
        # wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[1]/div[1]/input").click()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[1]/div[1]/input").clear()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[1]/div[1]/input").send_keys(
            vendor.VAD_First_Name)
        # wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[1]/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[1]/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[1]/div[2]/input").send_keys(
            vendor.VAD_Last_Name)
        # wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[2]/div[1]/input").click()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[2]/div[1]/input").clear()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[2]/div[1]/input").send_keys(
            vendor.Email)
        # wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[3]/div[1]/div/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[3]/div[1]/div/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[3]/div[1]/div/div[2]/input").send_keys(
            vendor.VAD_Phone)
        # upload Avatar
        WebDriverWait(wd, 10).until(EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, "div.fade modal-backdrop ng-animate ng-leave ng-leave-active")))

        # открываем страницу с формой загрузки файла
        wd.get("file://" + os.getcwd() + "/index.html")

        # находим элемент <input type="file">
        element = wd.find_element_by_id("file")

        # заполняем элемент путём до загружаемого файла
        element.send_keys(os.getcwd() + "/test2.jpg")

        # находим элемент <input type="file">
        element = wd.find_element_by_id("submit")

        # нажимаем на элемент (отправляем форму)
        element.click()

        wd.find_element_by_css_selector("input.btn-upload").click()
        wd.find_element_by_class_name("btn-upload").send_keys("C:/Users/olga.ostapenko/PycharmProjects/Espresa/Pics/test.jpg")
        #wd.find_element_by_xpath("//div[@class='modal-footer']//button[.='OK']").click()
        # save VAD
        WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'SAVE & EXIT')]")))
        WebDriverWait(wd, 10).until(EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, "div.fade modal-backdrop ng-animate ng-leave ng-leave-active")))
        wd.find_element_by_xpath("//div[@class='nav-bar-button']//button[@type='submit']").click()
        WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((By.ID, "header_logout")))
        WebDriverWait(wd, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.popup-loader")))