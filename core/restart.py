#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import time
import os
from core.api_test import test_restart_success
from core.sendmail import SendEmail
from core.get_time import time_now
import sys

class Restart(object):

    def __init__(self,ip):
        self.ip = ip


    def stop_tomcat(self,tomcat_home,*args):
        tomcat=tomcat_home.split('/')[2]
        if self.ip == "39.104.13.49":
            print('%s : ready to stop tomcat(%s:%s)...' % (time_now(), self.ip,tomcat_home))
            tomcat_pid = str(
                int(os.popen(
                    'ps aux|grep ' + tomcat + '|grep -v grep|grep java|grep -v restart|awk \'{print $2}\'').read()))
            print('%s : command:%s' % (time_now(),'ps aux|grep ' + tomcat + '|grep -v grep|grep java|grep -v restart|awk \'{print $2}\''))
            print('%s : result:%s'%(time_now(),tomcat_pid))
            os.popen('kill -9 ' + tomcat_pid)
            print('%s : command:%s'%(time_now(),'kill -9 ' + tomcat_pid))
            print('%s : stop tomcat(%s:%s) success...' % (time_now(),self.ip,tomcat_home))



        elif self.ip == "39.104.137.176":
            print('%s : ready to stop tomcat(%s:%s)...' % (time_now(), self.ip, tomcat_home))
            client=args[0]
            ssh=args[1]
            tomcat_pid = client.exec_command(
                'ps aux|grep ' + tomcat + '|grep -v grep|grep java|grep -v restart|awk \'{print $2}\'',ssh)
            client.exec_command('kill -9 ' + tomcat_pid,ssh)

            print('%s : stop tomcat(%s:%s) success...' % (time_now(),self.ip,tomcat_home))
        else:
            print('error ip')


    def start_tomcat(self,tomcat_home,port,*args):

        if self.ip == "39.104.13.49":
            print('%s : ready to start tomcat(%s:%s)...' % (time_now(), self.ip, tomcat_home))
            print('%s : command:%s'%(time_now(),'sh ' + tomcat_home + '/bin/startup.sh'))
            res=os.popen('sh ' + tomcat_home + '/bin/startup.sh').read()
            print('%s : result:%s' % (time_now(),res))
            test_restart_success(self.ip,port,tomcat_home)


        elif self.ip == "39.104.137.176":
            print('%s : ready to start tomcat(%s:%s)...' % (time_now(), self.ip, tomcat_home))
            client=args[0]
            ssh=args[1]
            client.exec_command('sh '+tomcat_home+'/bin/startup.sh',ssh)
            test_restart_success(self.ip,port,tomcat_home)

        else:
            print('error ip')