"""
1,写用例，TestCase
2,执行用例，TestSuite 存储用例，TestLoader 加载用例 存到TestSuit
3,对比期望结果和实际结果，判断用例是否通过，断言Assert
4,测试报告 TextTestRunner
"""

import unittest
from Unittest.Math_Function import MathFuction


# 需要继承unittest框架的TestCase类
class TestCaseAddition(unittest.TestCase):

    # 每一条用例执行前先执行setUp
    def setUp(self):
        print("开始执行用例")

    # 每一条用例执行后执行的tearDown
    def tearDown(self):
        print("用例执行结束")


    def test_add_two_positive(self):
        result = MathFuction(1, 2).addition()
        print("1 + 2=", result)
        self.assertEqual(3,result)

    def test_add_two_zero(self):
        result = MathFuction(0, 0).addition()
        print("0 + 0=", result)
        self.assertEqual(0,result)

    def test_add_tow_negative(self):
        result = MathFuction(-1, -3).addition()
        print("-1 + -3=", result)
        try:
            self.assertEqual(4,result,"加法算错了")
        except AssertionError as e:
            print("错误原因为{}".format(e))
            raise e
# class TestCaseMultiple(unittest.TestCase):
#     def test_add_two_positive(self):
#         result = MathFuction(1, 2).multiple()
#         print("1 * 2=", result)
#
#     def test_add_two_zero(self):
#         result = MathFuction(0, 0).multiple()
#         print("0 * 0=", result)
#
#     def test_add_tow_negative(self):
#         result = MathFuction(-1, -3).multiple()
#         print("-1 * -3=", result)


if __name__ == '__main__':
    # 执行所有的用例,执行的顺序按照方法名的ASCII码表排序
    unittest.main()
