from selenium import webdriver
import pytest
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import  time

class Test_002_DDT_Login:
    baseURl = ReadConfig.getAppUrl()
    path = ".//testData/login_data_DDT.xlsx"
    logger = LogGen.logGen()

    def test_DDT_login(self):
        self.driver= webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
        self.driver.get(self.baseURl)
        self.driver.implicitly_wait(5)
        self.lp = LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')


        list_status=[]
        for r in range(2,self.rows+1):
            self.userName=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.userName)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title== exp_title :
                if self.exp=='pass':
                    self.logger.info("********Passed********")
                    self.lp.clickLogout()
                    list_status.append('pass')

                elif self.exp=='fail':
                    self.logger.info("***********Failed**********")
                    self.lp.clickLogout()
                    list_status.append('fail')

            elif act_title != exp_title:
                if self.exp == 'fail':
                    self.logger.info("********Passed********")
                    list_status.append('pass')

                elif self.exp == 'pass':
                    self.logger.info("***********Failed**********")
                    list_status.append('fail')

        if 'fail' not in list_status:
            self.logger.info("Login_DDT_test Passed")
            self.driver.close()
            assert True

        else:
            self.logger.error("Login_DDT_Test is failed")
            self.driver.close()
            assert False

        self.logger.info("**********End of TC_002_DDT_login**********")









