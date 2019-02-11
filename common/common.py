#import requests
import readConfig as readConfig
import os
from xlrd import open_workbook
#from xml.etree import ElementTree as ElementTree
#from common import configHttp as configHttp
from common.Log import MyLog as Log
import json
import xml.dom.minidom
from xml.etree import ElementTree

localReadConfig = readConfig.ReadConfig()
proDir = readConfig.proDir
#localConfigHttp = configHttp.ConfigHttp()
log = Log.get_log()
logger = log.get_logger()

caseNo = 0


# def get_visitor_token():
#     """
#     create a token for visitor
#     :return:
#     """
#     host = localReadConfig.get_http("BASEURL")
#     response = requests.get(host+"/v2/User/Token/generate")
#     info = response.json()
#     token = info.get("info")
#     logger.debug("Create token:%s" % (token))
#     return token
#
#
# def set_visitor_token_to_config():
#     """
#     set token that created for visitor to config
#     :return:
#     """
#     token_v = get_visitor_token()
#     localReadConfig.set_headers("TOKEN_V", token_v)
#
#
# def get_value_from_return_json(json, name1, name2):
#     """
#     get value by key
#     :param json:
#     :param name1:
#     :param name2:
#     :return:
#     """
#     info = json['info']
#     group = info[name1]
#     value = group[name2]
#     return value
#
#
# def show_return_msg(response):
#     """
#     show msg detail
#     :param response:
#     :return:
#     """
#     url = response.url
#     msg = response.text
#     print("\n请求地址："+url)
#     # 可以显示中文
#     print("\n请求返回值："+'\n'+json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))
# # ****************************** read testCase excel ********************************
#

def get_xls(xls_name, sheet_name):
    """
    get interface data from xls file
    :return:
    """
    cls = []
    # get xls file's path
    xlsPath = os.path.join(proDir, "testFile", xls_name)
    # open xls file
    file = open_workbook(xlsPath)
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls

# ****************************** read Uiidconfig xml ********************************
def get_uiidconfig_xmlapk(programm,activity):
    """
    set sql xml
    :return:
    """
    uiidconfigPath = os.path.join(proDir,"testFile","Uiidconfig.xml")
    dom = xml.dom.minidom.parse(uiidconfigPath)
    root = dom.documentElement
    root = root.getElementsByTagName(programm)
    item = root[0]
    return item.getAttribute(activity)
def get_uiidconfig_xmlid(tag,name1,name2):
    uiidconfigPath = os.path.join(proDir, "testFile", "Uiidconfig.xml")
    tree = ElementTree.parse(uiidconfigPath)
    #tag = ".contact/activity"
    for u in tree.findall(tag):
        ob_name1 = u.get('name')
        #name1 = "联系人界面"
        if ob_name1 == name1:
            for c in u.getchildren():
                ob_name2 = c.get('name')
                #name2 = "新建联系人图标"
                if ob_name2 == name2:
                    id = c.get("id")
    return id

if __name__ == "__main__":
    print(get_xls("login"))
    #set_visitor_token_to_config()
