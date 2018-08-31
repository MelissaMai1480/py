# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:05:39 2017

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
    print(nickname)
    


 # 写入数据  
file = open('C:\Users\mai.mm.2\Desktop/pgtest.csv','w')
for i in list(range(0,len(nickname))):
    file.write(','.join((nickname[i],ratedate[i],color[i],size[i],ratecontent[i]))+'\n',encoding='utf-8')
file.close()

#遍历文件夹的学习
import os
import sys

if __name__=="__main__":
    print os.path.realpath(sys.argv[0])
    print os.path.split(os.path.realpath(sys.argv[0]))
    print os.path.split(os.path.realpath(sys.argv[0]))[0]

import os
import os.path
rootdir = "C:\Users\mai.mm.2\Desktop/check1-2"


for parent,dirnames,filenames in os.walk(rootdir):#分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for dirname in dirnames:#输出信息
        print "parent is:" + parent
        print "dirname is" + dirname
        
    for filename in filenames:
        print "parent is" + parent
        print "filename is"+ filename
        print "the full name of the file is:" + os.path.join(parent,filename)
        

import sys
print 'The name of this program is: %s'%(sys.argv[0])
print 'The command line arguments are：'
for i  in sys.argv: 
    print i 
print 'There are %5 argument.'%(len(sys.argv)-1)

from optparse import OptionParser

parser = OptionParser()
parser.add_option('-f','--file',dest='filename',
                  help='write report too FILE',metavar="FILE")
parser.add_option('-q','--quiet',action="store_false",dest='verbose',default=True,
                  help="don't print stauts message to stdout")

(options,args) = parser.parse_args() 

#0305pandas数据框1-2

import pandas as pd

pd.DataFrame([[1,2,3],[10,20,30],[100,200,300],[1,10,100]],columns=['v1','v2','v3'])

pd.DataFrame({'id':[1,2,3],'name':['Tony','Lily','Jim'],'age':[28,27,29]})

import pandas as pd
irris = pd.read_csv('aa.csv')
irris.head()
#取出species列
irris['species'].head()
#按照某些条件取出行
irris.loc[irris.species == 'setosa',:].head()

irris.loc[(irris.species == 'setosa') & (irris['abc.length']>5),:]
#两个变量值筛选并取出特定变量列a,b,
irris.loc[(irris.species == 'setosa') & (irris['abc.length']>5),'a','b']

#删除a,b列
irris.drop(['a','b'],axis=1).head()

#修改变量名称
irris.rename(columns={'a.b':'a_b','b.a':'b_a'},inplace = True)
irris.head()

#数值类型的转化
import pandas as pd
data = pd.DataFrame({'id':range(4),'age':['13','18','11','18'],'outcome':['15.3','11.8','13.5','11.4']})
data = data.astype({'outcome':'float','age':'int'})
data.dtypes

#数据集的排序
irris.sort_values(by = ['a','b'],ascending=[True,False]).head()
#数据去重
data = pd.DataFrame({'name':['Liu','Li','Chen','Liu'],'age':['28','31','27','28'],'gender':['M','M','M','M']})
data
data.duplicated()

#抽样
train = irris.sample(frac=0.8,random_state=1)
#通过索引的方式，将训练集中的行号排除出去
test = irris.loc[irris.index.isin(train.index),:]

#0306数据框3-4

import pandas as pd
income = pd.read_excel('abc.xlsx')
income.head()
#频数统计gender列
income.gender.value_counts()
#百分比
income.gender.value_counts()/sum(income.gender.value_counts())
#两个变量的交叉统计
pd.crosstab(index=income.gender,columns=income['income level'])

#缺失数据值处理
import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2,3,4],
                   [np.NaN,6,7,np.NaN],
                   [11,np.NaN,12,13],
                   [100,200,300,400,],
                   [20,40,60]],columns=['x1','x2','x3','x4'])
df
#检查缺失情况
print(any(df.isnull()),'/n')
#每一行是否有缺失值，以及缺失比例
is_null = []
null_ratio = []
for col in df.columns:
    is_null.append(any(pd.isnull(df[col])))
    null_ratio.append(float(round(sum(pd.isnull(df[col]))/df.shape[0],2)))
    
print(is_null,'/n',null_ratio,'/n')

#每一行是否有缺失
is_null = []
for index in list(df.index):
    is_null.append(any(pd.isnull(df.iloc[index,:])))
print(is_null,'/n')

#删除含有缺失值的含
df.dropna()
#删除只有缺失值的行
df.drdropna(how='all')
    
#替补法
#前替补
df.fillna(method='ffill')
#向后替补
df.fillna(method='bfill')
#不同列用不同函数替补
df.fillna(value={'x1':df.x1.mean(),
                 'x2':df.x2.median(),
                 'x4':df.x4.max()})
    
# 数据映射
#创造一个判断对象是否含有缺失值的函数
isnull = lambda x : any(pd.isnull(x))
#isnull函数映射到各列（axis=0）
df.apply(func = isnull,axis = 0)
#isnull函数映射到各行
df.apply(func = isnull,axis = 1)
#平均数
df.apply(func = np.mean,axis = 0)
#总数
df.apply(func = np.sum,axis = 0)

#对性别进行分组统计
groupby_gender = income.groupby(['gender'])
groupby_gender.aggregate(np.mean)

#对性别和收入水平进行分组统计
grouped = income.groupby(['gender','income_level'])
grouped.aggregate({'gender':np.mean,'edu_age':np.median})


#自己写着玩
import pandas as pd
import glob

csv_file = glob.glob("C:\Users\mai.mm.2\Desktop\hang\haiying/2yue/*.csv")
df = df = pd.DataFrame(columns=['new_Image_ID'],['image_id'],['image_url_original'],['store_number'] )
for csv in csv_file:
    df = pd.merge(df,pd.read_csv(csv),how='outer')

save = pd.DataFrame(columns=[df,'new_Image_ID'])
save.to_csv('all.csv',index = False)

#重命名文件保留后7位
import os
import shutil
wdir = ("C:\Users\mai.mm.2\Desktop/test")
files_id = os.listdir(wdir)
for files in files_id:
    file = os.path.join(wdir,files)
    files = os.path.join(wdir,files[-11:])
    os.rename(file,files)
    print 


#数据框04
#列合并
import os
import pandas as pd

path = "C:\\Users\\mai.mm.2\\Desktop\\hang\\haiying\\2yue\\"
filenames = os.listdir(path)

dataframes = []
for file in filenames:
    dataframes.append(pd.read_csv(path + file))
alldata = pd.concat(dataframes, ignore_index=Ture)

alldata.head()

#横向合并
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, 
         left_index=False, right_index=False, sort=False, 
         suffixes=('_x', '_y'), copy=True, indicator=False)

#left,right：为需要连接的两张表；
#how：默认对两张表进行内连，'right'，'left'为右连和左连，一般inner和left使用最多；
#on：指定关连两张表的公共字段；
#left_on,right_on：指定left表和right表中需要关连的字段；
#left_index,right_index：指定left表和right表中需要关连的行索引
merge_data = pd.merge(a,b,how='left')
merge_data.head()


#名称不一样，id——ID
merge_data2 = pd.merge(a,b,left_on='ID',right_on='ID',how='left')


#连续变量
import numpy as np
import pandas as pd
age = np.random.randint(low = 12,high = 80,size = 1000)
age = pd.Series(age)
age.describe()

age_cut = pd.cut(age,bins = [0,18,45,60,80],right = False,
                 labels = ['未成年','青年','中年','老年'])
age_cut.head()

#requests
import requests
import json
payload = {'key1':'value1','key2':'value2'}
r = requests.get('http://www.baidu.com',params=payload)
print r.url

r = requests.get('https://github.com/timeline.json')
print r.text
r.json()
r = requests.get('http://www.baidu.com',data=payload)
print(r.text)
r= requests.post('http://www.baidu.com',json=payload)
c = r.json()
print c

import requests
url="http://english.ctrip.com/chinaflights/ListPartial/GetRefundEndorseV2"
payload = {"item":"1285|282|922|880|890|0.74|4|False|False|ADU|1284,280,620,0,0,0,4,False,False|"}
r = requests.post(url,data=payload)
#用json解析，并提取数据
r.text

c = r.json()
print c[1]
print c[1]['ADUText']

#用辅助函数取代复杂表达式
from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)
print(repr(my_values))
print('Red:    ',my_values.get('red'))
#例1
red = my_values.get('red',[''])[0] or 0
print('Red:   %r' % red)
#例2
red = my_values.get('red',[''])
red = int(red[0] if red[0] else 0)
#例3
red = my_values.get('green',[''])
if green[0]:
    green = int(green[0])
else:
    green = 0    
#总结
def get_first_int(values,key,default=0):
    found = values.get(key,[''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found
green = get_first_int(my_values,'green')

#切割序列
a = ['a','b','c','d','f','g','f','h']
print('First four:',a[:4])
print('Last four:',a[-4:])

b = a[4:]
print('Before ', b)
b[1] = 99
print('After ', b)

print('Before ',a)
a[2:7] = [99,22,14]
print('After',a)

b = a[:]
assert b == a and b is not a 

b = a
print('Before',a)
a[:] = [101,102,103]
assert a is b
print('After',a)

#步进式切割
a  = ['red','orange','yellow','green','blue','purple']
odds = a[::2]
evens = a[1::2]
back = a[::-2]
print odds #偶数
print evens  #基数
print back #向前选取偶数

#把字符串反转
x = b'mongoose'
y = x[::-1]
print y

#对utf-8无法奏效
w = '谢谢'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')

#用列表推导替代map和filter
a  = [1,2,3,4,5,6,7,8,9,10]
squares = [x**2 for x in a]
print squares

squares = map(lambda x: x**2, a)

#可以被2整除
even_squares = [x**2 for x in a if x %2 ==0]
print(even_squares)
alt = map(lambda x: x**2,filter(lambda x: x % 2 == 0,a))
assert even_squares == list(alt)

chile_ranks = {'ghos':1,'habanero':2,'cayenne':3}
rank_dict = {rank:name for name,rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [x for row in matrix for x in row]
print(flat)

squared = [[x**2 for x in row] for row in matrix]
print squared

my_list = [
        [[1,2,3],[4,5,6]]
]
flat = [x for sublst1 in my_lists
        for sublist2 in sublist1
            for x in sublist2]
    
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)
        