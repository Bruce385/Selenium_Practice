from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib, os


class MailTest(object):
    def __init__(self, report_dir):
        self.report_dir = report_dir

    def send_mail(self):
        file_path = self.last_report_path()
        f = open(file_path, 'rb')
        mail_body = f.read()
        f.close()

        attach = MIMEText(mail_body, "base64", "utf-8")
        attach["Content-Type"] = "application/octet-stream"
        # 附件名称为中文时的写法
        attach.add_header("Content-Disposition", "attachment", filename=("utf-8", "", "最新测试报告.html"))

        msg = MIMEMultipart()
        msg["from"] = 'brucecyc@126.com'
        msg["to"] = '2297711680@qq.com'
        msg['Subject'] = Header('自动化测试报告', 'utf-8')
        msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
        msg.attach(attach)

        smtp = smtplib.SMTP()
        smtp.connect('smtp.126.com')
        smtp.login('brucecyc@126.com', 'LNCVQXIVQAKOGXOH')
        smtp.sendmail('brucecyc@126.com', '2297711680@qq.com', msg.as_string())
        smtp.quit()
        print('email has send out!')

    def last_report_path(self):
        lists = os.listdir(self.report_dir)
        lists.sort(key=lambda fn: os.path.getmtime(self.report_dir + '\\' + fn))
        last_report = os.path.join(self.report_dir, lists[-1])
        print(last_report)
        return last_report
