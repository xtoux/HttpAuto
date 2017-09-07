#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Package the rate calculate api

Author by slyutae on 2017.09.05

"""

from www.common.httpbase import *
from www.common.other import others



class rateSystem:

    def __init__(self):
        self.packHttpBase = httpbase()

    def calculate(self,type = None,sign_date = None,period_count = None,applay_amout = None,
                  principal_amount = None,product_number = None,merchant_number = None,borrow_days = None):
        url ='v5/rate/calculate'
        orgdata = {}
        orgdata['type'] = type
        orgdata['key'] = others.randomString()
        orgdata['from_system'] = 'KFQ'
        data = {}
        data['sign_date'] = sign_date
        data['period_count'] = period_count
        data['apply_amount'] = applay_amout
        data['principal_amount'] = principal_amount
        data['product_number'] = product_number
        data['merchant_number'] = merchant_number
        data['borrow_days'] = borrow_days
        rqsdata = {orgdata:data}
        self.packHttpBase.sendPost(rqsdata,url)
        return self.packHttpBase.body



