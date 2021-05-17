import logging

class LogGen:

    @staticmethod
    def logGen():
        logging.basicConfig(filename=".\\logs\\automation.log",format='%(asctime)s: %(levelname)s: %(message)s')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

