# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-04T11:56:18+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: SFTP.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-16T23:12:11+01:00

import os

import pysftp

from storageAbstract import storageAbstract, storageError


class SFTP(storageAbstract):

    """
    This class provides SFTP connector folowing the `storageAbstract` design.
    """

    def __init__(self, path=None, host=None, **kwargs):
        super(SFTP, self).__init__(**kwargs)

        if not path:
            raise storageError("missing required field 'path'")
        self.rootPath = path

        if not host:
            raise storageError("missing required field 'host'")
        self.host = host

        self.params = kwargs
        try:
            self.connect()
        except:
            pass

    def connect(self):
        """
        Method that try to instanciate an SFTP connection. This function will
        raise an Exception if the connection couldn't start.
        """
        if self.connected:
            raise storageError("storage already connected")
        allowedArgs = [
            "port",
            "username",
            "password",
            "private_key",
            "private_key_pass"
        ]
        filteredArgs = {}
        for key in [k for k in self.params if k in allowedArgs]:
            filteredArgs[key] = self.params[key]
        self.conn = pysftp.Connection(self.host, **filteredArgs)
        self.conn.makedirs(self.rootPath)
        self.connected = True
        return self

    def disconnect(self):
        """
        Method that close the current SFTP connection and free the context.
        """
        if not self.connected:
            raise storageError("storage already disconnected")
        self.conn.close()
        self.conn = None
        self.connected = False
        return self

    def __join(self, path):
        if ".." in path:
            raise storageError("path contains '..', operation not permitted")
        if path[0] == "/":
            path = "." + path
        return os.path.join(self.rootPath, path)

    # READ STORAGE CONTENT #

    def exists(self, path):
        return self.conn.exists(self.__join(path))

    def listdir(self, path):
        return self.conn.listdir(self.__join(path))

    def isdir(self, path):
        return self.conn.isdir(self.__join(path))

    # CREATE STORAGE CONTENT #

    def touch(self, path):
        cmd = "touch {0}".format(self.__join(path))
        return self.conn.execute(cmd)

    def makedirs(self, path):
        return self.conn.makedirs(self.__join(path))

    # TRANSFER STORAGE CONTENT #

    def put(self, src, dst):
        return self.conn.put_r(self.__join(src), self.__join(dst))

    def get(self, src, dst):
        return self.conn.get_r(self.__join(src), self.__join(dst))

    # MANIPULATE STORAGE CONTENT #

    def move(self, src, dst):
        cmd = "mv {0} {1}".format(self.__join(src), self.__join(dst))
        return self.conn.execute(cmd)

    def copy(self, src, dst):
        cmd = "cp -r {0} {1}".format(self.__join(src), self.__join(dst))
        return self.conn.execute(cmd)

    def rmtree(self, path):
        cmd = "rm -rf {1}".format(self.__join(path))
        return self.conn.execute(cmd)
