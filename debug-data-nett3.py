import os
import shutil
from subprocess import call
import time
import errno

from datetime import datetime

datotid = (time.strftime('%Y-%m-%d_%H-%M'))

print datotid

os.makedirs(datotid)

cmd = 'scp root@10.8.0.6:/root/Bachelor_v2017/debug-node3.txt /home/bachelor/Debug/nett3/bbg2nett3.txt'  #henter debug fil fra bbg2 nett3
call(cmd.split())

cmd = 'scp root@10.8.0.22:/root/Bachelor_v2017/debug-node3.txt /home/bachelor/Debug/nett3/bbg3nett3.txt' #henter debug fil fra bbg3 nett3
call(cmd.split())

sourcepath='/home/bachelor/Debug/nett3'
source = os.listdir(sourcepath)
destinationpath = os.path.join('/home/bachelor/Debug/nett3', datotid)
for files in source:
    if files.endswith('.txt'):
        shutil.move(os.path.join(sourcepath,files), os.path.join(destinationpath,files))

