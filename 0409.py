# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 18:07:51 2018

@author: mai.mm.2
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 10:31:23 2018

@author: ye.ky
"""

import pandas as pd
from pandas import DataFrame
import re
import numpy as np

count=pd.DataFrame(pd.read_excel("C:\\Users\\mai.mm.2\\Desktop\\instrument_brand.xlsx"))
category=pd.DataFrame(pd.read_excel("C:\\Users\\mai.mm.2\\Desktop\\instrument_category.xlsx"))
brand=pd.DataFrame(pd.read_excel("C:\\Users\\mai.mm.2\\Desktop\\instrument_brand.xlsx"))
function=pd.DataFrame(pd.read_excel("C:\\Users\\mai.mm.2\\Desktop\\instrument_benefit.xlsx"))
count["index"]=count.index


category1={}
for i in range(len(category)):
    for j in range(len(count.搜索词)):
        m=''.join(category.iloc[i,0])
        n=''.join(count.搜索词[j])
        pattern = re.compile(m)
        reach= pattern.search(n)
        if reach != None:
            a=1
            category1.setdefault(j,a)
        else:
            continue
category2=pd.DataFrame(list(category1.items()),columns=['index','Category'],index=category1.keys())
count=count.merge(category2,on='index')


brand1={}
for i in range(len(brand)):
    for j in range(len(count.搜索词)):
        m=''.join(brand.iloc[i,0])
        n=''.join(count.搜索词[j])
        pattern = re.compile(m)
        reach= pattern.search(n)
        if reach != None:
            a=1
            brand1.setdefault(j,a)
        else:
            continue
brand2=pd.DataFrame(list(brand1.items()),columns=['index','Brand'],index=brand1.keys())
count=count.merge(brand2,on='index')
		

function1={}
for i in range(len(function)):
    for j in range(len(count.搜索词)):
        m=''.join(function.iloc[i,0])
        n=''.join(count.搜索词[j])
        pattern = re.compile(m)
        reach= pattern.search(n)
        if reach != None:
            h=function.iloc[i,1]
            function1.setdefault(j,[]).append(h)
        else:
            continue
function2=pd.DataFrame(list(function1.items()),columns=['index','Benefit'],index=function1.keys())
count=count.merge(function2,on='index')


count.to_csv("instrument_result.csv",encoding="utf_8_sig")


import pandas as pd
from pandas import DataFrame
import re
import numpy as np


count=pd.DataFrame(pd.read_excel("C:\\Users\\ye.ky\\Desktop\\Dictionary\\instrument_word.xlsx"))
category=pd.DataFrame(pd.read_excel("C:\\Users\\ye.ky\\Desktop\\Dictionary\\dictionary_new\\instrument_category.xlsx"))
brand=pd.DataFrame(pd.read_excel("C:\\Users\\ye.ky\\Desktop\\Dictionary\\dictionary_new\\instrument_brand.xlsx"))
function=pd.DataFrame(pd.read_excel("C:\\Users\\ye.ky\\Desktop\\Dictionary\\dictionary_new\\instrument_benefit.xlsx"))
count['index']=count.index


brand1={}
for i in range(len(brand)):
    for j in range(len(count.搜索词)):
        m=''.join(brand.iloc[i,0])
        n=''.join(count.搜索词[j])
        pattern = re.compile(m)
        reach= pattern.search(n)
        if reach != None:
            h=brand.iloc[i,1]
            brand1.setdefault(j,[]).append(h)
        else:
            continue
brand2=pd.DataFrame(list(brand1.items()),columns=['index','Brand'],index=brand1.keys())
count=count.merge(brand2,on='index',how='outer')


del count['index']
count.to_excel("instrument_result111_brand.xlsx",encoding="utf_8_sig")


