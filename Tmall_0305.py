# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 14:08:43 2018

@author: mai.mm.2
"""

# 导入所需的开发模块
import requests
import re

# 创建循环链接
urls = []
for i in list(range(1,5)):
    urls.append('https://rate.tmall.com/list_detail_rate.htm?itemId=555315616493&spuId=861409578&sellerId=2129034002&order=3&currentPage=%s' %i)
    
#构建字段容器   
nickname = []
ratedate = []
color = []
size = []
ratecontent = []

# 循环抓取数据
for url in urls:
    content = requests.get(url).text
    
# 借助正则表达式使用findall进行匹配查询
    nickname.extend(re.findall('"displayUserNick":"(.*?)"',content))
    color.extend(re.findall(re.compile('颜色分类:(.*?);'),content))
    size.extend(re.findall(re.compile('尺码:(.*?);'),content))
    ratecontent.extend(re.findall(re.compile('"rateContent":"(.*?)","rateDate"'),content))
    ratedate.extend(re.findall(re.compile('"rateDate":"(.*?)","reply"'),content))
    print(nickname,color)
    


 # 写入数据  
file = open('C:\Users\mai.mm.2\Desktop/pgtest.csv','w')
for i in list(range(0,len(nickname))):
    file.write(','.join((nickname[i],ratedate[i],color[i],size[i],ratecontent[i]))+'\n',encoding='utf-8')
file.close()
