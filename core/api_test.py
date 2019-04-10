#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import requests
from core.get_time import time_now
from core.sendmail import SendEmail
import sys
import time
'''接口检测工具'''


def interface_test(ip,port):
    url = "http://%s:%s/card/cardValidate" % (ip, port)
    payload = "{\"cardNum\":\"2787504611\",\"companyId\":\"181\"}"
    headers = {
        'Content-Type': "application/json",
        'token': "2951314e0796466EE5c36ae737566128",
        'cache-control': "no-cache"
    }
    try:
       response = requests.request("POST", url, data=payload, headers=headers).text
    except Exception as e:
       return False
    response=eval(response)
    if int(response['code']) == 200:
        return True
    else:
        return False





def test_restart_success(ip,port,tomcat_home):
    for i in range(100):
        result = interface_test(ip, port)
        if result == True:
            print("%s : tomcat(%s:%s) is running success..." % (time_now(),ip, tomcat_home))
            break
        else:
            i += 1
            if i == 100:
                print("%s : warning:start tomcat(%s:%s) overtime,the thread has closed...see email later.." % (
                time_now(),ip, tomcat_home))
                from_ = "562605133@qq.com"  # 你的邮箱   发件地址
                to_ = '562605133@qq.com'  # 收件地址
                subject = '重启服务器'  # 邮件标题
                text = time_now() + ':\n重启ip:%s:%s失败，路径:%s 已停止后面的重启' % (ip, port,tomcat_home)  # 邮件内容
                SendEmail(from_, to_, subject, text)
                sys.exit()
            else:
                print("%s : tomcat(%s:%s) test time:%s" % (time_now(),ip,tomcat_home, i))
                time.sleep(10)

