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

#login_xls = common.get_uiidconfig_xml("calling",activity)

localReadConfig = readConfig.ReadConfig()
#configHttp = ConfigHttp.ConfigHttp()
#info = {}
cofig8909 = localReadConfig.get_phone("8909")


#@paramunittest.parametrized(*cofigAL1860)
class testCall(unittest.TestCase):
    def setUp(self):
        """

        :return:
        """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        self.logger.info("testCall测试开始前准备")
        print("initialize")

        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "8.1.0"
        caps["deviceName"] = "msm8909go_benz"
        caps["appPackage"] = "com.android.dialer"
        caps["appActivity"] = "com.android.dialer.app.DialtactsActivity"
        caps["unicodeKeyboard"] = "True"
        caps["resetKeyboard"] = "True"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        print("open app")
        time.sleep(10)

    def testcall(self):
        """
        test body
        :return:
        """
        # # set url
        # self.url = common.get_url_from_xml('login')
        # configHttp.set_url(self.url)
        # print("第一步：设置url  "+self.url)
        #
        # # get visitor token
        # if self.token == '0':
        #     token = localReadConfig.get_headers("token_v")
        # elif self.token == '1':
        #     token = None
        #
        # # set headers
        # header = {"token": str(token)}
        # configHttp.set_headers(header)
        # print("第二步：设置header(token等)")
        #
        # # set params
        # data = {"email": self.email, "password": self.password}
        # configHttp.set_data(data)
        # print("第三步：设置发送请求的参数")
        #
        # # test interface
        # self.return_json = configHttp.post()
        # method = str(self.return_json.request)[int(str(self.return_json.request).find('['))+1:int(str(self.return_json.request).find(']'))]
        # print("第四步：发送请求\n\t\t请求方法："+method)
        #self.PPP=self.method+self.token+self.email+self.password
        # check result
        #self.checkResult()
        #print("第五步：检查结果")
        #self.assertEqual(self.PPP, self.result)
        self.operatorNumber = "10086"
        self.driver.find_element_by_id("com.android.dialer:id/floating_action_button").click()
        time.sleep(10)
        for num in self.operatorNumber:
            if num == '*':
                self.driver.find_element_by_id("com.android.dialer:id/star").click()
                time.sleep(2)
            elif num == '#':
                self.driver.find_element_by_id("com.android.dialer:id/pound").click()
                time.sleep(2)
            else:
                self.key_code = int(num) + 7
                self.driver.keyevent("%d" % self.key_code)
                time.sleep(2)

        self.driver.find_element_by_id("com.android.dialer:id/dialpad_floating_action_button").click()
        time.sleep(10)

        self.element=self.driver.find_element_by_id("com.android.dialer:id/contactgrid_bottom_timer")

        self.path = Log.Log.get_screen_path("testCall")
        self.driver.get_screenshot_as_file(self.path)

        self.assertTrue(self.element)
        self.driver.find_element_by_id("com.android.dialer:id/incall_end_call").click()
        time.sleep(10)

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
