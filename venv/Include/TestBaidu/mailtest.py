from email.mime.text import MIMEText
from email.header import Header
import smtplib, os


class MailTest(object):
    def __init__(self, report_dir):
        self.report_dir = report_dir

    def send_mail(self):
        file_path = self.last_report_path()
        f = open(file_path, 'rb')
        mail_body = f.read()
        f.close()

        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg['Subject'] = Header('自动化测试报告', 'utf-8')

        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com')
        smtp.login('2297711680@qq.com', 'rrrhonwtbxapdide')
        smtp.sendmail('2297711680@qq.com', '2297711680@qq.com', msg.as_string())
        smtp.quit()
        print('email has send out!')

    def last_report_path(self):
        lists = os.listdir(self.report_dir)
        lists.sort(key=lambda fn: os.path.getmtime(self.report_dir + '\\' + fn))
        last_report = os.path.join(self.report_dir, lists[-1])
        print(last_report)
        return last_report
