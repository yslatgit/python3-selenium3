# -*- coding: UTF-8 -*-
# author:ysl
# 2019-10-08


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from .BaseElementEnum import Element as be


class OperateElement(object):
    """
    页面的基类
    """
    # def __init__(self, driver, url):
    #     """传入浏览器驱动以及网址初始化"""
    #     self.driver = driver
    #     self.url = url

    def __init__(self, driver):
        """传入浏览器驱动以及网址初始化"""
        self.driver = driver

    def find_element(self, operate):
        """定位页面元素"""
        try:
            t = operate["check_time"] if operate.get("check_time", "0") != "0" else be.TIMEOUT
            if type(operate) == list:  # 多条用例
                for item in operate:
                    t = item["check_time"] if item.get("check_time", "0") != "0" else be.TIMEOUT
                    WebDriverWait(self.driver, t).until(lambda x: self.elements_by(item))
                    return {"result": True}
            if type(operate) == dict:  # 单条用例
                WebDriverWait(self.driver, t).until(lambda x: self.elements_by(operate))
                return {"result": True}

        except Exception:
            pass
            return {"result": False}

    def elements_by(self, operate):
        """定位页面方法的重新封装"""
        elements = {
            be.find_element_by_id: lambda: self.driver.find_element_by_id(operate["element_info"]),
            be.find_elements_by_id: lambda: self.driver.find_elements_by_id(operate["element_info"]),
            be.find_element_by_xpath: lambda: self.driver.find_element_by_xpath(operate["element_info"]),
            be.find_element_by_partial_link_text: lambda: self.driver.find_element_by_partial_link_text(operate["element_info"])
        }
        return elements[operate["find_type"]]()

    def operate(self, operate):
        """操作页面元素"""
        res = self.find_element(operate)
        if res["result"]:
            return self.operate_by(operate)
        else:
            return res

    def operate_by(self, operate):
        """页面元素操作方法的封装"""
        if operate.get("operate_type", "0") == "0":
            return {"result": True}
        elements = {
            be.CLICK: lambda: self.click(operate),
            # be.CLEAR: lambda: self.clear(operate),
            be.GET_TEXT: lambda: self.get_text(operate),
            be.GET_VALUES: lambda: self.get_value(operate),
            be.MOVE_TO_ELEMENT: lambda: self.move_to_element(operate),
            be.SEND_KEYS: lambda: self.send_keys(operate)
        }
        return elements[operate["operate_type"]]()

    def click(self, operate):
        if operate["find_type"] == be.find_element_by_partial_link_text or \
           operate["find_type"] == be.find_element_by_xpath or operate["find_type"] == be.find_element_by_id:
            self.elements_by(operate).click()
        elif operate["find_type"] == be.find_elements_by_id:
            self.elements_by(operate)[operate["index"]].click()
        return {"result": True}

    # def clear(self, operate):
    #     self.elements_by(operate).clear()
    #     return {"result":True}

    def send_keys(self, operate):
        self.elements_by(operate).send_keys(operate["msg"])
        return {"result": True}

    def get_text(self, operate):
        element_info = self.elements_by(operate)
        text = element_info.text
        if text == operate["msg"]:
            return {"result": True, "text": text}
        else:
            return {"result": False, "text": text}

    def get_value(self, operate):
        element_info = self.elements_by(operate)
        value = element_info.get_attribute("value")
        return {"result": True, "value": value}

    def move_to_element(self, operate):
        ActionChains(self.driver).move_to_element(self.elements_by(operate)).perform()
        return {"result": True}

