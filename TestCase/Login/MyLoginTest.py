# -*- coding: UTF-8 -*-
# author:ysl
# 2019-10-08

import unittest
import os
import time
from Base.BaseRunner import ParametrizedTestCase
from PageObject.Login.LoginPage import LoginPage
from PageObject.Login.LoginAttendancePage import LoginAttendancePage
from PageObject.Attendance.DailyAttendanceManagement.EmployeeInformationManagement.EIMPage import EIMPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MyLoginTest(ParametrizedTestCase):

    @classmethod
    def setUpClass(cls):
        super(MyLoginTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def testLoginAttendance(self):
        app = {"driver": self.driver, "path": PATH("../../Yamls/LoginAttendance.yaml")}
        page = LoginAttendancePage(app)
        page.operate()


if __name__ == '__main__':
    unittest.main()
