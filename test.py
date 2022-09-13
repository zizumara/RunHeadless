import time
from os import path, getcwd, remove

while True:
    time.sleep(1)
    workingDir = getcwd()
    exitFile = path.join(workingDir, 'exitflag')
    if path.exists(exitFile):
        remove(exitFile)
        break
