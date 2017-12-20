# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-08T22:55:11+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: FOLDER.py
# @Last modified by:   kalif
# @Last modified time: 2017-12-20T21:55:03+01:00

import os
import shutil

from .storageAbstract import storageAbstract, storageError


class FOLDER(storageAbstract):

    required_fields = [
        {"field": "path", "type": str},
    ]

    def __init__(self, path=None, **kwargs):
        super(FOLDER, self).__init__(**kwargs)

        if not path:
            raise storageError("missing required field 'path'")
        if not os.path.isdir(path):
            try:
                os.mkdir(path)
            except:
                raise storageError("'path' isn't a directory")
        self.rootPath = os.path.abspath(path)

        self.kwargs = kwargs
        self.connect()

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def __join(self, path):
        # FILTER
        if ".." in path:
            raise storageError("path contains '..', operation not permitted")
        # SIMPLIFY / TRANSFORM
        while "//" in path:
            path = path.replace("//", "/")
        if path.startswith("./"):
            path = path[2:]
        if path.startswith("/"):
            path = path[1:]
        # RESOLV
        if not path or path == "":
            return self.rootPath
        path = os.path.abspath(os.path.join(self.rootPath, path))
        if not path.startswith(self.rootPath):
            raise storageError("invalid path")
        return path

    # READ STORAGE CONTENT #

    def exists(self, path):
        return os.path.exists(self.__join(path))

    def listdir(self, path):
        print(self.__join(path))
        return os.listdir(self.__join(path))

    def isdir(self, path):
        return os.path.isdir(self.__join(path))

    # CREATE STORAGE CONTENT #

    def touch(self, path):
        open(self.__join(path), 'a').close()

    def makedirs(self, path):
        return os.makedirs(self.__join(path))

    # TRANSFER STORAGE CONTENT #

    def put(self, src, dst):
        return self.copy(src, dst)

    def get(self, src, dst):
        return self.copy(dst, src)

    # MANIPULATE STORAGE CONTENT #

    def move(self, src, dst):
        return shutil.move(self.__join(src), self.__join(dst))

    def copy(self, src, dst):
        return shutil.copy(self.__join(src), self.__join(dst))

    def rm(self, path):
        path = self.__join(path)
        try:
            os.remove(path)
        except Exception:
            os.rmdir(path)

    def rmtree(self, path):
        try:
            os.remove(self.__join(path))
        except Exception:
            shutil.rmtree(self.__join(path))
