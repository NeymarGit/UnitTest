"""
加载测试用例
"""


import HTMLTestRunner
import unittest
from FmApp.TestExcute.TestCase import TestCase

suit = unittest.TestSuite()
loader = unittest.TestLoader()

suit.addTest(loader.loadTestsFromTestCase(TestCase))

with open(r"..\TestReport\login_report.html","wb") as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,title="回归测试",tester="lyh")
    runner.run(suit)