import HTMLTestRunner
import unittest
from Unittest.Jenkins_login.LoginCase import LoginCase
from Unittest.Jenkins_login.ExcelUtil import ExcelUtil

suit = unittest.TestSuite()
# loader = unittest.TestLoader()
# suit.addTest(loader.loadTestsFromModule(LoginCase)) # 加入类里的所有用例

# 方法一：通过超继承一条一条用例加
# dataList = ExcelUtil("test_data.xlsx","Sheet1").getExcelData()
# for item in dataList:
#     suit.addTest(LoginCase("test_login",item["url"],eval(item["data"]),item["expect"],eval(item["expectCookie"]))) # 出现过bug:这里的data从Excel取出来是str类型，要转换成字典类型

# 方法二：通过DDT加用例
loader = unittest.TestLoader()
suit.addTest(loader.loadTestsFromTestCase(LoginCase))


with open("jenkins_login_report.html","wb") as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,title="jenkins登录接口报告",description="今天好开心",tester="lyh")
    runner.run(suit)

