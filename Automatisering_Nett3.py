import os, sys
import shutil
from subprocess import call
import time
import fnmatch
import glob, re
import time

datotid = (time.strftime('%Y-%m-%d_%H-%M'))

#flytter .bin fil fra gjeldende til gammel -- legg til dato ved senere anledning
sourcepath='/home/bachelor/Upload/Nett3/Gjeldene/'
source = os.listdir(sourcepath)
destinationpath = '/home/bachelor/Upload/Nett3/Gammel/'
for files in source:
    if files.endswith('.bin'):
        shutil.move(os.path.join(sourcepath,files), os.path.join(destinationpath,files))
 
#Flytter ny .bin fil til gjeldene -- legg til dato ved senere anledning
sourcepath_2='/home/bachelor/Upload/Nett3/'
source_2 = os.listdir(sourcepath_2)
destinationpath_2 = '/home/bachelor/Upload/Nett3/Gjeldene/'
for files_2 in source_2:
    if files_2.endswith('.bin'):
        shutil.move(os.path.join(sourcepath_2,files_2), os.path.join(destinationpath_2,files_2))
		
#Forandrer navn til gjennkjenbart navn "Nett3" 
path = '/home/bachelor/Upload/Nett3/Gjeldene/'
for filename in os.listdir(path):
    filename_splitext = os.path.splitext(filename)
    if filename_splitext[1] in ['.bin']:
        os.rename(os.path.join(path, filename), 
                os.path.join(path, 'Nett3' + '.bin'))
print "\nSendert til aktive klienter...\n"



#CLIENT 2
cmd = 'ssh root@10.8.0.6 rm -rf /root/Bin_filer/Nett3/' #Fjerner gammel bin fil
call(cmd.split())
cmd = 'scp -r /home/bachelor/Upload/Nett3/Gjeldene/ root@10.8.0.6:/root/Bin_filer/Nett3/'  #Legger ny bin fil til nett 1 client2
call(cmd.split())

#CLIENT 3
cmd = 'ssh root@10.8.0.22 rm -rf /root/Bin_filer/Nett3/' #Fjerner gammel bin fil
call(cmd.split())
cmd = 'scp -r /home/bachelor/Upload/Nett3/Gjeldene/ root@10.8.0.22:/root/Bin_filer/Nett3/'  #Legger ny bin fil til nett 1 client2
call(cmd.split())




print "\nStarter flashing av nett3\n"
#CLIENT 2
print "\nStopper debugging av node 3 client 2..\n"
cmd = 'ssh -l root 10.8.0.6 pkill -9 -f debug-node3.py' #Stopper debug logging paa serialport
call(cmd.split())
print "\nStarter flashing av node 3 client 2\n"
cmd = 'ssh -l root 10.8.0.6 python /root/Bachelor_v2017/flash-node3.py -e -w -v /root/Bin_filer/Nett3/Nett3.bin' #Starter flashing
call(cmd.split())
print "\nStarter debugging av node 3 client 2\n"
cmd = 'ssh -l root 10.8.0.6 python /root/Bachelor_v2017/debug-node3.py > /dev/null 2>&1 & disown' #Starter debug logging paa serialport
call(cmd.split())
print "\nClient 2 nett 3 fullfort.\n"

#CLIENT 3
print "\nStopper debugging av node 3 client 3..\n"
cmd = 'ssh -l root 10.8.0.22 pkill -9 -f debug-node3.py' #Stopper debug logging paa serialport
call(cmd.split())
print "\nStarter flashing av node 3 client 3\n"
cmd = 'ssh -l root 10.8.0.22 python /root/Bachelor_v2017/flash-node3.py -e -w -v /root/Bin_filer/Nett3/Nett3.bin' #Starter flashing
call(cmd.split())
print "\nStarter debugging av node 3 client 3\n"
cmd = 'ssh -l root 10.8.0.22 python /root/Bachelor_v2017/debug-node3.py > /dev/null 2>&1 & disown' #Starter debug logging paa serialport
call(cmd.split())
print "\nClient 3 nett 3 fullfort.\n"

#For resterende klienter -> copy paste og endre ip-adresse

#Forandrer navn til dato den ble lagt over
path = '/home/bachelor/Upload/Nett2/Gjeldene/'
for filename in os.listdir(path):
    filename_splitext = os.path.splitext(filename)
    if filename_splitext[1] in ['.bin']:
        os.rename(os.path.join(path, filename), 
                os.path.join(path, datotid + '.bin'))