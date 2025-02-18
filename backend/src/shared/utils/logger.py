import logging
import os
from logging.handlers import TimedRotatingFileHandler


class Logger:
    _instance = None

    @staticmethod
    def getLogger(
        logDir: str = "./src/shared/data/log/",
        logFile: str = "its_api.log",
        when: str = "midnight",
        backupCount: int = 7,
        logLevel: int = logging.INFO,
    ):
        if not Logger._instance:
            Logger._instance = Logger.initializeLogger(logDir, logFile, when, backupCount, logLevel)
        return Logger._instance
    
    @staticmethod
    def initializeLogger(
        logDir: str, logFile: str, when: str, backupCount: int, logLevel: int
    ):
        os.makedirs(logDir, exist_ok=True)

        logger = logging.getLogger(logFile)
        logger.setLevel(logLevel)

        logPath = os.path.join(logDir, logFile)
        fileHandler = TimedRotatingFileHandler(
            logPath, when=when, interval=1, backupCount=backupCount
        )
        fileHandler.setLevel(logLevel)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logLevel)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fileHandler.setFormatter(formatter)
        consoleHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.addHandler(consoleHandler)

        return logger