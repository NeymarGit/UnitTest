"""
测试用例
"""


import json
import unittest
from FmApp.Utils.ExcelUtil import ExcelUtil
from FmApp.Utils.RequestUtil import RequestUtil
from ddt import ddt, data
from FmApp.Utils.Memory import Memory
from FmApp.Utils.Logger import Logger
log = Logger()

@ddt
class TestCase(unittest.TestCase):
    # 登录接口用例
    loginData = ExcelUtil(r"..\TestData\test_data.xlsx", "login").getExcelData()
    global loginList
    loginList = []

    @data(*loginData)
    def test_login(self, item):
        resultDict = {}
        sucessFlag = False
        url = item["request_url"]
        headers = {"deviceId": "CD9FD298-D8BD-4226-B78A-9073F6FC6D1G", "Content-Type": "application/json"}
        data_other = {"openChannelCd": "1", "newVersion": "true", "openId": "",
                      "distinctId": "CD9FD298-D8BD-4226-B78A-9073F6FC6D1G", "grantTypeCd": "1",
                      "jpushId": "101d855909e851a0721", "unionId": ""}
        login_data = {**eval(item["request_data"]), **data_other}  # 拼接字典
        response = RequestUtil(url, json.dumps(login_data), headers).requestPost()
        result = response.json()
        try:
            self.assertEqual(eval(item["expect_result"])["code"], result["code"])
            sucessFlag = True
            if eval(item["expect_result"])["code"] == "200":
                token = response.json()["data"]["token"]
                log.info(token)
                setattr(Memory, "token", token)  # 通过反射存储token
        except AssertionError as e:
            log.error("test_login执行不通过".format(e))
            raise e
        finally:
            resultDict["id"] = item["id"]
            resultDict["actual_result"] = result
            resultDict["is_success"] = sucessFlag
            global loginList
            loginList.append(resultDict)
            ExcelUtil(r"..\TestData\test_data.xlsx", "login", loginList).setExcelData()

    # 米粒兑换接口
    miliExchangeData = ExcelUtil(r"..\TestData\test_data.xlsx", "miliExchange").getExcelData()
    global miliExchangeList
    miliExchangeList = []

    @data(*miliExchangeData)
    def test_miliExchange(self, item):
        resultDict = {}
        sucessFlag = False
        url = item["request_url"]
        token = str(getattr(Memory, "token"))
        headers = {"os": "ios", "Content-Type": "application/json", "token": token}
        data = eval(item["request_data"])
        response = RequestUtil(url, json.dumps(data), headers).requestPost()
        result = response.json()
        try:
            self.assertEqual(eval(item["expect_result"])["code"], result["code"])
            sucessFlag = True
        except AssertionError as e:
            log.error("test_miliExchange执行不通过".format(e))
            raise e
        finally:
            resultDict["id"] = item["id"]
            resultDict["actual_result"] = result
            resultDict["is_success"] = sucessFlag
            global miliExchangeList
            miliExchangeList.append(resultDict)
            ExcelUtil(r"..\TestData\test_data.xlsx", "miliExchange", miliExchangeList).setExcelData()


if __name__ == '__main__':
    unittest.main
