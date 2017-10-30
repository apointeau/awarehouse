# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-24T22:09:46+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: localFolder.py
# @Last modified by:   kalif
# @Last modified time: 2017-10-31T00:27:09+01:00

import os, shutil

from storageAbstract import storageAbstract, storageError

class localFolder(storageAbstract):

    def __init__(self, path=None, **kwargs):
        if not path:
            raise storageError("localFolder: field 'path' is missing")
        if not os.isdir(path):
            raise storageError("localFolder: 'path' isn't a directory")
        self.folderPath = os.path.realpath(path)


    def __join(self, path):
        if ".." in path:
            raise storageError("localFolder: path contains '..', operation not permitted")
        p = os.path.realpath(os.path.join(self.folderPath, path))
        if not p.startswith(self.folderPath):
            raise storageError("localFolder: invalid path")
        return p

    def exists(self, path):
        return os.path.exists(self.__join(path))

    def makedirs(self, path):
        return os.path.makedirs(self.__join(path))

    def touch(self, path):
        open(self.__join(path), 'a').close()

    def listdir(self, path):
        return os.listdir(self.__join(path))

    def rmtree(self, path):
        return shutil.rmtree(self.__join(path))

    def move(self, src, dst):
        return shutil.move(self.__join(src), self.__join(dst))

    def copy(self, src, dst):
        return shutil.copy(self.__join(src), self.__join(dst))
