# _*_ coding: utf-8 _*_
from __future__ import division 
import matplotlib.pyplot as plt 
import numpy as np 


def create_left_right_line(leftArr,rightArr):
    for j in range(len(leftArr)):
        dataLeft = leftArr[j]
        dataRight = rightArr[j]
        plt.plot([dataLeft['x'],dataRight['x']],[dataLeft['y'],dataRight['y']])

def create_bootom_right_line(bootomArr,rightArr):
    bootomArr.reverse()
    for j in range(len(bootomArr)):
        dataLeft = bootomArr[j]
        dataRight = rightArr[j]
        plt.plot([dataLeft['x'],dataRight['x']],[dataLeft['y'],dataRight['y']])

def create_bootom_left_line(bootomArr,rightArr):
    bootomArr.reverse()
    for j in range(len(bootomArr)):
        dataLeft = bootomArr[j]
        dataRight = rightArr[j]
        plt.plot([dataLeft['x'],dataRight['x']],[dataLeft['y'],dataRight['y']])


def plot_grid_line(start, stop, tick, n,type): 
    result = []
    r = np.linspace(0, 1, n+1) 
    x = start[0] * (1 - r) + stop[0] * r 
    x = np.vstack((x, x + tick[0])) 
    y = start[1] * (1 - r) + stop[1] * r 
    y = np.vstack((y, y + tick[1])) 
    rticks = np.arange(0, 1.01, 0.1)
    #for i in range(len(x)):
    for j in range(len(x[1])):
        data = {}
        data['x'] = x[0][j]
        data['y'] = y[0][j]
        result.append(data)
    return result


def plot_create_step(start, stop, tick, n,type): 
    r = np.linspace(0, 1, n+1) 
    x = start[0] * (1 - r) + stop[0] * r 
    x = np.vstack((x, x + tick[0])) 
    y = start[1] * (1 - r) + stop[1] * r 
    y = np.vstack((y, y + tick[1])) 
    rticks = np.arange(0, 1.01, 0.1)
   
    #for i in range(len(x)):
    for j in range(len(x[1])):
        sx = x[1][j]
        sy = y[1][j]
        if type=='bottom':
            sx = x[1][j]
            sy = y[1][j]-0.02
        if type=='right':
            sx = x[1][j]
            sy = y[1][j]
        if type=='left':
            sx = x[1][j]-0.05
            sy = y[1][j]
        #备注开始
        plt.annotate(round(rticks[j], 2),
                        xy=(sx, sy),            # 在(3.3, 0)上做标注
                        fontsize=8,          # 设置字体大小为 16
                        xycoords='data')    # xycoords='data' 是说基于数据的值来选位置


def plot_ticks(start, stop, tick, n): 
    r = np.linspace(0, 1, n+1) 
    x = start[0] * (1 - r) + stop[0] * r 
    x = np.vstack((x, x + tick[0])) 
    y = start[1] * (1 - r) + stop[1] * r 
    y = np.vstack((y, y + tick[1])) 
    plt.plot(x, y, 'k', lw=1) 

   
        

n = 10 
tick_size = 0.2 
margin = 0.05 

# define corners of triangle  
left = np.r_[0, 0] 
right = np.r_[1, 0] 
top = np.r_[0.5, 3**0.5/2] 
triangle = np.c_[left, right, top, left] 

# define vectors for ticks 
bottom_tick = tick_size * (right - top)/n 
right_tick = tick_size * (top - left)/n 
left_tick = tick_size * (left - right)/n 

plt.plot(triangle[0], triangle[1], 'k', lw=2,linestyle='-') 
plot_ticks(left, right, bottom_tick, n) 
plot_ticks(right, top, right_tick, n) 
plot_ticks(left, top, left_tick, n) 

#创建备注坐标
plot_create_step(left, right, bottom_tick, n,'bottom')
plot_create_step(right, top, right_tick, n,'right')
plot_create_step(top, left, left_tick, n,'left')

#收集不同边框的坐标数组
bootomArr = plot_grid_line(left, right, bottom_tick, n,'bottom')
rightArr = plot_grid_line(right, top, right_tick, n,'right')
leftArr = plot_grid_line(left, top, left_tick, n,'left')


# 创建 left right line 
create_left_right_line(leftArr,rightArr)
create_bootom_right_line(bootomArr,rightArr)
create_bootom_left_line(bootomArr,leftArr)
#去掉边框
plt.axis('off')



plt.axis([left[0]-margin, right[0]+margin, left[1]-margin, top[1]+margin]) 
plt.gca().set_aspect('equal', adjustable='box') 
plt.show() 