# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-24T22:09:46+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: localFolder.py
# @Last modified by:   kalif
# @Last modified time: 2017-10-25T02:26:51+02:00

from storageAbstract import storageAbstract

class localFolder(storageAbstract):

    def __init__(self, **kwargs):
        pass

    def exists(self, path):
        print("hello")
