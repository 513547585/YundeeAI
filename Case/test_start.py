# coding:utf-8
import unittest, ddt, time, os,requests
from Unit_tools import day_type
from common.base import base
from common.ExceUtil import ExceUtil
from logs import loginfo
log = loginfo.log().logger
# 拿到ddt.xlsx文件
filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'case.xls')
readexcel = ExceUtil(filepath)
# 获取第二行所有的行数值
all_user = readexcel.dict_date()

@ddt.ddt
class test_start(unittest.TestCase, base):
    ''' 登录失败所有场景 '''
    def setUp(self):
        ...

    @ddt.data(*all_user)
    def test_login(self, data):
        try:
            print(data["ip"],data["interfase"],data["data"])
            request = requests.post(url=data["ip"]+data["interfase"], data=data["data"], headers={'Content-Type': 'application/json'})
            # print(request.json())
            assert request.json()['code'] == data["assert"]
            log.info(str(day_type.Now_time_ms()) + "登录成功")
            log.info("token值为  :" + str(request.json()['data']['access_token']))

            return request.json()['data']['access_token']
            print("测试通过")
        except:
            log.info(str(day_type.Now_time_ms()) + "用例执行失败："+str(request.json()))

    def tearDown(self):
        ...


if __name__ == '__main__':
    unittest.main()