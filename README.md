# Shi-Tomasi-Corner-Detector
This repository represents the solution to the assignment.  The main topic represents the theoretical overview with an explanation of the principles of **Shi-Tomasi corner detection**,  Python implementation, and performance comparison with the built-in function of the openCV library designed to solve computer vision problems.

* **Implementation -** contains commented implementation of Shi-Tomasi corner detection in Python with built-in function calls and experimental implementation of the algorithm for the presented assignment. The Main.py also contains the data preparation steps for mathematical experiments listed below.

* **PerformanceExperiments -** processes the output of 1000 measurements of execution times of both built-in function and our implementation with hypothesis tests in R language. 

* **OtherExperiments -** contains statistical comparison and hypothesis tests of detected corners coordinates precision, the number of detected corners, and visual comparison of each method performance. 

* **images -** contains all images needed for testing the performance of the algorithms.


## Theoretical overview

Shi-Tomasi Corner Detection was published by J.Shi and C.Tomasi in their paper ‘Good Features to Track‘ in 1994. This method is based entirely on the Harris corner detector, with the only variation in the corner scoring function.[1]
 
The scoring function in the Harris Corner Detector was given by: 
<img src="https://latex.codecogs.com/svg.latex?\inline&space;\dpi{150}&space;\fn_phv&space;R=\lambda_{1}&space;*&space;\lambda_{2}&space;-&space;k(\lambda_{1}&space;&plus;&space;\lambda_{2})^{2}" title="R=\lambda_{1} * \lambda_{2} - k(\lambda_{1} + \lambda_{2})^{2}" align="center" />

Instead of this, Shi-Tomasi proposed:
<img src="https://latex.codecogs.com/svg.latex?\inline&space;\dpi{150}&space;\fn_phv&space;R=min(\lambda_{1}&space;,&space;\lambda_{2})." title="R=min(\lambda_{1} , \lambda_{2})." align="center" /></a>



## Assignment solution

The main function represents our implemented solution of corner detection.

```python
findCorners(img, maxCor, thresh, dst)
```

* img - represents the image for corner detection
* maxCorners - specifying maximum number of corners
* thresh - is the minimum quality level below which the corners are rejected
* dist - is the minimum euclidean distance between two corners




## Pseudocode
 *.png
 description of variables and if something need clarification in pseudocode
 
## Citations
http://aishack.in/tutorials/shitomasi-corner-detector/?fbclid=IwAR1ayGNsnJca4TBidtq1oPsParBSqj4UFYux-5F427SAsnSTaUqyh4o2JY4
