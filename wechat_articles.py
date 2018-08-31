# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 15:42:58 2018

@author: 82389
"""

import requests
import re 
from urllib import request
from bs4 import BeautifulSoup
#抓单篇
def get_chapter_info(chapter_url):

    response = requests.get(chapter_url)
    response.encoding = 'utf-8'
    html = response.text

    #chapter_title = re.findall(r'<title>(.*?)</title>',html,re.S)[0]
    chapter_info = re.findall(r'<div class="rich_media_content " id="js_content">(.*?)</div>',html,re.S)[0]

#数据清洗
    chapter_info = chapter_info.strip()
    chapter_info = chapter_info.replace('</strong>','')
    chapter_info = chapter_info.replace('</p>','')
    chapter_info = chapter_info.replace('<br  />','')
    chapter_info = chapter_info.replace('</strong>','')
    return chapter_info
    
    #url = 'https://mp.weixin.qq.com/s?__biz=MzA4ODY4ODUzNQ==&mid=400848575&idx=1&sn=1bac16048cdfa815835dcd3b699beca8&scene=21#wechat_redirect'
    #info = get_chapterinfo(url)
    #print(info)
#抓文章的url    
def get_chapter_urls(title_url):
    response = requests.get(title_url)
    response.encoding = 'utf-8'
    html = response.text
    titles = BeautifulSoup(html,'html.parser')
    [i.text.strip() for i in titles.findAll('p') if i.text.strip()!='']
    #titles  = re.findall(r'target="_blank" data_ue_src=(.*?)</a>',html,re.S)
    return titles


fb = open('wechat.txt','w')    
url ='https://mp.weixin.qq.com/s/zekjj17ruH4PzcUXjZZGzQ'
title = get_chapter_urls(url)
for i in title:

    chapter_info = get_chapter_info(i[0])
    fb.write(i[1])
    fb.write('\n')
    fb.write(chapter_info)
    print(i[1])
fb.close()

