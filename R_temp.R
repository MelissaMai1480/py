
book1<-loadworkbook("book1.xlsx")
getSheets(book1)

#导入工作薄中的sheet数据
sheet1<-readworksheet(book1,"业绩")
sheet2<-readworksheet(book1,"店铺")
fix(sheet1)
fix(sheet2)
names(sheet1)
names(sheet2)
#合并sheet1中的x+y列与sheet2中的x+y列，进行数据提取
hebing<-merge(sheet1,sheet2,by.x=c('x','y'),)