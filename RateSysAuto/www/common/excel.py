#! usr/bin/env python
# -*- coding:utf-8 -*-

"""
Package the rate calculate api

Author by slyutae on 2017.09.09

"""


import xlwings as xw
from www.common.other import Dict
import os


class excel:

    def __init__(self):
        BASE_DIR = os.path.dirname(__file__)
        self.path = r'../../RateSysAuto/testdata/Rata'