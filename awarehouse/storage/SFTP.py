# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-04T11:56:18+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: SFTP.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-08T23:18:00+01:00

import os

import pysftp

from storageAbstract import storageAbstract, storageError

class SFTP(storageAbstract):


    def __init__(self, path=None, host=None, **kwargs):
        self.conn = self.__init_sftp_connection(host, **kwargs)
        if not path:
            raise storageError("field 'path' is missing")
        self.folderPath = path

    pysftpArgs = ["username", "private_key", "password", "port", "private_key_pass"]
    def __init_sftp_connection(self, host, **kwargs):
        connArgs = {}
        for key in [k for k in kwargs if k in self.pysftpArgs]:
            connArgs[key] = kwargs[key]
        return pysftp.Connection(host, **connArgs)

    def __join(self, path):
        if ".." in path:
            raise storageError("path contains '..', operation not permitted")
        if path[0] == "/":
            path = "." + path
        return os.path.join(self.folderPath, path)

    # READ STORAGE CONTENT #

    def exists(self, path):
        return self.conn.exists(self.__join(path))

    def listdir(self, path):
        return self.conn.listdir(self.__join(path))

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
