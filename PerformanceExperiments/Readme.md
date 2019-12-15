
# 1. Statistical comparison of 1000 measurements of execution times
## The experiment was oriented to record the outcomes of two algorithms over multiple tests and a comparison between execution times of built-in solution and our implementation.
* H0 hypothesis is based on the presumption that there is no statistically significant difference between execution times of listed algorithms.
* H1 hypothesis determines that the stated null hypothesis was rejected, and there is a statistically significant difference for a given alpha = 0.05.

## Methods used to perform the experiments.

#### Shapiro–Wilk test of normality

* H0 Hypothesis of this test is based on the presumption, that the execution times are normally distributed.
* H1 Hypothesis determines that the stated null hypothesis was rejected, and the execution times are not normally distributed for a given alpha = 0.05

```r
library(stats)
p1=shapiro.test(x[,1])$p
p2=shapiro.test(y[,1])$p
```
`p1-value = 1.203137e-44`  and `p2-value = 3.288539e-24` which means the null hypothesis was rejected. The execution times are not normally distributed.


### Wilcoxon test
is a nonparametric test that compares the values of two groups. A significant result suggests that the values for the two groups are different.

```r
library(stats)
p = wilcox.test(x[,1],y[,1],conf.level = 0.95, paired = TRUE, alternative = "two.sided")$p.value
```
### SIGN test
 assesses the number of observations in one group that are greater than paired observations in the other group without accounting for the magnitude of the difference. The test is similar in purpose to the two-sample Wilcoxon test but looks specifically at the median value of differences.

 ```r
 library(BSDA)
 p = SIGN.test(x[,1],y[,1],alternative = "two.sided", conf.level = 0.95)$p.value
 ```
 ## Results
 #### Wilcoxon test: `p-value = 3.330856e-165`

 #### SIGN test: `p-value = 2.220446e-16`

 ## Conclusion
 The non-parametric statistical tests encouraged for analyzing the listed algorithms confirmed that there is a statistically significant difference between the execution times.
