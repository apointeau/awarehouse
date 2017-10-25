# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-25T02:13:08+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: storageFactory.py
# @Last modified by:   kalif
# @Last modified time: 2017-10-25T02:23:13+02:00

import importlib

class storageFactory:

    def create_storage(self, **kwargs):
        if not kwargs.has_key("type"):
            raise Exception("Unable to build storage without type")
        t = str(kwargs["type"])
        try:
            storageClass = getattr(importlib.import_module(".." + t, __name__), t)
        except:
            raise Exception("Unknown storage type '%s'" % t)
        return storageClass(**kwargs)
