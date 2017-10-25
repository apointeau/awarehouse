# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-24T22:09:01+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: AWContext.py
# @Last modified by:   kalif
# @Last modified time: 2017-10-25T02:25:41+02:00

from AWConfig import AWConfig
from storage import storageFactory

class AWContextError(Exception):
    pass

class AWContext:
    """
    This class store all the necessary values and settings to manipulate all
    the AWarehouse components.
    """

    storageList = []

    def __init__(self, conf=None):
        self.conf = conf if type(conf) == AWConfig else AWConfig(conf)
        self.__initializeStorage()


    def __initializeStorage(self):
        if not self.conf.has_key("storage"):
            raise AWContextError("Conf field 'storage' - missing")
        storageConf = self.conf["storage"]

        if not type(storageConf) in [dict, list]:
            raise AWContextError("Conf field 'storage' - invalid type")

        if type(storageConf) == dict:
            storageConf = [storageConf]
        factory = storageFactory()
        for elem in storageConf:
            if not type(elem) == dict:
                raise AWContextError("Conf field 'storage' - invalid sub-component type")
            self.storageList.append(factory.create_storage(**elem))
