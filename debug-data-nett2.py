import os
import shutil
from subprocess import call
import time
import errno

from datetime import datetime

datotid = (time.strftime('%Y-%m-%d_%H-%M'))

print datotid

os.makedirs(datotid)

cmd = 'scp root@10.8.0.6:/root/Bachelor_v2017/debug-node2.txt /home/bachelor/Debug/nett2/bbg2nett2.txt'  #henter debug fil fra bbg2 nett2
call(cmd.split())

cmd = 'scp root@10.8.0.22:/root/Bachelor_v2017/debug-node2.txt /home/bachelor/Debug/nett2/bbg3nett2.txt' #henter debug fil fra bbg3 nett2
call(cmd.split())

sourcepath='/home/bachelor/Debug/nett2'
source = os.listdir(sourcepath)
destinationpath = os.path.join('/home/bachelor/Debug/nett2/', datotid)
for files in source:
    if files.endswith('.txt'):
        shutil.move(os.path.join(sourcepath,files), os.path.join(destinationpath,files))

