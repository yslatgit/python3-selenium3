# -*- coding: UTF-8 -*-
# author:ysl
# 2019-10-08

import os
from Base.BaseElementEnum import Element as be
from Base.BaseOperate import OperateElement

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)


class PagesObjects:
    def __init__(self, kw):
        self.driver = kw["driver"]
        self.operateElement = ""
        self.Operate = True
        self.test_msg = kw["test_msg"]
        # print(self.test_msg)
        self.testCase = self.test_msg[1]["testcase"]

    def operate(self):
        if self.test_msg[0] is False:
            self.Operate = False
            return False
        self.operateElement = OperateElement(self.driver)
        for item in self.testCase:
            result = self.operateElement.operate(item)
            # print(result)
        return True
