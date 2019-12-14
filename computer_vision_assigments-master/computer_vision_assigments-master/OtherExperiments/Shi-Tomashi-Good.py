import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

img = cv2.imread('C:/Users/Filip/Documents/Documents/Kurzy/Python Learn2code/2.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
t1=[]
t2=[]
tv=[]

for i in range(1000):
    t1.append(time.time())
    corners = cv2.goodFeaturesToTrack(gray,500,0.09,10)
    corners = np.int0(corners)
    t2.append(time.time())

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

for i in range(1000):
    tv.append(t2[i]-t1[i])
    #print(t2[i],t1[i])
    print(tv[i])

cv2.imwrite("topImageGood.png",img)
plt.imshow(img),plt.show()