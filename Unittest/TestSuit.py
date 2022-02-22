"""存储用例，执行用例"""

import unittest
import HTMLTestRunner
from Unittest import TestCase
from Unittest.TestCase import TestCaseAddition

# 存储用例的容器
suit = unittest.TestSuite()

# 方法一：一个用例一个用例得添加
# suit.addTest(TestCaseAddition("test_add_two_positive"))
# suit.addTest(TestCaseAddition("test_add_two_zero"))
# suit.addTest(TestCaseAddition("test_add_tow_negative"))

# 方法二：按模块添加所有的用例
loader = unittest.TestLoader()
suit.addTest(loader.loadTestsFromModule(TestCase))

# with open("report.txt", "w+", encoding="utf-8") as file:  # 上下文管理器，用完文件后自动关闭file
#     runner = unittest.TextTestRunner(stream=file, verbosity=2)  # verbosity有0,1,2三种选项
#     runner.run(suit)  # 执行用例

with open("test_report.html","wb") as file :
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title="lyh的测试报告",tester="刘阳何")
    runner.run(suit)