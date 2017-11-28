# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-24T22:09:01+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: AWContext.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-23T00:51:15+01:00

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
        self.conf.validate_storage()
        factory = storageFactory()

        for elem in self.conf["storage"]:
            if not type(elem) == dict:
                raise AWContextError("Configuration - invalid sub-component type in field 'storage'")
            self.storages.append(factory.create_storage(**elem))
        if len(self.masters) == 0:
            raise AWContextError("No storage with the role 'Master' found")

    # STORAGE MANAGMENT #
    @property
    def masters(self):
        return [s for s in self.storages if s.role == "Master"]

    @property
    def slaves(self):
        return [s for s in self.storages if s.role == "Slaves"]

    @property
    def _connected_master(self):
        return [s for s in self.masters if s.connected][0]



    # READ STORAGE CONTENT #

    def exists(self, path):
        return self._connected_master.exists(path)

    def listdir(self, path):
        return self._connected_master.listdir(path)

    def isdir(self, path):
        return self._connected_master.isdir(path)

    # CREATE STORAGE CONTENT #

    def touch(self, path):
        for s in self.storages:
            s.touch(path)

    def makedirs(self, path):
        for s in self.storages:
            s.makedirs(path)
