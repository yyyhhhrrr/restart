#!/usr/bin/env python
# coding:utf-8
# Author:Yang


import smtplib
from email.mime.text import MIMEText
from core.get_time import time_now

'''发送邮件工具'''


def SendEmail(fromAdd, toAdd, subject, text):
    _pwd = "lobhxvlvxnadbfeb"  # 授权码

    msg = MIMEText(text)
    msg["Subject"] = subject
    msg["From"] = fromAdd
    msg["To"] = toAdd
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 587)
        s.login(fromAdd, _pwd)
        s.sendmail(fromAdd, toAdd, msg.as_string())
        s.quit()
        print("%s : send email success!"%time_now())
    except smtplib.SMTPException:
        print('Falied!')



SendEmail("562605133@qq.com","562605133@qq.com","aa","aa")