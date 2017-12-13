# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-24T22:41:25+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: AWConfig.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-17T00:54:39+01:00


import os

import yaml


class AWConfigError(Exception):
    pass


class AWConfig:

    conf = {}

    def __init__(self, path=None):
        # Try getting the environment variable if configPath not given
        self.path = path if path else os.environ.get("AWAREHOUSE_CONF", None)
        self.path = self.path if self.path is not "" else None
        # Try loading the configuration file
        if self.path:
            self.load(path)
        else:
            # Try loading the current working directory configuration file
            cwdConfig = os.path.join(os.getcwd(), "warehouse.yml")
            try:
                self.load(cwdConfig)
            except Exception:
                raise AWConfigError("Unable to find configuration file")

    def __getitem__(self, key):
        return self.conf.__getitem__(key)

    def __iter__(self):
        for key in self.conf:
            yield key

    def has_key(self, key):
        return (key in self.conf)

    # LOAD / SAVE #

    def load(self, filePath, fileType="yaml"):
        with open(filePath, "r") as fd:
            if fileType == "yaml":
                self.conf = yaml.load(fd.read())
            else:
                raise NotImplementedError()
        if not self.conf:
            self.conf = {}
        if type(self.conf) is not dict:
            raise AWConfigError("invalid configuration type, expect dict")
        return self

    def save(self, filePath=None, fileType="yaml", append=False):
        mode = "a" if append else "w"
        with open(filePath, mode) as fd:
            if fileType == "yaml":
                self.conf = fd.write(yaml.dump(self.conf))
            else:
                raise NotImplementedError()
        return self

    # VALIDATION #

    def _validate_key(self, field, dictionary, key, isList=False):

        if key not in dictionary:
            sc = "sub-component " if isList else ""
            raise AWConfigError(
                "field '{0}', missing {1}required key '{2}'"
                .format(field, sc, key)
            )

    def validate_storage(self):
        if "storage" not in self.conf:
            raise AWConfigError("missing required field 'storage'")
        if not type(self.conf["storage"]) in [dict, list]:
            raise AWConfigError("field 'storage', invalid type, expect list or dict")
        if type(self.conf["storage"]) == dict:
            self.conf["storage"] = [self.conf["storage"]]
        closeList = []
        countMaster = 0
        for s in self.conf["storage"]:
            if not type(s) == dict:
                raise AWConfigError("field 'storage', invalid sub-component type, expect dict")

            for k in ["name", "type", "role"]:
                self._validate_key("storage", s, k, isList=True)

            if s["name"] in closeList:
                raise AWConfigError("field 'storage', duplicate entry name '{0}'".format(s["name"]))
            closeList.append(s["name"])

            if s["role"].lower() == "master":
                countMaster += 1
        if countMaster == 0:
            raise AWConfigError("field 'storage', require 1 master role")
        elif countMaster > 1:
            raise AWConfigError("field 'storage', more than 1 master role")
