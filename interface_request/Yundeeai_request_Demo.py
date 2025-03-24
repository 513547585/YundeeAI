# coding=utf8
import requests, sys
from logs import loginfo
from Unit_tools import day_type
from Unit_tools.DDT_xlsx import excel_red

log = loginfo.log().logger


def login_AI_token():
    # 登录
    url = excel_red.get_data_from_excel('login.xlsx')[0]['ip'] + excel_red.get_data_from_excel('login.xlsx')[0]['interfase']
    data = excel_red.get_data_from_excel('login.xlsx')[0]['data']
    headers = excel_red.get_data_from_excel('login.xlsx')[0]['headers']
    try:
        request = requests.post(url=url, data=data, headers=headers)
        print(request.json())
        assert request.json()['code'] == 200
        log.info(str(day_type.Now_time_ms())+"登录成功")
        log.info("token值为  :"+str(request.json()['data']['access_token']))
        return request.json()['data']['access_token']
    except:
        log.info(str(day_type.Now_time_ms()) + "登录失败")
        sys.exit(1, "【登录失败],程序异常退出")


if __name__ == '__main__':
    login_AI_token()