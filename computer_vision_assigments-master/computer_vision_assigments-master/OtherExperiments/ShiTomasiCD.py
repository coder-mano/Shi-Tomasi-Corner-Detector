import cv2
import numpy as np
import sys
import getopt
import operator
import time


def readImage(filename):
    img = cv2.imread(filename, 0)
    if img is None:
        print('Invalid image:' + filename)
        return None
    else:
        print('Image successfully read...')
        return img

def findCorners(img, window_size, k, thresh):
    #Find x and y derivatives
    dy, dx = np.gradient(img)
    Ixx = dx**2
    Ixy = dy*dx
    Iyy = dy**2
    height = img.shape[0]
    width = img.shape[1]

    cornerList = []
    newImg = img.copy()
    color_img = cv2.cvtColor(newImg, cv2.COLOR_GRAY2RGB)
    offset = int(window_size/25)

    #Search corners in image
    #print("Finding Corners...")
    for y in range(offset, height-offset):
        for x in range(offset, width-offset):
            #Calculate sum of squares
            windowIxx = Ixx[y-offset:y+offset+1, x-offset:x+offset+1]
            windowIxy = Ixy[y-offset:y+offset+1, x-offset:x+offset+1]
            windowIyy = Iyy[y-offset:y+offset+1, x-offset:x+offset+1]
            Sxx = windowIxx.sum()
            Sxy = windowIxy.sum()
            Syy = windowIyy.sum()


            #Find determinant and trace, use to get corner response
            det = (Sxx * Syy) - (Sxy**2)
            trace = Sxx + Syy
            r = min(Sxx,Syy,Sxy)
            #r = det - k*(trace**2)

            #Threshold for corner
            if r > thresh:
                #print(x, y, r)
                cornerList.append([x, y, r])
                #color_img.itemset((y, x, 0), 0)
                #color_img.itemset((y, x, 1), 0)
                #color_img.itemset((y, x, 2), 255)
    return  cornerList
#color_img,

def main():
    
    t1=[]
    t2=[]
    tv=[]
    k = 0.09
    thresh = 10
    
    img = readImage('/Users/Filip/Documents/Documents/Kurzy/Python Learn2code/2.png')

    window_size = (min(img.shape[0], img.shape[1]) / 1000)*5
    if img is not None:
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        if len(img.shape) == 4:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        print("Shape: " + str(img.shape))
        print("Size: " + str(img.size))
        print("Type: " + str(img.dtype))
        print("Printing Original Image...")
        print(img)
        #finalImg, 
        
        for i in range(1000):
            t1.append(time.time())
            cornerList = findCorners(img, int(window_size), float(k), int(thresh))
            t2.append(time.time())
        
        for i in range(1000):
            tv.append(t2[i]-t1[i])
            #print(t2[i],t1[i])
            print(tv[i])
            
        #if finalImg is not None:
            #cv2.imwrite("finalimage.png", finalImg)

        # Top 100 corners
        #cornerList.sort(key=operator.itemgetter(2))
        #outfile = open('corners.txt', 'w')
        #color_img = readImage('/Users/Filip/Documents/Documents/Kurzy/Python Learn2code/2.png').copy()
        #color_img = cv2.cvtColor(color_img, cv2.COLOR_GRAY2RGB)
        #for i in range(100):
        #    outfile.write(str(cornerList[i][0]) + ' ' + str(cornerList[i][1]) + ' ' + str(cornerList[i][2]) + '\n')
         #   color_img.itemset((cornerList[i][1],cornerList[i][0],0),0)
        #    color_img.itemset((cornerList[i][1],cornerList[i][0],1),0)
        #    color_img.itemset((cornerList[i][1],cornerList[i][0],2),255)
        #    cv2.imwrite("topImage.png",color_img)
       # outfile.close()
    t2.append(time.time())
    #print(tv)

if __name__ == "__main__":
    main()