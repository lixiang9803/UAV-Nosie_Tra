#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 13:45:40 2021

@author: lixiang
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import string
from fuzzy_extractor import FuzzyExtractor

with open(r'/Users/lixiang/Desktop/px4_log/star.txt') as txt:
       content = txt.readlines()
       txt.close()
data=list()
for i in content:
    data.append(i.split(','))
list_x = list()
list_y = list()
list_z = list()
for i in range(230):
    list_x.append(data[i+400][2])
    list_y.append(data[i+400][3])
    list_z.append(data[i+400][4])
plt.rcParams['font.sans-serif'] = ['Songti SC']
x = np.array(list_x)
x1 = np.delete(x,0,0)
x2 = x1.astype('float64')
y = np.array(list_y)
y1 = np.delete(y,0,0)
y2 = y1.astype('float64')
z = np.array(list_z)
z1 = np.delete(z,0,0)
z2 = z1.astype('float64')




fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.plot(x2, y2, z2, label='gps_trajectory')
ax.legend()
plt.savefig("star.png")
plt.show()


def get_speed(data):
    ans = 0
    for k in range(np.size(data)-3):
        ans = ans+(data[k+1]-data[k])
    return ans/(np.size(data)-3)

def get_noise(data,pre_err):
    k = np.size(data)
    noise_date = list()
    for i in range(k):
        j = data[i]+pre_err*get_speed(data)*10*(random.random()-0.5)
        noise_date.append(j)
    noise_date = np.array(noise_date)
    noise_date = noise_date.astype('float64')
    return noise_date

def get_fig():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(get_noise(x2,1),get_noise(y2,1), get_noise(z2,1), label='gps_trajectory with 0.01 err',color='blue')
    ax.legend()
    plt.show()
    
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(get_noise(x2,2),get_noise(y2,2), get_noise(z2,2), label='gps_trajectory with 0.02 err',color='red')
    ax.legend()
    plt.show()
    
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(get_noise(x2,5),get_noise(y2,5), get_noise(z2,5), label='gps_trajectory with 0.05 err',color='red')
    ax.legend()
    plt.show()

def flg_fig(err):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(get_noise(x2,err),get_noise(y2,err), get_noise(z2,err), label='gps_trajectory with '+str(err)+' err',color='red')
    ax.legend()
    plt.show()

def array_to_ascii_string(arr):
    # 将3维数组展开成1维数组
    arr_flat = arr.flatten()
    # 转换为字符串
    str1 = ''
    for i in arr_flat:
        if(int(i)<10):
            str1 = str1+str(int(i))
        if(int(i)>=10):
            str1 = str1+"9"
    return str1
	
# 创建一个2行3列的6个子图的画布
fig, axes = plt.subplots(2, 3, figsize=(12, 8), subplot_kw={'projection': '3d'})


# 给每个子图设置标题
axes[0, 0].set_title('标准轨迹',fontsize=22)
axes[0, 1].set_title('1%噪音轨迹',fontsize=22)
axes[0, 2].set_title('2%噪音轨迹',fontsize=22)
axes[1, 0].set_title('5%噪音轨迹',fontsize=22)
axes[1, 1].set_title('8%噪音轨迹',fontsize=22)
axes[1, 2].set_title('10%噪音轨迹',fontsize=22)

# 为每个子图生成随机数据并绘制
colors = ['g', 'g', 'g', 'g', 'r', 'r']
t = 0

for ax in axes.flatten():
    ax.plot(get_noise(x2,t),get_noise(y2,t), get_noise(z2,t), color=colors[t])
    t = t+1
# 调整子图之间的间距
fig.tight_layout()

# 显示图形
#plt.show()
plt.savefig("Nosie.pdf",dpi=1500) 


    
