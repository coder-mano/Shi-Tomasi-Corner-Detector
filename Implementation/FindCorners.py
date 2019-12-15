import cv2
import numpy as np
import operator

def readImage(filename):
    img = cv2.imread(filename, 0)
    if img is None:
        print('Invalid image:' + filename)
        return None
    else:
        print('Image successfully read...')
        return img


def findCorners(img, maxCor, thresh, dst):
    # Pre-processing tests
    # img = imagePreProcessing(img)

    # Find x and y derivatives
    dy, dx = np.gradient(img)
    Ixx = dx ** 2
    Iyy = dy ** 2
    # Ixy = dy*dx

    height = img.shape[0]
    width = img.shape[1]
    offset = 0  # customizable window size offset

    cornerList = []
    # Search corners in image
    for y in range(offset, height - offset):
        for x in range(offset, width - offset):
            # Calculate sum of squares
            windowIxx = Ixx[y - offset:y + offset + 1, x - offset:x + offset + 1]
            windowIyy = Iyy[y - offset:y + offset + 1, x - offset:x + offset + 1]
            # windowIxy = Ixy[y-offset:y+offset+1, x-offset:x+offset+1]

            Sxx = windowIxx.sum()
            Syy = windowIyy.sum()
            # Sxy = windowIxy.sum()

            # Find determinant and trace, for Harris corner detection
            # det = (Sxx * Syy) - (Sxy**2)
            # trace = Sxx + Syy

            # If Sxx(lambda1) and Syy(lambda2) have large positive
            # values, then a corner is found.
            r = min(Sxx, Syy)
            # r = det - k*(trace**2)

            # Threshold for corner
            if r > thresh:
                cornerList.append([x, y, r])

    return filterCornersByDistance(cornerList, dst)[0:maxCor]


def filterCornersByDistance(cornerList, dist):
    cornerList.sort(key=operator.itemgetter(2), reverse=True)  # by r
    eFiltered = [cornerList[0]]
    for x in cornerList:
        bigger = True
        for y in eFiltered:
            # euclidean distance comparison
            if ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** .5 <= dist:
                bigger = False
                break
        if bigger:
            eFiltered.append(x)
    return eFiltered


def imagePreProcessing(img):
    # img = cv2.blur(img, (4, 4))
    # img = cv2.GaussianBlur(img, (3, 3), 0)

    # Laplace 2
    # kernel = np.array([[1, 1, 1],
    #                   [1, -8, 1],
    #                   [1, 1, 1]])

    # Laplace 1
    # kernel = np.array([[0, 1, 0],
    #                   [1, -4, 1],
    #                   [0, 1, 0]])

    # Conv matrix 3x3 1/9
    # kernel = np.ones((3, 3), np.float32) / 9

    # img = cv2.filter2D(img, -1, kernel)
    # cv2.imwrite("testImage.png", img)
    return img

