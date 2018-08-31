setwd("C:\\golden eye\\Manual_check\\Set_report_1011\\PTN")
data<-read.csv("ptn_sept_2017-10-09.csv")
setwd("C:\\golden eye\\pampers\\API\\API_shelf_1\\API_2031_09132")
jpg<-list.files(pattern=".jpg")
setwd("C:\\golden eye\\Manual_check\\0914\\FEM_Demo")
jpg1<-list.files(pattern=".jpg")
jpg2<-jpg1[!jpg1 %in% jpg]
jpg_view<-c(jpg2,jpg[1:2173])
jpg_<-gsub(".jpg","",jpg_view)
setwd("C:\\golden eye\\pampers\\API\\API_shelf_1")
xml<-list.files(pattern=".xml")
xml_<-gsub(".xml","",xml)
jpg_no<-jpg_[!jpg_ %in% xml_]
label_list<-data[data$new_Image_ID %in% xml_,]
nolabel_list<-data[data$new_Image_ID %in% jpg_no,]
write.csv(label_list,"API_shelf_label_list1.csv")
write.csv(nolabel_list,"API_shelf_nolabel_list1.csv")

table(data$type)
data_sample<-data[sample(nrow(data),3000),]
data_sample$"label"<-apply(data_sample[8:9],1,sum)
data_sample$"new_Image_ID"<-paste(data_sample$store_number,data_sample$image_id,sep="_")
write.csv(data_sample,"PTN_sample.csv")

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



setwd("C:\\Users\\li.l.58\\Desktop")
report<-read.csv("定向日报表20171107142150.csv")
txt<-unique(report$定向名称)
report$时间<-as.Date(report$时间)
report<-report[order(report$Spending),]
for(i in 12:43){
  pic_data<-report[report$定向名称==txt[i],]
  pic_data1<-pic_data[which(pic_data$时间<="2017-10-31"),]
  pic_data2<-pic_data[which(pic_data$时间>"2017-10-31"),]
  plot(pic_data1$Spending,pic_data1$Conversion,type = "l",main=txt[i],
       xlab="Spending",ylab="Conversion%%",col="brown",lwd=2.5)
  lines(pic_data2$Spending,pic_data2$Conversion,col="royalblue",lwd=2.5)
  legend("bottomright",legend=c("预售","预热"),pch=c(22,16),col=c("brown","royalblue"),lwd=2,ty)
  savePlot(txt[i], type=c("jpg"),device=dev.cur(),restoreConsole=TRUE)
}
for(i in 10:13){
  pic_data<-report[report$定向名称==txt[i],]
  pic_data2<-pic_data[which(pic_data$时间>"2017-10-31"),]
  plot(pic_data2$Spending,pic_data2$Conversion,type = "l",main=txt[i],
       xlab="Spending",ylab="Conversion%%",col="brown",lwd=2.5)
  legend("bottomright",legend=c("预热"),pch=c(22,16),col="royalblue",lwd=2,type="l")
  savePlot(txt[i], type=c("jpg"),device=dev.cur(),restoreConsole=TRUE)
}