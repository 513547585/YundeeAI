# coding:utf-8
from selenium import webdriver
import unittest, ddt, time, os
from common.base import base
from common.ExceUtil import ExceUtil


@ddt.ddt
class test_start(unittest.TestCase, base):
    ''' 登录失败所有场景 '''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()

    def logins(self, user, passwore, result):
        time.sleep(5)

    # 拿到ddt.xlsx文件
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ddt.xlsx')
    readexcel = ExceUtil(filepath)
    # 获取第二行所有的行数值
    all_user = readexcel.dict_date()

    @ddt.data(*all_user)
    def test_login(self, data):
        #  传入 Excel里面的列的值【user】【passwored】【result】
        self.logins(data["user"], data["passwored"], data["result"])
        # 断言
        ll = self.driver.switch_to.alert.text
        login_false = base.is_value_in_element(self, "登录失败，请检查您的用户名或密码是否填写正确", ll)
        # print("登录失败场景---成功",aa)
        try:
            self.assertEqual(login_false, False, '成功')
            print("成功")
        except:
            print("失败")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
