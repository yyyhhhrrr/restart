#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from core import restart
from core import sshclient
from conf.settings import ip_list,tomcat_home
from core.sendmail import SendEmail
from core.get_time import time_now
import sys

def run():


    # '''重启本机 39.104.13.49 '''
    # r1 = restart.Restart(ip_list[0])
    #
    # '''39.104.13.49:7001'''
    # r1.stop_tomcat(tomcat_home[0])
    # r1.start_tomcat(tomcat_home[0],7001)
    #
    # '''39.104.13.49:7002'''
    # r1.stop_tomcat(tomcat_home[1])
    # r1.start_tomcat(tomcat_home[1], 7002)
    #
    # '''建立ssh'''

    client=sshclient.SSHClient(ip_list[1])
    ssh=client.SSH()


    '''重启远程主机 39.104.137.176'''
    r2 = restart.Restart(ip_list[1])

    '''39.104.137.176:7001'''
    r2.stop_tomcat(tomcat_home[0],client,ssh)
    r2.start_tomcat(tomcat_home[0],7001,client,ssh)

    '''39.104.137.176:7002'''
    r2.stop_tomcat(tomcat_home[1], client, ssh)
    r2.start_tomcat(tomcat_home[1], 7002, client, ssh)
    ssh.close()

    from_ = "562605133@qq.com"  # 你的邮箱   发件地址
    to_ = '562605133@qq.com'  # 收件地址
    subject = '重启服务器'  # 邮件标题
    text =  '重启所有快乐yoyo成功，日期:%s'%time_now()  # 邮件内容
    SendEmail(from_, to_, subject, text)
    sys.exit()


