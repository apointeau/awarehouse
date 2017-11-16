# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-25T02:13:21+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: storageAbstract.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-16T00:10:06+01:00

import abc

class storageError(Exception):
    pass

class storageAbstract:
    __metaclass__ = abc.ABCMeta

    # CLASS PROPERTIES #

    required_fields = None

    # INSTANCE PROPERTIES #

    connected = False

    def __init__(self, name=None, role=None, **kwargs):
        if not name:
            raise storageError("missing required field 'name'")
        self.name = name
        if not role:
            raise storageError("missing required field 'role'")
        self.role = role.capitalize()

    # STORAGE MANAGEMENT #

    @abc.abstractmethod
    def connect(self): raise NotImplementedError()

    @abc.abstractmethod
    def disconnect(self): raise NotImplementedError()

    # READ STORAGE CONTENT #

    @abc.abstractmethod
    def exists(self, path): raise NotImplementedError()

    @abc.abstractmethod
    def listdir(self, path): raise NotImplementedError()

    # CREATE STORAGE CONTENT #

    @abc.abstractmethod
    def touch(self, path): raise NotImplementedError()

    @abc.abstractmethod
    def makedirs(self, path): raise NotImplementedError()

    # TRANSFER STORAGE CONTENT #

    @abc.abstractmethod
    def put(self, src, dst): raise NotImplementedError()

    @abc.abstractmethod
    def get(self, src, dst): raise NotImplementedError()

    # MANIPULATE STORAGE CONTENT #

    @abc.abstractmethod
    def move(self, src, dst): raise NotImplementedError()

    @abc.abstractmethod
    def copy(self, src, dst): raise NotImplementedError()

    @abc.abstractmethod
    def rmtree(self, path): raise NotImplementedError()
