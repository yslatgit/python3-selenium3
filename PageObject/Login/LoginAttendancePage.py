# -*- coding: UTF-8 -*-
# author:ysl
# 2019-10-08

from PageObject.Pages import PagesObjects
from Base.BaseYaml import get_yaml


class LoginAttendancePage:
    def __init__(self, kw):
        _init = {"driver": kw["driver"], "test_msg": get_yaml(kw["path"])}
        self.page = PagesObjects(_init)

    def operate(self):
        self.page.operate()
