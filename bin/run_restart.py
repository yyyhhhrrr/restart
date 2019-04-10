#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import sys
import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.main import run


if __name__=='__main__':
    run()