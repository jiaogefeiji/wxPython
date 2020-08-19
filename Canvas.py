# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
 
# matplotlib采用WXAgg为后台,将matplotlib嵌入wxPython中
matplotlib.use("WXAgg")
 
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.ticker import MultipleLocator, FuncFormatter
 
import pylab
from matplotlib.patches import ConnectionPatch
import matplotlib.patches as mpatches
from matplotlib import pyplot

N = 8
x = [0.506884,0.571535,0.51603,0.734182,0.78354,0.492207,0.51053,0.354755]
y = [0.860554,0.807568,0.675512,0.998336,0.851434,0.573235,0.598598,0.352898]
#x2 = np.random.rand(N)
#y2 = np.random.rand(N)
#x3 = np.random.rand(N)
#y3 = np.random.rand(N)
area = np.random.rand(N) * 100
fig = pyplot.figure()
ax = pyplot.subplot()
ax.scatter(x, y, s=area,marker='v', cmap='Reds', alpha=0.5)
#ax.scatter(x2, y2, s=area, c='green', alpha=0.6)
#ax.scatter(x3, y3, s=area, c=area, marker='v', cmap='Reds', alpha=0.7)  # 更换标记样式，另一种颜色的样式

ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
#ax.set_xlim(1e-1, 1e6)
#ax.set_ylim(1e-2, 1e6)

#小箭头开始

ax.arrow(0.25, 1.5, 0.3, -0.5, head_width=0.02, head_length=0.1, shape="full",fc='red',ec='red',alpha=0.9, overhang=0.5)



ax.plot([0,2],[-0.5,1.5])
ax.plot([0,2],[0,2])
ax.plot([0,2],[0.5,2.5])
ax.text(0.5, 1, 'put some text',ha='right',va='baseline')
ax.grid(True)
pyplot.show()