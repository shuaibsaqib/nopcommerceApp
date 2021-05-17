from selenium import webdriver
import pytest
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURl = ReadConfig.getAppUrl()
    userName = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()


    def test_HomePageTitle(self):
        self.logger.info("****Test_001_Login****")
        self.driver = webdriver.Chrome(executable_path=".\\venv\\chromedriver_win32\\chromedriver")
        self.driver.get(self.baseURl)
        act_title = self.driver.title
        if act_title == "Your store. Login" :
            assert True
            self.driver.close()
            self.logger.info("*****Test is passed******")
        else:
            self.driver.save_screenshot(".\screenshots\page.png")
            self.driver.close()
            self.logger.error("*****Test is Failed******")
            assert False


    def test_login(self):
        self.driver= webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
        self.driver.get(self.baseURl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration" :
            self.driver.close()
            self.logger.info("*****Test is passed******")
            assert True

        else:
            self.driver.save_screenshot(".\screenshots\loginPage.png")
            self.driver.close()
            self.logger.error("*****Test is Failed******")
            assert False
