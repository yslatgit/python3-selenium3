# -*- coding: UTF-8 -*-
# author:ysl
# 2019-10-09

import os
import sys
import unittest
from datetime import datetime
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Runner.HTMLTestRunner import HTMLTestRunner
from Base.BaseLog import MyLog


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AllTest:
    def __init__(self, case_list_conf=PATH("./caselist.txt"), case_dir=PATH("../TestCase")):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.suite = unittest.TestSuite()
        self.case_dir = case_dir
        self.case_list_conf = case_list_conf
        self.case_list = []

    def set_list(self):
        with open(self.case_list_conf) as f:
            lines = f.readlines()
            self.logger.info(lines)
            for line in lines:
                if line.startswith("#"):
                    pass
                else:
                    self.case_list.append(line.replace("\n", ""))
            f.flush()
            f.close()
        if len(self.case_list) == 0:
            self.logger.info("请检查caselist.txt配置文件")

    def aaa(self):
        print(self.case_list)

    def set_suite(self):
        self.set_list()
        # test_dir = r"../TestCase"
        suite_module = []

        for case in self.case_list:
            try:
                discover = unittest.defaultTestLoader.discover(self.case_dir, pattern=case + ".py", top_level_dir=None)
                suite_module.append(discover)
            except Exception as msg:
                self.logger.error(msg)
                self.logger.error("请检查当前的查找路径下是否有测试类文件")

        if len(suite_module) > 0:
            for suite in suite_module:
                for case_name in suite:
                    self.suite.addTest(case_name)
        else:
            pass

    def run(self):
        self.log.build_start_line("all")
        self.set_suite()
        try:
            report_path = r"../reports/AllTestReport.html"
            if self.suite is not None:
                with open(report_path, 'wb') as f:
                    runner = HTMLTestRunner(stream=f, title="泰禾考勤系统测试报告", tester="ysl")
                    runner.run(self.suite)
            else:
                self.logger.info("没有测试用例，无法执行测试")
        except Exception as ex:
            self.logger.error(ex)
        finally:
            self.log.build_end_line("all")




"""


def runner_case(name):
    # report_name = name
    report_path = os.path.join("../reports/", name)
    start_time = datetime.now()
    suite = unittest.TestSuite()
    test_dir = r"../TestCase"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="*Test.py")
    with open(report_path, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title="泰禾考勤系统测试报告", tester="ysl")
        runner.run(discover)
    # end_time = datetime.now()
    # print(end_time-start_time)
"""

if __name__ == '__main__':
    # runner_case(name="测试2.html")
    a = AllTest()
    a.run()

