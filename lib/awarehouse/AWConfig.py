# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-24T22:41:25+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: AWConfig.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-15T22:45:31+01:00


import os

import yaml


class AWConfig:

    conf = {}

    def __init__(self, configPath=None):
        # Try getting the environment variable if configPath not given
        configPath = configPath if configPath else os.environ.get("AWAREHOUSE_CONF", None)
        # Try loading the configuration file
        if configPath and not configPath == "":
            self.loadFileYaml(configPath)
        else:
            # Try loading the current working directory configuration file
            cwdConfig = os.path.join(os.getcwd(), "warehouse.yml")
            try:
                self.loadFileYaml(cwdConfig)
            except:
                # Try loading the system default configuration file
                systemDefault = "/etc/AWarehouse/warehouse.yml"
                try:
                    self.loadFileYaml(systemDefault)
                except:
                    # Try loading the module default configuration file
                    moduleDefault = os.path.join(os.path.dirname(__file__), "warehouse.yml")
                    try:
                        self.loadFileYaml(moduleDefault)
                    except:
                        raise Exception("Unable to find awarehouse configuration file")

    def __getitem__(self, key):
        return self.conf[key]

    def has_key(self, key):
        return (key in self.conf)

    def loadFileYaml(self, filePath):
        with open(filePath, "r") as fd:
            self.conf = yaml.load(fd.read())
        return self
