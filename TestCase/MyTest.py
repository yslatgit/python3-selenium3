# -*- coding: UTF-8 -*-
# author:ysl
# 2019-10-08

import unittest
import os
import time
from Base.BaseRunner import ParametrizedTestCase

from PageObject.Login.LoginAttendancePage import LoginAttendancePage
from PageObject.Attendance.DailyAttendanceManagement.EmployeeInformationManagement.EIMPage import EIMPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MyTest(ParametrizedTestCase):

    @classmethod
    def setUpClass(cls):
        super(MyTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def loginAttendance(self):
        self.logger.info("登录后跳转页面到员工信息页")
        app = {"driver": self.driver, "path": PATH("../Yamls/LoginAttendance.yaml")}
        page = LoginAttendancePage(app)
        page.operate()

    # @unittest.skip("pass")
    def testEim(self):
        self.logger.info("开始测试")
        self.loginAttendance()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        app = {"driver": self.driver, "path": PATH("../Yamls/Attendance/DailyAttendanceManagement/EmployeeInformationManagement/EIM.yaml")}
        page = EIMPage(app)
        page.operate()
        time.sleep(1)
        self.logger.info("测试结束")
        # print(self.driver.current_url)


if __name__ == '__main__':
    unittest.main()
