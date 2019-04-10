#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import time


def time_now():
    time_format="%Y-%m-%d %X"
    time_current=time.strftime(time_format)
    return time_current

