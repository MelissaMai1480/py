# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:57:15 2018

@author: mai.mm.2
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
        }

urls = []
for i in range(1,652):
    url = 'http://zdb.pedaily.cn/inv/p%s/' %i
    res = requests.get(url,headers = headers).text
    soup = BeautifulSoup(res,'html.parser')
    urls.extend(['http://zdb.pedaily.cn' + i.find('a')['href'] for i in soup.findAll('dt',{'class':'view'})[1:]])

# 构建空列表，用户后面存储数据
data = []
# 循环抓数
for url in urls:
    # 获取源代码并解析
    res = requests.get(url, headers = headers).text
    soup = BeautifulSoup(res, 'html.parser')
        # 异常处理
    try:
        # 目标数据获取
        financing = soup.find('div',{'class':'info'}).findAll('li')[0].find('a').text
        investment = soup.find('div',{'class':'info'}).findAll('li')[1].find('a').text
        money = soup.find('div',{'class':'info'}).findAll('li')[2].text.split('：')[1]
        turn = soup.find('div',{'class':'info'}).findAll('li')[3].text.split('：')[1]
        date = soup.find('div',{'class':'info'}).findAll('li')[4].text.split('：')[1]
        industry = soup.find('div',{'class':'info'}).findAll('li')[5].find('a').text
    except:
        pass    # 数据存储到字典中
    data.append({
            'financing':financing,
            'investment':investment,
            'money':money,
            'turn':turn,
            'date':date,
            'industry':industry
            })    
    # 停顿，防止反爬
    time.sleep(3)
    
# 将抓取下来的信息构造成数据框对象 
Invest_Events = pd.DataFrame(data)
# 数据导出
Invest_Events.to_excel('C:/Users/mai.mm.2/Desktop/Invest_Events.xlsx', index = False)