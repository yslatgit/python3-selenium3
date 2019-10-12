# -*- coding: UTF-8 -*-
# author:ysl
# 2019-10-08


class Element:
    # 登录信息
    BASE_URL = r"http://ucssotest.tahoecndemo.com:9988/logout?ReturnURL=http%3A%2F%2Foa.tahoecndemo.com%3A8080%2Fportal%2Findex.html&sysId=OA"
    USERNAME = r"duyi"
    PASSWORD = r"123456"

    # 等待元素出现的时间
    TIMEOUT = 10

    # 下载文件的路径
    DOWNLOAD_PATH = r"C:\Users\Administrator\Downloads"

    # 数据库配置信息
    DATABASE_INFO = r"Driver={SQL Server};Server=10.0.104.238;Port=1433;UID=KQ;PWD=KQpassword;"

    # 定位元素的方法
    find_element_by_id = "id"
    find_elements_by_id = "ids"
    find_element_by_xpath = "xpath"
    find_element_by_partial_link_text = "partial_link_text"

    # 页面元素操作
    CLICK = "click"
    GET_TEXT = "get_text"
    SEND_KEYS = "send_keys"
    GET_VALUES = "get_values"
    MOVE_TO_ELEMENT = "move_to_element"
    DOUBLE_CLICK = "double_click"
    CLEAR = "clear"

    # Email信息
    EmailConf = {
        "mail_host": "qq.com",
        "mail_user": "9999999@qq.com",
        "mail_sender": "9999999@qq.com",
        "mail_pass": "123123123",
        "mail_port": "465",
        "mail_receiver": "121313121@qq.com",
        "mail_subject": "自动化测试报告"
    }
