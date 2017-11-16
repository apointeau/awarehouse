# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-24T22:09:01+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: AWContext.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-16T01:22:11+01:00

from AWConfig import AWConfig
from storage import storageFactory


class AWContextError(Exception):
    pass


class AWContext:
    """
    This class store all the necessary values and settings to manipulate all
    the AWarehouse components.
    """

    storages = []

    def __init__(self, conf=None):
        self.conf = conf if type(conf) == AWConfig else AWConfig(conf)
        self.__init_storages()

    def __init_storages(self):
        if "storage" not in self.conf:
            raise AWContextError("Configuration - missing required field 'storage'")
        storageConf = self.conf["storage"]

        if not type(storageConf) in [dict, list]:
            raise AWContextError("Configuration - invalid field type 'storage'")

        if type(storageConf) == dict:
            storageConf = [storageConf]
        factory = storageFactory()
        for elem in storageConf:
            if not type(elem) == dict:
                raise AWContextError("Configuration - invalid sub-component type in field 'storage'")
            self.storages.append(factory.create_storage(**elem))
        if len(self.masters) == 0:
            raise AWContextError("No storage with the role 'Master' found")

    @property
    def _storage(self):
        return self.masters[0]

    @property
    def masters(self):
        return [s for s in self.storages if s.role == "Master"]

    @property
    def slaves(self):
        return [s for s in self.storages if s.role == "Slaves"]

    # READ STORAGE CONTENT #

    def listdir(self, path):
        return self._storage.listdir(path)

    # CREATE STORAGE CONTENT #

    def touch(self, path):
        for s in self.storages:
            s.touch(path)
