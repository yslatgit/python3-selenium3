#coding:utf-8

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
import threading
from Base.BaseLog import MyLog
from Base.BaseElementEnum import Element as be


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


class Email:
    def __init__(self):
        global host, user, sender, passwd, port, receiver, title
        host = be.EmailConf["mail_host"]
        user = be.EmailConf["mail_user"]
        sender = be.EmailConf["mail_sender"]
        passwd = be.EmailConf["mail_pass"]
        port = be.EmailConf["mail_port"]
        receiver = be.EmailConf["mail_receiver"]
        title = be.EmailConf["mail_subject"]

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = "接口测试报告"+" "+date
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        #MIMEMultipart 下面有三种子类型
        #1.mixed --- 可以包含附件  2.related --- 可以包含内嵌资源  3.alternative --- 纯文本与超文本共存
        self.msg = MIMEMultipart()

    def config_header(self):
        self.msg['from'] = title
        self.msg['to'] = ','.join(receiver)
        # print(self.msg['to'])
        self.msg['subject'] = self.subject

    def config_content_xlsx(self):
        self.msg.attach(MIMEText(title,'plain','utf-8'))
        #测试发送邮件的数据
        # xlspart = MIMEApplication(open(PATH("../report.xls"),'rb').read())
        xlspart = MIMEApplication(open(PATH("../result/AllTestReport.html"),'rb').read())
        xlspart.add_header('Content-Disposition','attachment',filename='report.xls')
        self.msg.attach(xlspart)

    def config_content_image(self):
        imagepart = MIMEApplication(open(PATH("../report.image"),'rb').read())
        imagepart.add_header('Content-Disposition','attachment',filename='re.image')
        self.msg.attach(imagepart)

    def config_content_text(self):
        textpart = MIMEApplication(open(PATH("../report.text"),'rb').read())
        textpart.add_header('Content-Disposition','attachment',filename='re.text')
        self.msg.attach(textpart)

    def send_email(self):
        self.config_header()
        self.config_content_xlsx()
        try:
            smtp = smtplib.SMTP_SSL(host, port)
            # smtp.connect(host)
            smtp.login(user,passwd)
            smtp.sendmail(sender,receiver,self.msg.as_string())
            smtp.quit()
            self.logger.info("The test report has send to developer by email.")
        except Exception as ex:
            self.logger.error(str(ex))


class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():

        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email

if __name__ == '__main__':
    # email = MyEmail().get_email()
    #
    # email.send_email()
    Email().send_email()



