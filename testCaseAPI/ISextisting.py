#  -*- coding:utf-8 -*-
#判断某个元素是否存在当前页面，存在返回true，不存在返回False
#未实现的结果判定——1.判断某个关键字是否在当前页面 2.某个某个元素是否在指定页面 3.等等后续用例中要用到的断言
from testCaseAPI import Screenshot
class ISextisting:
    def __init__(self,driver,element,deviceID,screenName):
        self.driver = driver
        self.element = element
        self.deviceID = deviceID
        self.screenName = screenName
    #通过ID方式查看当前页面是否存在此元素
    def IdTag(self):
        try:
            self.driver.find_element_by_id(self.element)
            Screenshot.Screenshot(self.driver, self.deviceID, self.screenName)
            return True
        except:
            Screenshot.Screenshot(self.driver,self.deviceID,self.screenName)
            return False
    #通过xpath方式查看当前页面是否存在此元素
    def XpathTag(self):
        try:
            self.driver.find_element_by_xpath(self.element)
            Screenshot.Screenshot(self.driver, self.deviceID, self.screenName)
            return True
        except:
            Screenshot.Screenshot(self.driver,self.deviceID,self.screenName)
            return False


