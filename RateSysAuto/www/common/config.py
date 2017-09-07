#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
waiting for a moment

Author by slyutae

"""

import ConfigParser


class config:

    def __init__(self):
        ini_file = '.../.../config/env_config'
        ConfigEnv = ConfigParser.ConfigParser()
        ConfigEnv.read(ini_file)
        self.envName = ConfigEnv['ENV']['switch']
        self.configHttp = self.getconfig(envName= self.envName,iniName='../../Http_config.ini')
        self.configserver = self.getconfig(envName = self.envName,iniName='../../config/server_config.ini')
        self.configDB = self.getconfig(envName = self.envName,iniName='../../config/db_config.ini')

    def getconfig(self,envName,iniName):
        config = ConfigParser.ConfigParser()
        config.read(iniName)
        keys = config.options(envName)
        values = []
        for i in range(0,len(keys)):
            values.append(config.get(keys[1],envName))
        return dict(keys,values)