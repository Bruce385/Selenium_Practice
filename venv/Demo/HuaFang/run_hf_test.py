from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib, unittest, time, os


# ========查找最近的测试报告文件============
def new_report(report_dir):
    lists = os.listdir(report_dir)
    lists.sort(key=lambda fn: os.path.getmtime(report_dir + '\\' + fn))
    return os.path.join(report_dir, lists[-1])


# ===============发送邮件==================
def send_mail(file_new):
    att = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="auto-test-report.html"'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = '华方自动化测试登录'
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login('2297711680@qq.com', '')
    smtp.sendmail('2297711680@qq.com', '2297711680@qq.com', msgRoot.as_string())
    smtp.quit()


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './report/' + now + ' result.html'
    discover = unittest.defaultTestLoader.discover('./test_case', pattern='*_sta.py')
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title='华方自动化测试报告', description='系统:win10,浏览器:Chrome')
        runner.run(discover)
    fp.close()
    # print(new_report('./report/'))
    # filepath = new_report('./report/')
    # send_mail(filepath)
