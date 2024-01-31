#data set
c1<-c(551,457,450,731,499,632)
c2<-c(595,580,508,583,633,517)
c3<-c(639,615,511,573,648,677)
c4<-c(417,449,517,438,415,555)
c5<-c(563,631,522,613,656,679)

type=c(rep("1",6), rep("2",6), rep("3",6), rep("4",6), rep("5",6)) 
weight=c(c1,c2,c3,c4,c5)
dataA=data.frame(type,weight)



#visualizing data
library(mosaic)
library(ggplot2)
library("ggpubr")
ggboxplot(dataA, x="type", y="weight", 
          color="type", palette=c("purple","blue","orange","red","green"),
          ylab="Weight", xlab = "Mixture type")



#normality test of each group
qqnorm(c1)
qqline(c1)
qqnorm(c2)
qqline(c2)
qqnorm(c3)
qqline(c3)
qqnorm(c4)
qqline(c4)
qqnorm(c5)
qqline(c5)

shapiro.test(c1)
shapiro.test(c2)
shapiro.test(c3)
shapiro.test(c4)
shapiro.test(c5)



#homogeneity of variances test
library(car)
leveneTest(weight,type)



#one-way ANOVA Test
weight.anova<-aov(weight~type,data=dataA)
summary(weight.anova)



##Visualization of normality and variance homogeneity tests as a whole
#Normality
e=residuals(weight.anova)
predicted=fitted(weight.anova)
qqnorm(e)
qqline(e)

#Variance homogeneity
plot(predicted,e, xlab="predicted y",ylab="residuals")



#Multiple comparisons of means
PostHocTest(aov(weight~type, data = dataA),method = "hsd")