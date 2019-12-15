
library(stats)
library(BSDA)

# 1. Statistical comparison of detected corners precision.
x <- read.table("assignmentCorners.txt")
y <- read.table("builtInCorners.txt")
alpha = 0.05

# Distribution test
p1=shapiro.test(x[,1])$p
p2=shapiro.test(y[,1])$p

if(p1>alpha) cat("H0 the execution times are normally distributed.") else cat("H1 the execution times are not normally distributed.")
if(p2>alpha) cat("H0 the execution times are normally distributed.") else cat("H1 the execution times are not normally distributed.")


# Wilcox precision test
p = wilcox.test(x[,1],y[,1],conf.level = 0.95, paired = TRUE, alternative = "two.sided")$p.value
if(p1>alpha) cat("H0 no signifiant difference") else cat("H1 signifiant difference")

# SIGN test
library(BSDA)
p = SIGN.test(x[,1],y[,1],alternative = "two.sided", conf.level = 0.95)$p.value
if(p>alpha) cat("H0 no signifiant difference") else cat("H1 signifiant difference")

