from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains


class LoginMethode(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.username = "//input[@name='username']"
        self.password = "//input[@name='password']"
        self.login_button = "//ancestor::div/child::div/following::button"
        self.PIM = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span"
        self.Add = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
        self.firstname = "//input[@name='firstName']"
        self.MiddleName = "//input[@name='middleName']"
        self.lastName = "//input[@name='lastName']"
        self.save = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
        self.Edit = "//div[contains(text(),'0070')]"
        self.AntonyMiddleName = "//input[@name='middleName']"

    #testcase=TC_Login_01
    #login with valid username and password
    def test_login_methode1(self):
        self.driver.find_element(By.XPATH, self.username).send_keys("Admin")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.password).send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login_button).click()

        time.sleep(2)
        self.driver.save_screenshot("successfull_login.png")
    #Testcase2=TC_Login_02
    #wrong username and password for the login
    def test_Login_Methode2(self):

        self.driver.find_element(By.XPATH, self.username).send_keys("dmin")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.password).send_keys("admin12")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        self.driver.save_screenshot("invalid_login.png")

    #testcase:TC_PIM_01
    #Added new employee
    def test_Add_New_Employee(self):
        self.driver.find_element(By.XPATH, self.username).send_keys("Admin")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.password).send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login_button).click()

        time.sleep(2)
        self.driver.find_element(By.XPATH,self.PIM).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Add).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.firstname).send_keys('Krishna')
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.MiddleName).send_keys('Teja')
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.lastName).send_keys('rajamreddy')
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.save).click()
        time.sleep(2)
        self.driver.save_screenshot("ADD_NEW_EMPLOYEE.png")

    #testcase:TC_PIM_02
    #Edited employee details
    def test_Edit_Employee(self):
        self.driver.find_element(By.XPATH, self.username).send_keys("Admin")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.password).send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login_button).click()

        time.sleep(2)
        self.driver.find_element(By.XPATH,self.PIM).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Edit).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.AntonyMiddleName).send_keys('Updated')
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.save).click()
        time.sleep(2)
        self.driver.save_screenshot("EDIT_EMPLOYEE.png")

    #testcase:TC_PIM_03
    #Deleting an existing employee on the PIM module
    def test_delete_employee(self):
        self.driver.find_element(By.XPATH, self.username).send_keys("Admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password).send_keys("admin123")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button).click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, self.PIM).click()
        time.sleep(3)
        selector = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[9]/div[1]/button[1]")
        selector.click()
        time.sleep(2)
        popup = self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes, Delete']")
        popup.click()
        time.sleep(1)
        self.driver.save_screenshot("delete_employee.png")












    def tearDown(self):
         self.driver.quit()



