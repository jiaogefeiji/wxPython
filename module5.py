# _*_ coding: utf-8 _*_
import matplotlib.pyplot as plt 
from matplotlib.patches import Polygon 
fig = plt.figure() 
ax = fig.add_subplot(111, aspect='equal') 
ax.add_patch(Polygon([[0,0],[0,1],[1,0]], closed=True,fill=True)) 
ax.set_xlim((0,1)) 
ax.set_ylim((0,1)) 
plt.show()