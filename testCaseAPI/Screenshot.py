#  -*- coding:utf-8 -*-
from common import Log as Log
#截取屏幕存放在相应路径中
def Screenshot(driver,deviceID,testcase):
    path = Log.Log.get_screen_path(deviceID,testcase)
    driver.get_screenshot_as_file(path)