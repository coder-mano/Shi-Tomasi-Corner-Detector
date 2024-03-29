# Shi-Tomasi-Corner-Detector
This repository represents the solution to the assignment.  The main topic represents the theoretical overview with an explanation of the principles of **Shi-Tomasi corner detection**,  Python implementation, and performance comparison with the built-in function of the openCV library designed to solve computer vision problems.


* **<a href="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/tree/master/Implementation">Implementation -</a>** contains commented implementation of Shi-Tomasi corner detection in Python with built-in function calls and experimental implementation of the algorithm for the presented assignment. The Main.py also contains the data preparation steps for mathematical experiments listed below.

* **<a href="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/tree/master/PerformanceExperiments">PerformanceExperiments -</a>** processes the output of 1000 measurements of execution times of both built-in function and our implementation with hypothesis tests in R language. 

* **<a href="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/tree/master/OtherExperiments">OtherExperiments -</a>** contains statistical comparison and hypothesis tests of detected corners coordinates precision, the number of detected corners, and visual comparison of each method performance. 

* **<a href="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/tree/master/images">images -</a>** contains all images needed for testing the performance of the algorithms.


## Theoretical overview

Corner Detection is the fundamental feature for Vision Algorithms. In this paper we will introduce the evolution of the Shi-Tomasi Corner Detection, based on former Harris corner detector.  

“Shi-Tomasi Corner Detection was published by J.Shi and C.Tomasi in their paper ‘Good Features to Track‘ in 1994.”[1] The Shi-Tomasi corner detector is based entirely on the Harris corner detector, with the only variation in the corner scoring function.

One slight variation in a selection criteria made this detector much accurate than Harris corner detector. If Harris corner detector fails with calculation, the Shi tomashi will take it over and make a little change.

Original Harris corner detector has a corner selection criteria, which means that the score is calculated for each pixel. “If the score is above a certain value, the pixel is marked as a corner. The score is calculated using two eigenvalues. That is, you gave the two eigenvalues to a function. The function manipulates them, and gave back a score.”[1]


The scoring function in the Harris Corner Detector was given by: 
<img src="https://latex.codecogs.com/svg.latex?\inline&space;\dpi{150}&space;\fn_phv&space;R=\lambda_{1}&space;*&space;\lambda_{2}&space;-&space;k(\lambda_{1}&space;&plus;&space;\lambda_{2})^{2}" title="R=\lambda_{1} * \lambda_{2} - k(\lambda_{1} + \lambda_{2})^{2}" align="center" />

Instead of this, Shi-Tomasi proposed:
<img src="https://latex.codecogs.com/svg.latex?\inline&space;\dpi{150}&space;\fn_phv&space;R=min(\lambda_{1}&space;,&space;\lambda_{2})." title="R=min(\lambda_{1} , \lambda_{2})." align="center" />

**Built function Good Features to Track -**
From OpenCv we can use function goodFeaturesToTrack. The function finds N strongest corners in an image. For this purpose we have to translate image to grayscale  by using cvtColor from OpenCv. Then we select how many corners we want to find in the image. Then we choose the level of quality which represents the minimum value of corner under which every corner is rejected. Value is between 0-1.

After that we count the minimum of euclidean distance between corners detected. Function finds all corners which are above the minimum value. Then it sorts them by the quality in descending order. After all the function takes first strongest corner and throws away all nearby corners in the range of minimum distance and returns N strongest corners.


<img src="http://aishack.in/static/img/tut/shi-tomasi-region1.jpg" align="center" />

 - Green area is for accepted corners. λ1 and λ2 are greater than a certain value. 
 - In the blue and gray regions, λ1 or λ2 is less than selected minimum .
 - In the red region, both λ1 and λ2 are less than the required minimum.

<br/>

## Assignment implementation overview


The final implementation is divided into two parts:
* **FindCorners.py -** includes the implementation of the Shi-Tomasi corner detector algorithm for the assignment
* **Main.py** - contains all functions performing data preparation for experiments


### FindCorners.py
The main function represents our implemented solution of Shi-Tomasi corner detection.

```python
def findCorners(img, maxCor, thresh, dst):
```
Returns the list of [x, y, r] arrays where the x, y represents the coordinates of the corner, and r represents the overall score.

* **img -** represents the image for corner detection
* **maxCorners -** specifying maximum number of corners
* **thresh -** is the minimum quality level below which the corners are rejected
* **dist -** is the minimum euclidean distance between two corners

```python
def findCorners(img, maxCor, thresh, dst):
# Find x and y derivatives
dy, dx = np.gradient(img)
Ixx = dx ** 2   #Laplace oparators
Iyy = dy ** 2

cornerList = []
# Search corners in image
for y in range(offset, height - offset):
    for x in range(offset, width - offset):
    
        # Calculate sum of squares
        windowIxx = Ixx[y - offset:y + offset + 1, x - offset:x + offset + 1]
        windowIyy = Iyy[y - offset:y + offset + 1, x - offset:x + offset + 1]
        Sxx = windowIxx.sum()
        Syy = windowIyy.sum()

        # If Sxx and Syy have large positive values - then a corner is found.
        r = min(Sxx, Syy)
        
        # Threshold for corner
        if r > thresh:
            cornerList.append([x, y, r])

# Returns the list of filtered corners by euclidean distance threshold.
return filterCornersByDistance(cornerList, dst)[0:maxCor]
```

### Main.py
```python
def executionTimeTest(img, maxCor, thresh, dst):
```
Performs 1000 measurements of execution times
* **findCorners()** time measurement output - `/PerformanceExperiments/assignmentCorners.txt`
* **goodFeaturesToTrack()** time measurement output - `/PerformanceExperiments/builtInCorners.txt`

<br/>

```python
def cornerPrecisionTest(img, maxCor, thresh, dst):
```
Performs 1000 measurements of detected corners precision.
* **findCorners()** corners coordinates output - `/OtherExperiments/assignmentCornersCoordinates.txt`
* **goodFeaturesToTrack()** corners coodinates output - `/OtherExperiments/builtInCornersCoordinates.txt`

<br/>

```python
def cornerNumberTest(img, maxCor, thresh, dst):
```
Performs 1000 measurements of the detected number of corners.
* **findCorners()** number of corners output - `/OtherExperiments/assignmentCornerNumbers.txt`
* **goodFeaturesToTrack()** number of corners output - `/OtherExperiments/builtInCornerNumbers.txt`

<br/>

```python
def visualTest(color_img, img, maxCor, thresh, dst):
```
Draws all  the detected corners on two separate test images.
* **findCorners()** image output - `/OtherExperiments/assignmentImage.png`
* **goodFeaturesToTrack()** image output - `/OtherExperiments/builtInImage.png`

<br/>

## Pseudocode
<img src="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/blob/master/PseudocodeShi-Tomashi.png"/>
 
## Citations
1.Sinha, Utkarsh. Fundamentals of Feutures and Corners. [online]. 2016. [15.12.2019]. Available on the Internet: <http://aishack.in/tutorials/shitomasi-corner-detector/>



