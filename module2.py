import numpy as np
import cv2

#创建一个背景图
img = np.zeros((512,512,3))
#设置三角形定点坐标
pts = np.array([[250,20],[20,500],[480,500]],np.int32)

pts = pts.reshape((-1,1,2))

cv2.polylines(img,[pts],True,(255,255,0))

#显示图形
cv2.imshow('triangle',img)

cv2.waitKey()


