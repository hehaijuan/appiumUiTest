#  -*- coding:utf-8 -*-
import os
import unittest
from common.Log import MyLog as Log
import readConfig as readConfig
import HTMLTestRunner
from common.configEmail import MyEmail
from common import common
from ParametrizedTestCase import ParametrizedTestCase
import threading
import testCase
import time


localReadConfig = readConfig.ReadConfig()

#获取测试用例集，并传参给测试脚本
class AllTest:
    def __init__(self,devicePlatN,devicePlatV,deviceName,deviceID,devicePort):
        global log, logger
        global on_off

        self.devicePlatN = devicePlatN
        self.devicePlatV = devicePlatV
        self.deviceName = deviceName
        self.deviceID = deviceID
        self.devicePort = devicePort
        #实例化LOG,
        log = Log.get_log()
        logger = log.get_logger()

        #每个测试终端生成测试报告的文件地址和文件名
        self.resultPath = log.get_report_path(self.deviceID)

        #获取配置文件中是否通过邮件发送报告的开关值on_off
        on_off = localReadConfig.get_email("on_off")
        #实例化发送邮件
        self.email = MyEmail.get_email()

        #读取需要执行的测试用例的文件
        self.caseListFile = os.path.join(readConfig.proDir, "caselist.txt")
        self.caseFile = os.path.join(readConfig.proDir, "testCase")
        self.caseList = []

    #设置要执行的测试用例
    def set_case_list(self):
        """
        set case list
        :return:
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()
    #设置测试用例集
    def set_case_suite(self):
        """
        set case suite
        :return:
        """
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:
            case_name = case.split("/")[-1]
            suite_module.append(case_name)
        print(suite_module)  #选中的所有测试用例
        if len(suite_module) > 0:
            count = len(suite_module)
            testcase_klass = []
            for i in range(count):
                testklass = "testCase"+"."+str(suite_module[i]) + "." + str(suite_module[i])
                testcase_klass.append(testklass)
            for self.testcaseclass in testcase_klass:
                test_suite.addTest(ParametrizedTestCase.parametrize(eval(self.testcaseclass), param01=str(self.devicePlatN),param02=str(self.devicePlatV),param03=str(self.deviceName),param04=str(self.deviceID),param05=int(self.devicePort)))
        else:
            return None
        return test_suite

#每个测试终端线程中执行的函数，传入的参数为APPIUM 中需要的参数
def run(devicePlatN,devicePlatV,deviceName,deviceID,devicePort):
    """
    run test
    :return:
    """
    #实例化所有的测试用例集
    obj = AllTest(devicePlatN,devicePlatV,deviceName,deviceID,devicePort)
    try:
        #组建测试用例集
        suit = obj.set_case_suite()
        if suit is not None:
            logger.info("********TEST START********")
            #执行测试用例集，并生成HTML的测试报告
            fp = open(obj.resultPath, 'wb')
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
            runner.run(suit)
            fp.close()
        else:
            logger.info("Have no case to test.")
    except Exception as ex:
        logger.error(str(ex))
    finally:
        logger.info("*********TEST END*********")
        # 发送测试报告
        if on_off == 'on':    #on_off 是否发送测试报告的开关
            self.email.send_email()
        elif on_off == 'off':
            logger.info("Doesn't send report email to developer.")
        else:
            logger.info("Unknow state.")


if __name__ == '__main__':
    #获取device.xlsx的行数，第一行为表头，第二行之后为设备数
    device = common.get_xls("device.xlsx", "android_device")
    #获取device 数量
    count = len(device) - 1
    print("test device's is %d"%count)
    #为每个测试终端创建一个线程，可以同时执行同一套脚本测试
    for i in range(count):
        t = threading.Thread(target=run,args=(device[i+1][0],device[i+1][1],device[i+1][2],device[i+1][3],device[i+1][4]))
        t.start()


