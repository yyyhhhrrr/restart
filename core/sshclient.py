#!/usr/bin/env python
# coding:utf-8
# Author:Yang


import paramiko
import sys
from core.get_time import time_now
from conf.settings import BASE_DIR

''' SSH连接类 '''


class SSHClient(object):

    def __init__(self,ip):
        self.ip = ip
        self.username="root"

    def SSH(self):
        print('%s : ssh %s@%s ...' % (time_now(), self.username, self.ip))
        try:
            private_key = paramiko.RSAKey.from_private_key_file(BASE_DIR+'\\core\\id_rsa_49')
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            ssh.connect(hostname=self.ip, port=22, username=self.username, pkey=private_key)
            print('%s : ssh %s@%s success!' % (time_now(), self.username, self.ip))
            return ssh
        except Exception as e:
            print('%s : ssh %s@%s failed :%s' % (time_now(), self.username, self.ip, e))
        sys.exit(0)

    def exec_command(self, cmd,ssh):
        print('%s : command:%s' % (time_now(), cmd))
        stdin, stdout, stderr = ssh.exec_command(cmd)
        res, err = stdout.read(), stderr.read()
        result = res if res else err
        print('%s : result:%s' % (time_now(), result.decode()))
        return result.decode()

# client=SSHClient("39.104.137.176")
# ssh=client.SSH()
# time.sleep(10)
# client.exec_command("ls",ssh)


