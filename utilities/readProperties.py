import configparser

config=configparser.RawConfigParser()
config.read(".\configurations\config.ini")

class ReadConfig:

    @staticmethod
    def getAppUrl():
        url = config.get('Common Info','baseURL')
        return  url
    @staticmethod
    def getUsername():
        username = config.get('Common Info','userName')
        return  username

    @staticmethod
    def getPassword():
        password = config.get('Common Info', 'password')
        return  password
