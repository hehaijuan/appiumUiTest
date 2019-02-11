#  -*- coding:utf-8 -*-
import unittest
import paramunittest
import readConfig as readConfig
from common import Log as Log
from common import common
#from common import configHttp as ConfigHttp
from appium import webdriver
import time
import os
from datetime import datetime

#login_xls = common.get_xls("userCase.xlsx", "Summation")
localReadConfig = readConfig.ReadConfig()
#configHttp = ConfigHttp.ConfigHttp()
#info = {}
cofig8909 = localReadConfig.get_phone("8909")


#@paramunittest.parametrized(*cofigAL1860)
class testContact(unittest.TestCase):
    def setUp(self):
        """

        :return:
        """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        self.logger.info("testCall01测试开始前准备")
        print("initialize")

        caps = {}
        caps["platformName"] = cofig8909["platformname"]
        caps["platformVersion"] = cofig8909["platformversion"]
        caps["deviceName"] = cofig8909["devicename"]
        caps["appPackage"] =  "com.android.contacts"
        caps["appActivity"] = "com.android.contacts.activities.PeopleActivity"
        caps["unicodeKeyboard"] = cofig8909["unicodekeyboard"]
        caps["resetKeyboard"] = cofig8909["resetkeyboard"]

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.operatorNumber = cofig8909["operatornumber"]
        print("open app")
        time.sleep(10)

    def test01(self):
        self.driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='电话']").click()
        except:
            print('is not frist made  contacts')
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='姓氏']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='姓氏']").send_keys('xiaoming')
        time.sleep(2)
        self.driver.find_element_by_id("com.android.contacts:id/kind_icon").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='电话']").send_keys('10086')
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='电子邮件']").send_keys('123456789@126.com')
        time.sleep(1)
        self.driver.find_element_by_id("com.android.contacts:id/editor_menu_save_button").click()
        time.sleep(2)

        self.element = self.driver.find_element_by_id("com.android.contacts:id/large_title")
        self.path = Log.Log.get_screen_path("testcontact01")
        self.driver.get_screenshot_as_file(self.path)

        self.assertTrue(self.element)

        #self.driver.keyevent('4')

    # 新建卡联系人
    def test02(self):
        self.driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='SIM卡']").click()
        except:
            print('is not frist made  contacts')
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='姓名']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='姓名']").send_keys('xiaoming')
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='电话']").send_keys('10086')
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='电子邮件']").send_keys('123456789@126.com')
        time.sleep(1)
        self.driver.find_element_by_id("com.android.contacts:id/editor_menu_save_button").click()
        time.sleep(1)

        self.element = self.driver.find_element_by_id("com.android.contacts:id/large_title")
        self.path = Log.Log.get_screen_path("testcontact02")
        self.driver.get_screenshot_as_file(self.path)

        self.assertTrue(self.element)



    # 删除全部联系人
    def test03(self):
        self.driver.find_element_by_id("com.android.contacts:id/menu_delete").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.android.contacts:id/selection_menu").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.android.contacts:id/popup_list_title").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.android.contacts:id/btn_ok").click()
        time.sleep(2)
        self.driver.find_element_by_id("android:id/button1").click()

        self.element = self.driver.find_element_by_id("com.android.contacts:id/empty_home_view_text")
        self.path = Log.Log.get_screen_path("testcontact03")
        self.driver.get_screenshot_as_file(self.path)

        self.assertTrue(self.element)


    def tearDown(self):
        """

        :return:
        """
        # info = self.info
        # if info['code'] == 0:
        #     # get uer token
        #     token_u = common.get_value_from_return_json(info, 'member', 'token')
        #     # set user token to config file
        #     localReadConfig.set_headers("TOKEN_U", token_u)
        # else:
        #     pass
        # self.log.build_case_line(self.case_name, self.info['code'], self.info['msg'])
        self.driver.keyevent('4')
        self.driver.keyevent('4')
        self.driver.keyevent('4')
        self.logger.info("测试结束，输出log完结\n\n")
        self.driver.quit()
        print("close app!")
        time.sleep(5)

    # def checkResult(self):
    #     """
    #     check test result
    #     :return:
    #     """
    #     self.info = self.return_json.json()
    #     # show return message
    #     common.show_return_msg(self.return_json)
    #
    #     if self.result == '0':
    #         email = common.get_value_from_return_json(self.info, 'member', 'email')
    #         self.assertEqual(self.info['code'], self.code)
    #         self.assertEqual(self.info['msg'], self.msg)
    #         self.assertEqual(email, self.email)
    #
    #     if self.result == '1':
    #         self.assertEqual(self.info['code'], self.code)
    #         self.assertEqual(self.info['msg'], self.msg)
