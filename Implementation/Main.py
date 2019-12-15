import FindCorners as fc
import numpy as np
import cv2
import time


def executionTimeTest(img, maxCor, thresh, dst):
    assignmentOutfile = open('../PerformanceExperiments/assignmentCorners.txt', 'w')
    builtInOutfile = open('../PerformanceExperiments/builtInCorners.txt', 'w')

    # 1000 measurements of execution times
    for i in range(1000):
        # Assignment time test
        t1 = time.time()
        fc.findCorners(img, maxCor, thresh, dst)
        t2 = time.time()
        assignmentOutfile.write(str(t2 - t1) + '\n')

        # Built-in time test
        t1 = time.time()
        cv2.goodFeaturesToTrack(img, maxCor, thresh, dst)
        t2 = time.time()
        builtInOutfile.write(str(t2 - t1) + '\n')

    builtInOutfile.close()
    assignmentOutfile.close()


def cornerPrecisionTest(img, maxCor, thresh, dst):
    assignmentOutfile = open('../OtherExperiments/assignmentCornersCoordinates.txt', 'w')
    builtInOutfile = open('../OtherExperiments/builtInCornersCoordinates.txt', 'w')

    for i in range(1000):
        assignmentCorners = fc.findCorners(img, maxCor, thresh, dst)
        builtInCorners = np.int0(cv2.goodFeaturesToTrack(img, maxCor, thresh, dst))

        for corner in assignmentCorners:
            assignmentOutfile.write(str(corner[0]) + ' ' + str(corner[1]) + '\n')
        for corner in builtInCorners:
            builtInOutfile.write(str(corner.ravel()[0]) + ' ' + str(corner.ravel()[1]) + '\n')

    builtInOutfile.close()
    assignmentOutfile.close()


def cornerNumberTest(img, maxCor, thresh, dst):
    assignmentOutfile = open('../OtherExperiments/assignmentCornerNumbers.txt', 'a')
    builtInOutfile = open('../OtherExperiments/builtInCornerNumbers.txt', 'a')

    for i in range(1000):
        assignmentCorners = fc.findCorners(img, maxCor, thresh, dst)
        builtInCorners = cv2.goodFeaturesToTrack(img, maxCor, thresh, dst)

        assignmentOutfile.write(str(len(assignmentCorners)) + '\n')
        builtInOutfile.write(str(len(builtInCorners)) + '\n')

    builtInOutfile.close()
    assignmentOutfile.close()


def visualTest(color_img, img, maxCor, thresh, dst):

    # Assignment Shi-Tomasi
    assignmentCorners = fc.findCorners(img, maxCor, thresh, dst)
    tmpImage = color_img
    for corner in assignmentCorners:
        cv2.circle(tmpImage, (corner[0], corner[1]), 3, 255, -1)
        cv2.imwrite("../OtherExperiments/assignmentImage.png", tmpImage)

    # Built-in Shi-Tomasi
    builtInCorners = np.int0(cv2.goodFeaturesToTrack(img, maxCor, thresh, dst))
    tmpImage = color_img
    for corner in builtInCorners:
        x, y = corner.ravel()
        cv2.circle(tmpImage, (x, y), 3, 255, -1)
        cv2.imwrite("../OtherExperiments/builtInImage.png", tmpImage)


def main():
    # Images for testing
    color_img = fc.readImage('../images/combined.png')
    # color_img = fc.readImage('../images/chess.png')
    # color_img = fc.readImage('../images/simple.png')
    img = color_img

    if img is not None:
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        if len(img.shape) == 4:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)

        # Specifying maximum number of corners as maxCorners
        # thresh is the minimum quality level below which the corners are rejected
        # dist is the minimum euclidean distance between two corners
        maxCorners = 500
        thresh = 0.1
        dist = 10

        # 1000 measurements of execution times
        executionTimeTest(img, maxCorners, thresh, dist)

        # OtherExperiments data preparation
        cornerPrecisionTest(img, maxCorners, thresh, dist)
        cornerNumberTest(img, maxCorners, thresh, dist)

        # Visualization
        color_img = cv2.cvtColor(color_img, cv2.COLOR_GRAY2RGB)
        visualTest(color_img, img, maxCorners, thresh, dist)

if __name__ == "__main__":
    main()
