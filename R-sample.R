setwd("C:\\Users\\mai.mm.2\\Desktop\\hang\\report\\report_6\\Reports_Jun\\Fem_Demo")
data<-read.csv("report.csv")

data_sample<-data[sample(nrow(data),3000),]
data_sample$"label"<-apply(data_sample[7:18],1,sum)
#data_sample$"new_Image_ID"<-paste(data_sample$store_number,data_sample$image_id,sep="_")
length(which(data_sample$label>0))
write.csv(data_sample,"baby_sample.csv")

length(which(data_sample$label>0))

setwd("C:\\golden eye\\Manual_check\\Set_report_1011\\1025")
table<-read.csv("fem_demo_sample_1026.csv")
for(j in 8:11){
  for(i in 1:3000){
    if(is.na(table[,j+4][i])){
      table[,j+4][i]=table[,j][i]
    }
  }
}
name1<-"radiant_demo"
name2<-"radiant_demo.1"
length(which(table[,name1]!=0&table[,name2]!=0))
length(which(table[,name1]!=0&table[,name2]==0))
length(which(table[,name1]==0&(table[,name2]!=0)))
length(which(table[,name1]==0&(table[,name2]==0)))


data<-read.csv("fem_demo_th0.92_sept_2017-10-25.csv")
data$"new_Image_ID"<-paste(data$store_number,data$image_id,sep="_")
table_new<-merge(data,table_pre[,c(12:17)],by="new_Image_ID")
write.csv(table_new,"demo_1026.csv")

setwd("C:\\golden eye\\pampers\\report")
data<-read.csv("baby_sunrise_report_conf.csv")
training<-data[which(data$demom6>0.1&data$demom6<0.9|data$demos7>0.1&data$demos7<0.9),]
write.csv(training,"training.csv")

setwd("C:\\golden eye\\rejoice")
rejoice<-read.csv("HC SBD Tracking-Aug.csv")
select<-rejoice[which(rejoice$MW.Tray>0&rejoice$MW.Facing..>0),]
img<-read.csv("aug_api_2017-08-01_08-31_img_url_hc_shelf_0910.csv")
rejoice_training<-img[img$store_num %in% select$store_number_1,]

write.csv(rejoice_training,"rejoice_training1.csv")



setwd("C:\\Users\\li.l.58\\Desktop\\demo")
report<-read.csv("定向日报表20171107142150.csv")
txt<-unique(report$定向名称)
report$时间<-as.Date(report$时间)
report<-report[order(report$Spending),]
for(i in 1:10){
  pic_data<-report[report$定向名称==txt[i],]
  pic_data1<-pic_data[which(pic_data$时间<="2017-10-31"),]
  pic_data2<-pic_data[which(pic_data$时间>"2017-10-31"),]
  if(nrow(pic_data1)==0&nrow(pic_data2)!=0){
    plot(pic_data2$Spending,pic_data2$Conversion,type = "l",main=txt[i],
         xlab="Spending",ylab="Conversion(千分比)",col="royalblue",lwd=2.5)
    legend("bottomright",legend=c("预热"),col="royalblue",lty=1,lwd=2.5)
    savePlot(txt[i], type=c("jpg"),device=dev.cur(),restoreConsole=TRUE)
  }
  else{
    plot(pic_data1$Spending,pic_data1$Conversion,type = "l",main=txt[i],
         xlab="Spending",ylab="Conversion(千分比)",col="brown",lwd=2.5)
    lines(pic_data2$Spending,pic_data2$Conversion,col="royalblue",lwd=2.5)
    legend("bottomright",legend=c("预售","预热"),col=c("brown","royalblue"),lwd=2,lty=1)
    savePlot(txt[i], type=c("jpg"),device=dev.cur(),restoreConsole=TRUE)
  }
}
txt[i]

setwd("C:\\Users\\mai.mm.2\\Desktop\\hang\\haiying\\3yue")
data<-read.csv("BB.csv")
data_sample<-data[sample(nrow(data),15),]
View(data_sample)
write.csv(data_sample,"BB.csv")


