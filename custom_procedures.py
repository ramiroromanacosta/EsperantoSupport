# -*- coding: utf-8 -*-

def newestFile(path):
    import os
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)
# end of procedure
