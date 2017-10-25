# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-25T02:13:21+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: storageAbstract.py
# @Last modified by:   kalif
# @Last modified time: 2017-10-25T02:22:38+02:00

import abc

class storageAbstract:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def exists(self, path):
        pass
