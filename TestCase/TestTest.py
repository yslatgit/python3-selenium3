# -*- coding: UTF-8 -*-
# author:ysl
# 2019-10-11

import os
import unittest
import ddt
from Base.BaseYaml import get_yaml


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


@ddt.ddt
class TestTest(unittest.TestCase):
    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")

    @ddt.file_data("../Yamls/Test.yaml")
    def test_a(self, value):
        print(value)


if __name__ == '__main__':
    print(get_yaml("../Yamls/Test.yaml"))
    unittest.main()
