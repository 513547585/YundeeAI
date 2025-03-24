# coding:utf-8
import unittest, ddt
from common.base import base


@ddt.ddt
class test_start(unittest.TestCase,base):
    '''登录失败所有场景'''
    def setUp(self):
        pass

    # test运行用例
    # @ddt.file_data("data.json")
    # @ddt.unpack
    # def test_login(self, value):
    #     # print(value)
    #     a, b = value.split('||')
    #     # print(value)
    #     # print(a, b)
    #     print("a", a)
    #     print("b", b)

    @ddt.data([3, 2, 1], [5, 3, 2], [10, 4, 6])
    @ddt.unpack  # @ddt.unpack ,将【3，2，1】被分解开，按照用例的三个参数传递
    def test_minus(self, a, b, c):
        actual = int(a)-int(b)
        # print(a)
        print(b)
        # print(c)
        # print("aaaa", a, b, c)

    def tearDown(self):
        ...


if __name__ =='__main__':
    unittest.main()
