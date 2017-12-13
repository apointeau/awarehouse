# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-24T22:09:01+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: AWContext.py
# @Last modified by:   kalif
# @Last modified time: 2017-12-13T01:19:27+01:00

from .AWConfig import AWConfig
from .storage import storageFactory


class AWContextError(Exception):
    pass


class AWContext:
    """
    This class store all the necessary values and settings to manipulate all
    the AWarehouse components.
    """

    master = False
    slaves = []

    commands = {
        "everywhere": ["touch", "makedirs", "rm", "rmtree"],
        "master": ["exists", "listdir", "isdir"]
    }

    def __init__(self, conf=None):
        self.conf = conf if type(conf) == AWConfig else AWConfig(conf)
        self.__init_storages()

    def __init_storages(self):
        self.conf.validate_storage()
        factory = storageFactory()

        for elem in self.conf["storage"]:
            if not type(elem) == dict:
                raise AWContextError("Configuration - invalid sub-component type in field 'storage'")
            new = factory.create_storage(**elem)
            if new.role == "Master":
                self.master = new
            else:
                self.slaves.append(new)
        if not self.master:
            raise AWContextError("No storage with the role 'Master' found")

    # READ STORAGE CONTENT #

    def __getattr__(self, name):
        def method(*args, **kwargs):
            if name in self.commands["everywhere"]:
                getattr(self.master, name)(*args, **kwargs)
                for s in self.slaves:
                    getattr(s, name)(*args, **kwargs)
            elif name in self.commands["master"]:
                return getattr(self.master, name)(*args, **kwargs)
            else:
                raise AttributeError("AWContext instance has no attribute '{0}'".format(name))
        return method
