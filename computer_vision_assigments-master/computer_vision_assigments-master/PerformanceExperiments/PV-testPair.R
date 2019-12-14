# Read a txt file 
x <- read.table("~/Documents/Kurzy/Python Learn2code/OutputOfFunctionTvalue.txt")
x

y <- read.table("~/Documents/Kurzy/Python Learn2code/OutputOfGoodFeuturesToTrackTvalue.txt")
y

x=x[,1]
y=y[,1]

#pre x=y
n=1000
alpha = 0.01 # hladina v??znamnosti
di=x-y
d=(1/n)*sum(di)
sd=(1/(n-1))*sum((di-d)^2)
TS=(d/sqrt(sd))*sqrt(n) # testovacie krit??rium
KH=qt(1-alpha/2,n-1) # kritick?? hodnota
cat("Kriticka oblast (-Inf,",-KH,") zjednotenie (",KH,", Inf)")
# vyhodnotenie pomocou kritickej oblasti
if(TS > KH) cat("TS patri do kritickej oblasti, H0 zamietame prijimame H1") else
  if (TS < -KH) cat("TS patri do kritickej oblasti, H0 zamietame prijimame H1") else
    cat("TS nepatri do kritickej oblasti, H0 nezamietame ")

tab=cbind(x,y,di)
tab

#pre x>y
d1=(1/n)*sum(di)
sd1=(1/(n-1))*sum((di-d)^2)
TS1=(d/sqrt(sd))*sqrt(n) # testovacie krit??rium
KH1=qt(1-alpha,n-1) # kritick?? hodnota
cat("Kriticka oblast (",KH1,", Inf)")
# vyhodnotenie pomocou kritickej oblasti
if(TS1 > KH1) cat("TS patri do kritickej oblasti, H0 zamietame prijimame H1") else
    cat("TS nepatri do kritickej oblasti, H0 nezamietame ")


# alebo (bal??k stats)
t.test(x,y,paired = TRUE, conf.level = 0.99)
p=t.test(x,y,paired = TRUE, conf.level = 0.99)$p.value
# vyhodnotenie pomocou p-hodnoty
if(p > alpha)
  cat("p > alpha, H0 nezamietame na hladine alpha") else
    cat("p <= alpha, H0 zamietame prijimame H1")

