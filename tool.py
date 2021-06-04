
# -*- coding: utf-8 -*-
import psutil,time

start = time.time()
char = "0" * 1073741824

with open('./hogehoge.csv',mode='a') as f:
    flag_time=start
    while(1):
        dsk = psutil.disk_usage('/')
        f.write(char)
        dif_time = int(time.time()-flag_time)
        if dif_time > 5:
            print("RC =",int(dsk.free / 1000000000),"GB",int(dsk.free / 1000000),"MB",int(dsk.free / 1000),"KB",int(dsk.free),"B")
            flag_time=time.time()
        if dsk.free < 1:
            break
