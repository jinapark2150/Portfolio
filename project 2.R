#anova test
a<-4
b<-8
response=c(36.05, 42.47, 51.50, 37.55,
           52.47, 85.15, 65.00, 59.30,
           56.55, 63.20, 73.10, 79.12,
           45.20, 52.10, 64.40, 58.33,
           35.25, 66.20, 57.45, 70.54,
           66.38, 73.25, 76.49, 69.47,
           40.57, 44.50, 40.55, 46.48,
           28.34, 35.05, 33.17, 36.20)
dose=rep(c("T1", "T2", "T3", "T4"),b)
cyclist=rep(c("B1", "B2", "B3", "B4","B5", "B6", "B7", "B8"),each=a)
dataA=data.frame(dose,cyclist,response)
dataA.anova=aov(response~dose+cyclist, data=dataA)
summary(dataA.anova)


#normality checking shapiro_test
shapiro.test(response[dose=="T1"])
shapiro.test(response[dose=="T2"])
shapiro.test(response[dose=="T3"])
shapiro.test(response[dose=="T4"])
shapiro.test(response)
#normality checking QQPLOT
e=residuals(dataA.anova)
predicted=fitted(dataA.anova)
fitted.dataA=cbind(dataA, e, predicted)
qqnorm(e)
qqline(e)



#variance checking levene test
library(car)
leveneTest(e,dose)
leveneTest(e,cyclist)
#variance checking predicted vs residuals
library(ggplot2)
plot(predicted,e, xlab="Predicted",ylab="Residuals")

#plots of residuals by treatment (dosage)
ggplot(data=fitted.dataA, aes(x=dose, y=e))+geom_point(size=2, col="blue")+
  xlab("Dosage")+ylab("Residuals")+geom_hline(yintercept=0, linetype="dashed", col="red")+
  ggtitle("Residual Plot Across Treatments")

#plots of residuals by block (cyclist)
ggplot(data=fitted.dataA, aes(x=cyclist, y=e))+geom_point(size=2, col="blue")+
  xlab("Cyclist")+ylab("Residuals")+geom_hline(yintercept=0, linetype="dashed", col="red")+
  ggtitle("Residual Plot Across the Blocks")


#tukey test (comparison)
tukey=TukeyHSD(dataA.anova, conf.level=0.95)
tukey
mplot(tukey)

