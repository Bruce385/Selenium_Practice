# -*- coding: utf-8 -*-
# @Author  : Bruce.Chen
# @Time    : 2020/5/6 15:04
# @File    : mailsend.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# 全部为python内置，不需要安装第三方模块
receivers = "2297711680@qq.com,123@qq.com"
sender = "brucecyc@126.com"
mail_auth = "LNCVQXIVQAKOGXOH"
mail_subject = "python发送邮件测试"  # 邮件的标题
mail_context = "这是邮件内容"

msg = MIMEMultipart()
msg["From"] = sender  # 发件人
msg["To"] = receivers  # 收件人
msg["Subject"] = mail_subject  # 邮件标题

# 邮件正文
msg.attach(MIMEText(mail_context, 'plain', 'utf-8'))

# 图片附件
# 不同的目录下要写全文件路径
with open('./data/test.jpg', 'rb') as picAtt:
    msgImg = MIMEImage(picAtt.read())
    msgImg.add_header('Content-Disposition', 'attachment', filename='你.jpg')
    # msgImg.add_header('Content-ID', '<0>')
    # msgImg.add_header('X-Attachment-Id', '0')
    msg.attach(msgImg)

# 构造附件
att = MIMEText(open('./data/test.txt', "rb").read(), "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
# 附件名称为中文时的写法
att.add_header("Content-Disposition", "attachment", filename=("gbk", "", "测试结果.txt"))
# 附件名称非中文时的写法
# att["Content-Disposition"] = 'attachment; filename="test.html")'
msg.attach(att)

smtp = smtplib.SMTP()
smtp.connect('smtp.126.com')
smtp.login(sender, mail_auth)
smtp.sendmail(sender, receivers.split(","), msg.as_string())
smtp.quit()
print('email has send out!')
