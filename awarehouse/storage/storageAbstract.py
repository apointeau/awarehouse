# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-25T02:13:21+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: storageAbstract.py
# @Last modified by:   kalif
# @Last modified time: 2017-10-31T00:33:17+01:00

import abc

class storageError(Excpetion):
    pass

class storageAbstract:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def exists(self, path): raise NotImplementedError()

    @abc.abstractmethod
    def mkdir(self, path): raise NotImplementedError()

    @abc.abstractmethod
    def touch(self, path): raise NotImplementedError()

    @abc.abstractmethod
    def listdir(self, path): raise NotImplementedError()

    @abc.abstractmethod
    def rmtree(self, path): raise NotImplementedError()

    @abc.abstractmethod
    def move(self, path): raise NotImplementedError()

    @abc.abstractmethod
    def copy(self, path): raise NotImplementedError()
