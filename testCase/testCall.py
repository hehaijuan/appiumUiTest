#  -*- coding:utf-8 -*-
import readConfig as readConfig
from common import Log as Log
from appium import webdriver
import time
from testCaseAPI.ISextisting import ISextisting
from testCaseAPI.Screenshot import Screenshot
from ParametrizedTestCase import ParametrizedTestCase

#login_xls = common.get_uiidconfig_xml("calling",activity)

localReadConfig = readConfig.ReadConfig()
cofig8909 = localReadConfig.get_phone("8909")


#@paramunittest.parametrized(*cofigAL1860)
class testCall(ParametrizedTestCase):
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
        caps["appPackage"] = "com.android.dialer"
        caps["appActivity"] = "com.android.dialer.app.DialtactsActivity"
        caps["udid"] = self.param04                # 测试的手机ID
        caps["unicodeKeyboard"] = True  # appium虚拟键盘
        caps["resetKeyboard"] = True  # appium虚拟键盘

        self.webid = 'http://localhost:' + str(self.param05) + '/wd/hub'   # param05为端口号
        self.driver = webdriver.Remote(self.webid, caps)
        self.deviceID = self.param04
        print("open app")
        time.sleep(10)

    def testcall(self):
        """
        test body
        :return:
        """
        self.operatorNumber = "10086"
        self.driver.find_element_by_id("com.android.dialer:id/floating_action_button").click()
        time.sleep(10)
        Screenshot(self.driver, self.deviceID, "testcall001")

        element="com.android.dialer:id/deleteButton"
        bflag = ISextisting(self.driver, element,self.deviceID,"testcall002").IdTag()
        self.assertTrue(bflag)

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
        Screenshot(self.driver, self.deviceID, "testcall003")

        self.driver.find_element_by_id("com.android.dialer:id/dialpad_floating_action_button").click()
        time.sleep(10)
        Screenshot(self.driver, self.deviceID, "testcall004")

        element="com.android.dialer:id/contactgrid_bottom_timer"
        bflag = ISextisting(self.driver, element, self.deviceID, "testcall005").IdTag()
        self.assertTrue(bflag)
        self.driver.find_element_by_id("com.android.dialer:id/incall_end_call").click()
        time.sleep(10)
        Screenshot(self.driver, self.deviceID, "testcall006")

    def tearDown(self):
        """

        :return:
        """
        self.logger.info("测试结束，输出log完结\n\n")
        self.driver.quit()
        print("close app!")
        time.sleep(5)