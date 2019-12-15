import FindCorners as fc
import numpy as np
import cv2
import time


def assignmentTest(img, maxCor, thresh, dst):
    outfile = open('../PerformanceExperiments/assignmentCorners.txt', 'w')
    for i in range(1000):
        t1 = time.time()
        fc.findCorners(img, maxCor, thresh, dst)
        t2 = time.time()
        outfile.write(str(t2 - t1) + '\n')
    outfile.close()


def goodFeatureTest(img, maxCor, thresh, dst):
    outfile = open('../PerformanceExperiments/builtInCorners.txt', 'w')
    for i in range(1000):
        t1 = time.time()
        cv2.goodFeaturesToTrack(img, maxCor, thresh, dst)
        t2 = time.time()
        outfile.write(str(t2 - t1) + '\n')
    outfile.close()


def cornerPrecisionTest(img, maxCor, thresh, dst):
    assignmentOutfile = open('../OtherExperiments/assignmentCornersCoordinates.txt', 'w')
    builtInOutfile = open('../OtherExperiments/builtInCornersCoordinates.txt', 'w')

    for i in range(10):
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

    for i in range(100):
        assignmentCorners = fc.findCorners(img, maxCor, thresh, dst)
        builtInCorners = cv2.goodFeaturesToTrack(img, maxCor, thresh, dst)

        assignmentOutfile.write(str(len(assignmentCorners)) + '\n')
        builtInOutfile.write(str(len(builtInCorners)) + '\n')

    builtInOutfile.close()
    assignmentOutfile.close()

def main():
    img = fc.readImage('../images/combined.png')

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

        # Assignment Shi-Tomasi
        assignmentTest(img, maxCorners, thresh, dist)

        # Built-in Shi-Tomasi
        goodFeatureTest(img, maxCorners, thresh, dist)

        # OtherExperiments data preparation
        cornerPrecisionTest(img, maxCorners, thresh, dist)
        cornerNumberTest(img, maxCorners, thresh, dist)

        # Visualization
        color_img = fc.readImage('../images/combined.png')
        color_img = cv2.cvtColor(color_img, cv2.COLOR_GRAY2RGB)

        # Assignment Shi-Tomasi
        assignmentCorners = fc.findCorners(img, maxCorners, thresh, dist)

        for corner in assignmentCorners:
            cv2.circle(color_img, (corner[0], corner[1]), 3, 255, -1)
            cv2.imwrite("../OtherExperiments/assignmentImage.png", color_img)

        color_img = fc.readImage('../images/combined.png')
        color_img = cv2.cvtColor(color_img, cv2.COLOR_GRAY2RGB)

        # Built-in Shi-Tomasi
        builtInCorners = np.int0(cv2.goodFeaturesToTrack(img, maxCorners, thresh, dist))

        for corner in builtInCorners:
            x, y = corner.ravel()
            cv2.circle(color_img, (x, y), 3, 255, -1)
            cv2.imwrite("../OtherExperiments/builtInImage.png", color_img)


if __name__ == "__main__":
    main()
