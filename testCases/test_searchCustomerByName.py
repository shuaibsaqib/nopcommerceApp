import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
from pageObjects.SearchCustomer import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseURl = ReadConfig.getAppUrl()
    userName = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()


    def test_searchCustomerByName(self):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver=webdriver.Chrome(executable_path=".\\venv\\chromedriver_win32\\chromedriver")
        self.driver.get(self.baseURl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(2)

        self.logger.info("************* searching customer by Name **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")
