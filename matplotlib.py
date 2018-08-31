# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 16:42:31 2018

@author: mai.mm.2
"""

import numpy as np
import matplotlib.pyplot as plt

#简单的绘图
x = np.linspace(0,2 * np.pi,50)  #生成50个元素分布在（0，2pi)
plt.plot(x,np.sin(x))#(x,y)
plt.show()

x = np.linspace(0,2 * np.pi,50)
plt.plot(x,np.sin(x),
         x,np.sin(2 * x))
plt.show()

#自定义曲线外表
x = np.linspace(0,2 * np.pi,50)
plt.plot(x,np.sin(x),'r-o',
         x,np.cos(x),'g--')
#蓝色 - 'b' 绿色 - 'g' 红色 - 'r' 青色 - 'c' 品红 - 'm' 黄色 - 'y' 黑色 - 'k'（'b'代表蓝色，所以这里用黑色的最后一个字母） 白色 - 'w' 线： 直线 - '-' 虚线 - '--' 点线 - ':' 点划线 - '-.' 常用点标记 点 - '.' 像素 - ',' 圆 - 'o' 方形 - 's' 三角形 - '^' 
#更多点标记样式点击:http://matplotlib.org/api/markers_api.html
plt.show()


#使用子图
x = np.linspace(0,2 * np.pi,50)
plt.subplot(2,1,1)  #行，列，活跃区
plt.plot(x,np.sin(x),'r')
plt.subplot(2,1,2)
plt.plot(x,np.cos(x),'g')
plt.show()


#简单的散点图
x = np.linspace(0,2 * np.pi,50)
y = np.sin(x)
plt.scatter(x,y)
plt.show()

#彩色映射散点图
x = np.random.rand(1000)
y = np.random.rand(1000)
size = np.random.rand(1000) * 50
color = np.random.rand(1000)
plt.scatter(x,y,size,color)
plt.colorbar()
plt.show()

#直方图
x = np.random.randn(1000)
plt.hist(x,50)
plt.show()

#添加标题和坐标，图例
x = np.linspace(0,2 * np.pi,50)
plt.plot(x,np.sin(x),'r-x',label='Sin(x)')
plt.plot(x,np.cos(x),'g-^',label='Cos(x)')
plt.legend() #展示图例
plt.xlabel('Rads') #给x轴添加标签
plt.ylabel('Amplitude') #给y轴添加标签
plt.title('Sin and Cos Waves')
plt.show()
