#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
requests is a simple framework

Author by slyutae

"""



import requests,json,logging
from www.common.config import config
from www.common.other import Dict

def configlog():
    logconfig = logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',filename='myapp.log',filemode='w')
    consol = logging.StreamHandler()
    consol.setLevel(logging.INFO)
    formater = logging.Formatter('%(name)-12s:%(levelname) -8s %(message)s')
    return logconfig



class httpbase:

    def __init__(self):
        httpbase = config().configHttp
        self.name = httpbase['Testing_name']
        self.host = httpbase['Testing_host']
        self.port = httpbase['Testing_port']
        self.header = {"Content-Type":"application/json;charset=UTF-8"}
        self.body = {}


    def sendPost(self,data = None,url = None):
        urlpost = 'http://'+str(self.host)+':'+str(self.port)+str(url)
        params = json.dump(data,ensure_ascii=False)
        try:
            rsppost = requests.post(urlstring = urlpost,params = params)
            dict = json.load(rsppost.json())
            for key,values in dict:
                self.body[key] = values
            self.body =Dict(self.body.keys(),self.body.values())
            return self.body
        except Exception as e:
            print('%s' %e)
            return {}
        finally:
            print 'warning!'

    def sendget(self,url = None,params = None):
        urlget = 'http://'+str(self.host)+':'+str(self.port)+str(url)
        data = params
        try:
            rspget = requests.get(urlget,data)
            json = rspget.json()
            return json
        except Exception as d:
            print('%s' %d)
            return {}