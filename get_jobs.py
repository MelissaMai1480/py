# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 12:55:22 2018

@author: mai.mm.2
"""

import re
import csv
import requests
from tqdm import tqdm
import urllib
from requests.exceptions import RequestException


def get_one_page(city,keyword,region,page):
    
    paras = {
            'jl' : city,
            'kw' : keyword,
            'isadv' : 0,
            'isfilter' : 1,
            'p' : page
    }
    
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Host': 'sou.zhaopin.com',
            'Referer': 'http://www.zhaopin.com/',
            'Accept': 'text/html.application/xhtml+xml,application/xml;q=0.9,image/webq,iamge/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
            }
    
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?' + urllib.urlencode(paras)
    try:
        
        response = requests.get(url,headers=headers)
        
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        return None
    
    
def parse_one_page(html):
    
    pattern = re.compile('<a style=.*? target="_blank">(.*?)</a>.*?'
        '<td class="gsmc"><a href="(>*?)" target="_blank">(.*?)</a>.*?'
        '<td class="zwyx">(.*?)</td>',re.S)
    
    items = re.findall(pattern,html)
    
    for item in items:
        job_name = item[0]
        job_name = job_name.replace('<b>','')
        job_name = job_name.replace('</b>','')
        yield{
                'job': job_name,
                'website': item[1],
                'company':item[2],
                'salary':item[3],
                }
        
def write_csv_file(path,headers,rows):
    with open(path,'a',encoding='utf-8',newline='') as f:
        f_csv = csv.DictWriter(f,headers)
        f_csv.writeheader()
        f_csv.writerows(rows)
        
def write_csv_headers(path,headers):
    
    with open(path,'a',encoding='utf-8',newline='') as f:
        f_csv = csv.DictWriter(f,headers)
        f_csv.writeheader()
        
def write_csv_rows(path,headers,rows):
    
    with open(path,'a',encoding='utf-8',newline='') as f:
        f_csv = csv.DictWriter(f,headers)
        f_csv.writerows(rows)
        
def main(city,keyword,region,pages):
    filename = 'zl_' + city + '_' + keyword + '.csv'
    headers = ['job','website','company','salary']
    write_csv_headers(filename,headers)
    for i in tqdm(range(pages)):
        
        jobs = []
        html = get_one_page(city,keyword,region,i)
        items = parse_one_page(html)
        
        for item in items:
            jobs.append(item)
        write_csv_rows(filename,headers,jobs)
        
if __name__ == '__main__':
    main('广州','python','10')
    
