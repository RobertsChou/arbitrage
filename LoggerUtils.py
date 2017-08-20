#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果
import logging


class LoggerUtils:

    def __init__(self, name):
        self.__name = name
        self.__formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


    def getLogger():
        return logger.getLogger(self.__name)

    def logInfo(log = ''):
        if log:
            logging.info(self.__name,':', log)


    def logWarning(log = ''):
        if log:
            logging.warning(self.__name,':',log)


    def logDebug(log =''):
        if log:
            logging.debug(self.__name,':', log)



