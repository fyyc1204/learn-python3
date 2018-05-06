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

df1= pd.DataFrame(pd.read_csv('D://project/learn-python3/MachineLearn/55.txt' ,header=None,decimal=',',names=["ip","time"] ))


table = pd.pivot_table(df1, index=["time"],values=["ip","time"],aggfunc=len)

#print(table)
#df1 = table.set_index('time')

# table["time"]=pd.to_datetime(table["time"])
# df1 = table.set_index('time')
# print(type(df1))
print(table.groupby(pd.TimeGrouper(freq='1Min')).sum())

#print(df1)

# df1["time"]=pd.to_datetime(df1["time"])
# df1 = df1.set_index('time')
# ss=df1.groupby(pd.TimeGrouper(freq='1Min')).count()
# print(ss)
