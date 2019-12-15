 # 1. Statistical comparison of detected corners precision.


 ## The experiment was oriented to record the outcomes of two algorithms over multiple tests and a comparison of the precision of each corner's coordinates. 
 * H0 hypothesis is based on the presumption that there is no statistically significant difference between their performances.
 * H1 hypothesis determines that the stated null hypothesis was rejected, and there is a statistically significant difference for a given alpha = 0.05.

 ## Methods used to perform the experiments.
 * **Wilcoxon test** is a nonparametric test that compares the values of two groups. A significant result suggests that the values for the two groups are different. 
 ```r
 library(stats)
 p1 = wilcox.test(x[,1],y[,1],conf.level = 0.95, paired = TRUE, alternative = "two.sided")$p.value
 p2 = wilcox.test(x[,2],y[,2],conf.level = 0.95, paired = TRUE, alternative = "two.sided")$p.value
 p=(p1+p2)/2
 ```
 * The **SIGN test** assesses the number of observations in one group that are greater than paired observations in the other group without accounting for the magnitude of the difference. The test is similar in purpose to the two-sample Wilcoxon test but looks specifically at the median value of differences.
 ```r
 library(BSDA)
 p1=SIGN.test(x[,1],y[,1],alternative = "two.sided", conf.level = 0.95)$p.value
 p2=SIGN.test(x[,2],y[,2],alternative = "two.sided", conf.level = 0.95)$p.value
 p=(p1+p2)/2
 ```

 ## Results
 #### Wilcoxon test: `p-value = 0.4427`

 #### SIGN test: `p-value = 0.156567`

 ## Conclusion
 The non-parametric statistical tests encouraged for analyzing the listed algorithms confirmed that there is no statistically significant difference between the precision of coordinates of detected corners.


 <br/>
 <br/>


 # 2. Statistical comparison of the detected number of corners.

 ## The experiment was oriented to record the outcomes of two algorithms over multiple tests and a comparison of the numbers of detected corners
 * H0 hypothesis is based on the presumption that there is no statistically significant difference between the count of found corners.
 * H1 hypothesis determines that the stated null hypothesis was rejected, and there is a statistically significant difference for a given alpha = 0.05.

 ## Methods used to perform the experiments.
 * Wilcoxon test
 ```r
 library(stats)
 p = wilcox.test(x[,1],y[,1],conf.level = 0.95, alternative = "two.sided")$p.value
 ```
 * SIGN test
 ```r
 library(stats)
 p = wilcox.test(x[,1],y[,1],conf.level = 0.95, alternative = "two.sided")$p.value
 ```

 ## Results
 #### Wilcoxon test: `p-value = 1`

 #### SIGN test: `p-value = 1`

 ## Conclusion
 The non-parametric statistical tests encouraged for analyzing the listed algorithms confirmed that there is no statistically significant difference between the precision of coordinates of detected corners. Furthermore, they are equal.


<br/>
<br/>


# 3. Visual comparison of detected corners.
<p float="center">
  <img src="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/blob/master/OtherExperiments/builtInImage.png" width="400" />
  <img src="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/blob/master/OtherExperiments/assignmentImage.png" width="400" /> 
</p>

| Find corners | Good features to track |
|--------------|------------------------|
| <img src="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/blob/master/OtherExperiments/assignmentImage1.png"/> | <img src="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/blob/master/OtherExperiments/builtInImage1.png"/> |
| <img src="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/blob/master/OtherExperiments/assignmentImage3.png"/> | <img src="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/blob/master/OtherExperiments/builtInImage3.png"/> |
| <img src="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/blob/master/OtherExperiments/assignmentImage4.png"/> | <img src="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/blob/master/OtherExperiments/builtInImage4.png"/> |
| <img src="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/blob/master/OtherExperiments/assignmentImage6.png"/> | <img src="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/blob/master/OtherExperiments/builtInImage6.png"/> |
| <img src="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/blob/master/OtherExperiments/assignmentImage99.png"/> | <img src="https://github.com/Coder-mano/Shi-Tomasi-Corner-Detector/blob/master/OtherExperiments/builtInImage99.png"/> |

## Conclusion
As we can see, the differences between the listed algorithms are quite minimal. The occurrences of minor differences in coordinates of some specific corners are caused by Euclidean distance calculation. 

