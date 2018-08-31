# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:37:49 2018

@author: mai.mm.2
"""

from scipy import io as spio
import numpy as np

#保存文件
a = np.ones((3,3))
spio.savemat('flie.mat',{'a' : a})

#导入文件
data = spio.loadmat('file.mat',struct_as_record= True)
data

#分析随机函数
import scipy.stats as stats

generated = stats.norm.rvs(size = 900)
generated

#得到均值和标准差
Mean,std = stats.norm.fit(generated)
print('Mean = ',Mean,',std = ',std)

#偏度
stats.skewtest(generated)  #pvalue的概率服从正态分布

#峰度
stats.kurtosistest(generated)  #陡峭程度

#正态性检验
stats.normaltest(generated)

#95%的数值
stats.scoreatpercentile(generated,95)
#数值所在的百分比
stats.percentileofscore(generated,1)

#分布直方图
import matplotlib.pyplot as plt
plt.hist(generated)
plt.show()
#均值检验
import numpy as np
price = get_price(['000001.XSHE','601398.XHSG'],start_date = '2016-01-01',end_date = '2017-01-01',fields='close')
price_001 = np.diff(np.log(np.array(price['000001.XSHE'])))
price_398 = np.diff(np.log(np.array(price['601398.XHSG'])))

#Kolmogorov-Smirnov检验
stats.ks_2samp(price_001,price_398)
#Jarque-Bera正态性检验
stats.jarque_bera(price_001 -price_398)[-1]

#信号处理

#检验股价的线性趋势
from datetime import date,datetme,time
from scipy import signal
import pandas as pd
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocater
price = get_price(['000001.XSHE','601398.XHSG'],start_date = '2016-01-01',end_date = '2017-01-01',fields='close')
y = signal.detrend(price)
#Series=串
trend = pd.Series(np.array(price) - y,index = price.index)
trend
trend.plot()


#傅里叶分析
from scipy import fftpack
#运用傅里叶变换，得到信号频谱

amps = np.abs(fftpack.fftshift(fftpack.rfft(y)))
#过滤噪音 某一分量的大小低于最强分贝的10%

amps[amps < 0.1*amps.max()] = 0
#过滤后的信号，去除趋势后的信号

plt.plot(price.index,y,label = 'datrended')
plt.plot(price.index,-fftpack.irfft(fftpack.fftshifft(amps)),label = 'fftrended')

#插值
#添加数据并噪音
x = np.linspace(-18,18,36)
noise = 0.1*np.random.random(len(x))
signal = np.sin(x) + noise

from scipy import interpolate
#创造一个线性插值函数
interpolate = interpolate.interp1d(x,signal)
x2 = np.linspace(-18,18,180)
y = interpolate.interpreted(x2)

#执行前一步，使3次插值
cubic = interpolate.interp1d(x,signal,king = 'cubic')
y2 = cubic(x2)

plt.plot(x,signal,'o',label = 'data')
plt.plot(x2,y,'-',label = 'lenear')
plt.plot(x2,y2,'-',lw = 2,label = 'cubic')

