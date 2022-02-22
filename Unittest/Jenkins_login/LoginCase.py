"""
登录的用例
"""


import unittest
from ddt import ddt,data

from Unittest.Jenkins_login.ExcelUtil import ExcelUtil
from Unittest.Jenkins_login.HttpRequestUtil import HttpRequestUtil

@ddt # 装饰测试类
class LoginCase(unittest.TestCase):

    # def __init__(self,methonName,url,data,expect,expectCookie):
    #     super(LoginCase,self).__init__(methonName)
    #     self.url = url
    #     self.data = data
    #     self.expect = expect
    #     self.expectCookie = expectCookie

    test_data = ExcelUtil("test_data.xlsx","Sheet1").getExcelData()

    # 正常登陆
    @data(*test_data) # 装饰测试方法，拿到几条数据就执行几次用例
    def test_login(self,item):
        req = HttpRequestUtil(item["url"], eval(item["data"]))
        response = req.post_request()
        try:
            resCookie = response.headers.__contains__("Set-Cookie")
            self.assertEqual(item["expect"],response.status_code)  # 注意这里本来就是数字类型，不用加eval
            if eval(item["expectCookie"]):
                self.assertTrue(resCookie)
            else:
                self.assertFalse(resCookie)
        except AssertionError as e:
            print("test_login执行不通过".format(e))
            raise e

    # # 不输入用户名
    # def test_login_no_username(self):
    #     data = {"j_username": "", "j_password": "123456"}
    #     req = HtppRequestUtil(self.url,data)
    #     response = req.post_request()
    #     exitCookie = response.headers.__contains__("Set-Cookie")
    #     try:
    #         self.assertEqual(401,response.status_code)
    #         self.assertFalse(exitCookie)
    #     except AssertionError as e:
    #         print("test_login_no_username执行不通过".format(e))
    #         raise e
    #
    # # 不输入密码
    # def test_login_no_pwd(self):
    #     data = {"j_username": "liuyanghe", "j_password": ""}
    #     req = HtppRequestUtil(self.url,data)
    #     response = req.post_request()
    #     exitCookie = response.headers.__contains__("Set-Cookie")
    #     try:
    #         self.assertEqual(401,response.status_code)
    #         self.assertFalse(exitCookie)
    #     except AssertionError as e:
    #         print("test_login_no_pwd执行不通过".format(e))
    #         raise e
    #
    # # 输入错误的密码
    # def test_login_incorrect_pwd(self):
    #     data = {"j_username": "liuyanghe", "j_password": "123321"}
    #     req = HtppRequestUtil(self.url,data)
    #     response = req.post_request()
    #     exitCookie = response.headers.__contains__("Set-Cookie")
    #     try:
    #         self.assertEqual(401,response.status_code)
    #         self.assertFalse(exitCookie)
    #     except AssertionError as e:
    #         print("test_login_incorrect_pwd执行不通过".format(e))
    #         raise e

if __name__ == '__main__':
    unittest.main()
