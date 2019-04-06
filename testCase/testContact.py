#  -*- coding:utf-8 -*-
import unittest
import paramunittest
import readConfig as readConfig
from common import Log as Log
from common import common
from appium import webdriver
import time
import os
from datetime import datetime
from ParametrizedTestCase import ParametrizedTestCase
from testCaseAPI.ISextisting import ISextisting

localReadConfig = readConfig.ReadConfig()

class testContact(ParametrizedTestCase):
    def setUp(self):
        """

                :return:
                """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        self.logger.info("testCall测试开始前准备")
        print("initialize")

        caps = {}
        caps["platformName"] =self.param01      # 平台 "Android"
        caps["platformVersion"] = self.param02    # 版本号 "8.1.0"
        caps["deviceName"] = self.param03         #手机型号 "msm8909go_benz"
        caps["appPackage"] =  "com.android.contacts"
        caps["appActivity"] = "com.android.contacts.activities.PeopleActivity"
        caps["udid"] = self.param04                # 测试的手机ID
        caps["unicodeKeyboard"] = True  # appium虚拟键盘
        caps["resetKeyboard"] = True  # appium虚拟键盘

        self.webid = 'http://localhost:' + str(self.param05) + '/wd/hub'   # param05为端口号
        self.driver = webdriver.Remote(self.webid, caps)
        self.deviceID = self.param04
        print("open app")
        time.sleep(10)

    def test01(self):
        #第一步：点击通讯录新建按钮
        self.driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='电话']").click()
        except:
            print('is not frist made contacts')
        time.sleep(2)
        #需要加一个判断语句，查看当前界面是不是有创建新联系人字样。
        element = "//android.widget.TextView[@text='创建新联系人']"
        Tag = ISextisting(self.driver, element,self.deviceID,"testContact001").XpathTag()
        self.assertTrue(Tag)
        time.sleep(2)

        #创建联系人，添加各种字段
        #self.driver.find_element_by_xpath("//android.widget.EditText[@text='姓氏']").click()
        #time.sleep(2)
        #self.driver.find_element_by_xpath("//android.widget.EditText[@text='姓氏']").send_keys('xiaoming')
        #self.driver.press_keycode("4")
        time.sleep(2)
        self.driver.find_element_by_id("com.android.contacts:id/kind_icon").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='电话']").send_keys('10086')
        self.driver.press_keycode("4")
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='电子邮件']").send_keys('123456789@126.com')
        time.sleep(2)
        self.driver.find_element_by_id("com.android.contacts:id/editor_menu_save_button").click()
        time.sleep(5)
        #判断联系人是否新建成功
        element ="com.android.contacts:id/photo_touch_intercept_overlay"
        Tag = ISextisting(self.driver, element, self.deviceID, "testContact002").IdTag()
        self.assertTrue(Tag)
    def tearDown(self):
        self.logger.info("测试结束，输出log完结\n\n")
        self.driver.quit()
        print("close app!")
        time.sleep(5)


