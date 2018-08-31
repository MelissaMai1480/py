import os
import shutil
import pandas as pd
import requests as req

img_dir = 'C:/Users/mai.mm.2/Desktop/hang/HuaHao/'
csv = 'G:\pg\pampers/storeiii_store_list.csv'

url = 'http://ec2-54-222-132-113.cn-north-1.compute.amazonaws.com.cn:3000/api/v1/images'

task_code ='p102','110','118','126','134','142','150'
takenfrom = '2018-04-01'
takento = '2018-05-31'

df = pd.read_csv(csv)

for s in df.iterrows():
    store_num = s[1]['SFAcode']
    para = '?takenfrom=%s&takento=%s&store_number=%s&task_code=%s&per_page=%s'%(takenfrom,takento,store_num,task_code,str(5))
    r = req.get(url+para)
    jsons = r.json()
    for j in jsons['result']:
        pgurl = j['image_url_original']
        scn_id = j['scene_uid']
        img_id = j['image_id']
        img = '%s_%s_%s.jpg'%(store_num,scn_id,img_id)
        
        print(img)
        
        r_img = req.get(pgurl,stream=True)
        path = os.path.join(img_dir,img)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                shutil.copyfileobj(r_img.raw, f)
        print('Done:' + img)

import os
import shutil
import pandas as pd
import requests as req
df1=[]     
for i in range(1,1000):
    url='https://ec2-54-222-182-81.cn-north-1.compute.amazonaws.com.cn:3000/api/v1/images?show=session_date,task_code,image_id,pg_image_url_original,image_url_original,image_type&per_page=200&page=%s&ssid=1000&category=fem&image_type=display'%(i)
    r = req.get(url,verify=False,auth=("ds_team","4!faDca$#@ufa5!"))
    jsons=r.json()
    for index,j in enumerate(jsons['result']):
        picec=pd.DataFrame([[j['image_id'],j['image_type'],j['image_url_original'],j['session_date'],j['task_code']]],index=[index])
        df1.append(picec)
        print(i,index)
        #tmp = pd.DataFrame([[store_num,image_type,session_date,task_code,scn_id,img_id,image_url_original]],columns=col)
        #df_list = df1.append(tmp)
        
#df_list.to_csv('C:/Users/mai.mm.2/Desktop/hang/Alex/test.csv',index=False,encoding='utf-8')
#print 'Done'        


#图片分割算法的学习        
from PIL import Image
import numpy as np
import cv2


img_path = 'C:\\Users\\mai.mm.2\\Desktop\\hang\\sku\\fem_first\\16752549.jpg'
read = Image.open(img_path)
img = np.array(read)#get numpy object
print(type(img))
print(img.shape)
    

import cv2
#读取图片
img = cv2.imread('C:\\Users\\mai.mm.2\\Desktop\\hang\\sku\\HS\\HS\\17586838.jpg')
#创建窗口
cv2.namedWindow('Image')
#在窗口中显示图片
cv2.imshow('Image',img)

#复制图片
emptyImage2 = img.copy()
cv2.imshow('EmptyImage2',emptyImage2)
#保存图片
cv2.imwrite('.jpg',img,[int(cv2.IMWRITE_PNG_COMPRESSION),6])
cv2.waitKey(0)

cv2.destroyAllWindows()



import requests
import re

# 根据url获取网页html内容
def getHtmlContent(url):
    page = requests.get(url)
    return page.text

# 从html中解析出所有jpg图片的url
# 百度贴吧html中jpg图片的url格式为：<img ... src="XXX.jpg" width=...>
def getJPGs(html):
    # 解析jpg图片url的正则
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)" width')  # 注：这里最后加一个'width'是为了提高匹配精确度
    # 解析出jpg的url列表
    jpgs = re.findall(jpgReg,html)
    
    return jpgs

# 用图片url下载图片并保存成制定文件名
def downloadJPG(imgUrl,fileName):
    # 可自动关闭请求和响应的模块
    from contextlib import closing
    with closing(requests.get(imgUrl,stream = True)) as resp:
        with open(fileName,'wb') as f:
            for chunk in resp.iter_content(128):
                f.write(chunk)
    
# 批量下载图片，默认保存到当前目录下
def batchDownloadJPGs(imgUrls,path = './baidu'):
    # 用于给图片命名
    count = 1
    for url in imgUrls:
        downloadJPG(url,''.join([path,'{0}.jpg'.format(count)]))
        print '下载完成第{0}张图片'.format(count)
        count = count + 1

# 封装：从百度贴吧网页下载图片
def download(url):
    html = getHtmlContent(url)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)
    
def main():
    url = 'http://tieba.baidu.com/p/2256306796'
    download(url)
    
if __name__ == '__main__':
    main()

