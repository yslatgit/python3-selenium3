# -*- coding: UTF-8 -*-
# author:ysl
# 2019-10-08

import unittest
from Base.BaseElementEnum import Element as be
from Base.BaseLog import MyLog
from selenium import webdriver


def get_driver():
    """声明测试用的浏览器"""
    # options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome()
    url = be.BASE_URL
    driver.get(url)
    return driver


def get_logger():
    """声明logger"""
    logger = MyLog.get_log().get_logger()
    return logger


class ParametrizedTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.logger = get_logger()

    @classmethod
    def tearDownClass(cls):
        pass

    # @staticmethod
    # def parametrize(testcase_class):
    #     testloader = unittest.TestLoader()
    #     testnames = testloader.getTestCaseNames(testcase_class)
    #     suite = unittest.TestSuite()
    #     for name in testnames:
    #         suite.addTest(testcase_class(name))
    #     return suite
