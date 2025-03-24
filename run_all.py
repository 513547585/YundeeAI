import unittest, os, time, sys
from common import HTMLTestRunner_cn, mail,HTMLTESTRunner_b
from Unit_tools import tools


class run_all():

    def run_case(self):
        tools.delete_file()
        curpath = os.path.dirname(os.path.realpath(__file__))
        casepath = os.path.join(curpath, "case")
        reportpath = os.path.join(curpath, "report")
        # 匹配用例
        rule = 'test*.py'
        # 获取用例
        discover = unittest.defaultTestLoader.discover(start_dir=casepath, pattern=rule)
        # 给文件取名字按照时间戳展示
        # dt=datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
        # filename='report'+dt+'.html'
        # filename='report'+'.html'
        now = time.strftime('%Y_%m_%d %H_%M_%S')
        # wb代表存在打开重置重新编写，没有创建编写
        fp = open(reportpath + "\\" + "report.html", 'wb')
        # stream写报告title报告名称description描述
        # 有图片
        runner = HTMLTESTRunner_b.HTMLTestRunner(stream=fp, title="369智慧供应链系统UI自动化测试报告", description="测试用例执行情况如下：")
        # 无图片 百分比
        # runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title="369智慧供应链系统UI自动化测试报告", description="测试用例执行情况如下：")
        # 执行找到的用例
        runner.run(discover)
        fp.close()


if __name__ == '__main__':
    run_all().run_case()
    mail.MailUtils().send_test_report()
    # print(sys.path)
