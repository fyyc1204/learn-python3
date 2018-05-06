#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 分析电商日志访问情况
# awk 对access.txt 预处理
# cat localhost_access_log.2018-04-06.txt |awk -F':|/|'' ' '{print $1 "," $7":"$8":"$9}' |more >>11.txt


import numpy as np    
import pandas as pd 
import matplotlib.pyplot as plt
from pandas import Series, DataFrame 
print('Load data')

df1=pd.read_csv('D://project/learn-python3/MachineLearn/11.txt' ,header=None,decimal=',',names=["ip","time"] )

df1["time"]=pd.to_datetime(df1["time"])
df1 = df1.set_index('time')

print("time ...")
t = []
for ss in range(24):
    if ss<10:
        zz = str('0') + str(ss)
    else:
        zz = str(ss)        
    sdr = '2018-04-07 ' + zz
    t.append(sdr)
#print(t)
#print("******************")
h = []
for hh in t:
    for ss in range(60):
        if ss<10:
            mm = str('0') + str(ss)
        else:
            mm = str(ss)        
        sdr = hh + ":" + mm
        h.append(sdr)
        #print(len(h))

print(len(h))
#print(h[836])
print("##########")
ss = []
zz = []
for n in range(len(h)-1):
    count=df1[h[n]:h[n+1]].count()
    zz.append(count)
    
    ss.append(str(h[n]) + " " + str(zz[n])  + "\n")

fo = open("foo.txt", "w")
fo.write(str(ss))
fo.close
#print(zz)
print("plot ...")
#print(zz)
#print()
plt.plot(h[:1439],zz)
plt.show()
