# coding=utf-8
import smtplib
import os ,time,datetime
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from report import report_path
from email.mime.application import MIMEApplication


class MailUtils():
    # XUXPWVYTAXPILWIG
    def send_test_report(self):
        # XUXPWVYTAXPILWIG 授权码
        # 表示一个类方法，不需要实例化，可以直接调用
        sender = 'w513547585@126.com'  # 发邮件人
        # 给多个人发邮件
        # receiver = '513547585@qq.com,492811634@qq.com'   #收件人
        receiver = '513547585@qq.com'   # 收件人
        auth_code = 'FZSZYLYLLMLMEMRC'  # 设置客户端授权码，不是密码，(发件人的)
        f = open(report_path.report_relative_path(), 'rb')
        mail_body = f.read()
        time = datetime.datetime.now()
        subject = '自动化测试报告'+str(time)  # 主题
        # HTML 形式的文件内容
        self.html = MIMEText(mail_body, _subtype='html', _charset='utf-8')  # 邮件消息体
        self.html['Subject'] = subject
        self.html['from'] = sender  # 从哪里来的消息
        self.html['to'] = receiver  # 发送到那里去
        msg = MIMEMultipart()
        msg['Subject'] = subject  # 邮件的标题
        msg.attach(self.html)  # 将html附加在msg里
        with open(report_path.report_relative_path(), 'rb') as f:
                mime = MIMEApplication(f.read())
                mime.add_header('Content-Disposition', 'attachment', filename='369智慧供应链自动化测试报告.html')
                msg.attach(mime)  # 新增一个附件

        # 连接邮箱服务器 登录 上smtp服务器
        smtp = smtplib.SMTP()
        smtp.connect('smtp.126.com')
        smtp.login(sender, auth_code)
        # 发送邮件sender发件人  receiver收件人，发送内容对象
        smtp.sendmail(sender, receiver.split(','), msg.as_string())
        print("邮件发送成功")
        smtp.quit()


if __name__ == "__main__":
        MailUtils().send_test_report()
        # print(MailUtils().get_NewReport())
        # f = open(report_relative_path.report_relative_path(), 'rb')
        # mail_body = f.read()
        # print(mail_body)