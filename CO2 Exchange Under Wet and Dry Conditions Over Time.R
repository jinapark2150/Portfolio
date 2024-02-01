library(car)
library(mosaic)
library(ggplot2)
library(ggpubr)
#------------------------------------------------
a=2
b=4
n=3
treatmenttype=rep(c("Dry","Wet"),each=3)#n
treatment=rep(treatmenttype, 4)#b
Timepoint=rep(c("T1","T2","T3","T4"),each=6)#a*n
CO2=c(-1.397, -2.402, -1.358, -1.160, -1.470, -1.878,
      -0.699, -1.201, -0.970, -1.367, -1.617, -2.442,
      -0.873, -1.502, -0.194, -0.410, -0.735, -0.376,
      -0.524, -1.201, 0.388, 0.410, 0.735, 0.376)
exchange=data.frame(treatment,Timepoint,CO2)

exchange.aov=aov(CO2~treatment*Timepoint, data=exchange) 
summary(exchange.aov)
#------------------------------------------------
e=residuals(exchange.aov) 
fitted=fitted(exchange.aov) 
fitted.exchange=cbind(exchange, e, fitted)

shapiro.test(e)

ggplot(data=fitted.exchange, aes(sample=e))+stat_qq(size=2, col="blue")+stat_qqline(col="red")+ 
  ggtitle("Normal Probability Plot of the Residuals") 
#------------------------------------------------
ggplot(data=fitted.exchange, aes(x=fitted, y=e))+geom_point(size=2, col="blue")+xlab("Fitted Values")+
  ylab("Residuals")+geom_hline(yintercept=0, linetype="dashed", col="red")+
  ggtitle("Plot of Residuals versus Fitted Values")

ggplot(data=fitted.exchange, aes(x=treatment, y=e))+geom_point(size=2, col="blue")+xlab("Treatment Type")+
  ylab("Residuals")+geom_hline(yintercept=0, linetype="dashed", col="red")+
  ggtitle("Plot of Residuals versus treatment(dry,wet) Factor")

ggplot(data=fitted.exchange, aes(x=Timepoint, y=e))+geom_point(size=2, col="blue")+xlab("Timepoint")+
  ylab("Residuals")+geom_hline(yintercept=0, linetype="dashed", col="red")+
  ggtitle("Plot of Residuals versus Timepoint Factor")

leveneTest(e,treatment)
leveneTest(e,Timepoint) 
#------------------------------------------------
#visualizing data
ggboxplot(data=exchange, x="Timepoint", y="CO2", col="treatment")+
  ggtitle("Boxplots for the Battery Design Experiment")

ggline(data=exchange, x="Timepoint", y="CO2",col="treatment",
       add=c("mean_se", "dotplot"))+geom_hline(yintercept = 0, linetype="dashed", col= "red")
#------------------------------------------------
#Multiple Comparisons
par(mfrow=c(1,1))
interaction.plot(Timepoint, treatment, CO2, col=2:4, xlab="Timepoint", 
                 ylab="Average CO2 concentration", main="Treatment-Timeplot Interaction Plot")

#Dry
mean.T1D=mean(CO2[Timepoint=="T1" & treatment=="Dry"]) 
mean.T2D=mean(CO2[Timepoint=="T2" & treatment=="Dry"]) 
mean.T3D=mean(CO2[Timepoint=="T3" & treatment=="Dry"]) 
mean.T4D=mean(CO2[Timepoint=="T4" & treatment=="Dry"]) 
mean.T1D
mean.T2D
mean.T3D
mean.T4D

#HSD
edf=a*b*(n-1)
qtukey(0.95, a, edf)

mse=0.250
HSD=qtukey(0.95, a, edf)*sqrt(mse/n)
HSD


abs(mean.T1D-mean.T2D)>HSD
abs(mean.T1D-mean.T3D)>HSD
abs(mean.T1D-mean.T4D)>HSD
abs(mean.T2D-mean.T3D)>HSD
abs(mean.T2D-mean.T4D)>HSD
abs(mean.T3D-mean.T4D)>HSD



#Wet
mean.T1W=mean(CO2[Timepoint=="T1" & treatment=="Wet"]) 
mean.T2W=mean(CO2[Timepoint=="T2" & treatment=="Wet"]) 
mean.T3W=mean(CO2[Timepoint=="T3" & treatment=="Wet"]) 
mean.T4W=mean(CO2[Timepoint=="T4" & treatment=="Wet"]) 
mean.T1W
mean.T2W
mean.T3W
mean.T4W

abs(mean.T1W-mean.T2W)>HSD
abs(mean.T1W-mean.T3W)>HSD
abs(mean.T1W-mean.T4W)>HSD
abs(mean.T2W-mean.T3W)>HSD
abs(mean.T2W-mean.T4W)>HSD
abs(mean.T3W-mean.T4W)>HSD
