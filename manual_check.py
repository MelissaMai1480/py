# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:33:32 2018

@author: mai.mm.2
"""
#Manual_check_copy_xml
import os
import shutil
ori="C:\\Users\\mai.mm.2\\Desktop\\hang\\report\\report_4yue\\pog/pog"
tar="C:\\Users\\mai.mm.2\\Desktop\\hang\\report\\report_4yue\\pog\\an0.7"
img_id=os.listdir(ori)
for img in img_id:
    xml=os.path.join(tar,img[:-4]+'.xml')
    print os.path.isfile(xml)
    if os.path.isfile(xml):
        ori_xml= os.path.join(ori,img[:-4]+'.xml')
        #ori_xml= os.path.join(ori,img)
        shutil.copy(xml,ori_xml)
        print ori_xml
        
        
#分离label和nolabel
import os
import shutil
wdir="C:\Users\mai.mm.2\Desktop/hang/report/report_4yue/demo/demo"
xml="C:\Users\mai.mm.2\Desktop/hang/report/report_4yue/demo/an0.7"
label="C:\Users\mai.mm.2\Desktop/hang/report/report_4yue/demo/label"
nolabel="C:\Users\mai.mm.2\Desktop/hang/report/report_4yue/demo/nolabel"

for jpg in os.listdir(wdir):
    anno=os.path.join(xml,jpg[:-4]+".xml")
    if os.path.isfile(anno):
        ori_img=os.path.join(wdir,jpg)
        tar_img=os.path.join(label,jpg)
        shutil.copy(ori_img,tar_img)
        print(tar_img)
        
        ori_xml=anno
        tar_xml=os.path.join(label,jpg[:-4]+".xml")
        shutil.copy(ori_xml,tar_xml)
    else:
        ori_img=os.path.join(wdir,jpg)
        tar_img=os.path.join(nolabel,jpg)
        shutil.copy(ori_img,tar_img)
    
#计数
import pandas as pd
table = pd.read_excel('C:\Users\mai.mm.2\Desktop\hang/report/report_4yue/demo/demo.xlsx')

#查看行名称
table.index
#查看列名称
table.columns

#读取3行
table[0:3]
#读取散列

table1=table["radiant_demo"]
table1=table1.reset_index(drop=True)
table2=table["radiant_demo.1"]
table2=table2.reset_index(drop=True)
table2=table2.fillna(1000).astype('int')
def count():
    a=0
    b=0
    c=0
    d=0
    for i in range(len(table1)):
        if table1[i] !=0 and table2[i] !=0:
            a=a+1
        elif table1[i] !=0 and table2[i] ==0:
            b=b+1
        elif table1[i] ==0 and table2[i] !=1000:
            c=c+1
        elif table1[i] ==0 and table2[i] ==1000:
                                  d=d+1
    test1=[a,b,c,d]
    return test1

count=count()
count
    