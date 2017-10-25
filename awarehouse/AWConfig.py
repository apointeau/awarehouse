# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-24T22:41:25+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: AWConfig.py
# @Last modified by:   kalif
# @Last modified time: 2017-10-25T01:09:59+02:00

import os, copy

import yaml

class AWConfig:

    conf = {}

    def __init__(self, configPath=None):
        # Try loading the module default configuration file
        moduleDefault = os.path.join(os.path.dirname(__file__), "warehouse.yml")
        try: self.loadFileYaml(moduleDefault)
        except: pass

        # Try loading the system default configuration file
        systemDefault = "/etc/AWarehouse/warehouse.yml"
        try: self.loadFileYaml(systemDefault)
        except: pass

        if configPath: # Load the given configuration file
            self.loadFileYaml(configPath)
        else: # Try loading the current working directory configuration file
            cwdConfig = os.path.join(os.getcwd(), "warehouse.yml")
            try: self.loadFileYaml(cwdConfig)
            except: pass


    def __getitem__(self, key): return self.conf[key]
    def has_key(self, key): return self.conf.has_key(key)

    def loadFileYaml(self, filePath, method='override'):
        with open(filePath, "r") as fd:
            data = yaml.load(fd.read())
        self._updateConf(data, method)
        return self


    def _updateConf(self, data, method='override'):
        if method == 'override':
            self.conf.update(data)
        elif method == 'fill':
            self.conf = data.update(conf)
        elif method == 'erase':
            self.conf = copy.deepcopy(data)
        else:
            raise Exception("Unknown configuration update method %s" % (method))
