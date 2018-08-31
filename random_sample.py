k# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:07:40 2017

@author: mai.mm.2
"""

import random
import sys
import os
sys.path.append("C:\Users\mai.mm.2/Downloads\package\py\Lib")

wdir="C:\Users\mai.mm.2\Desktop\report"
csv_dir=os.path.join(wdir,"dis_add.csv")

def loadDataSet():      #general function to parse tab -delimited floats
    dataMat = [","]                #assume last column is target value
    fr = open("C:\Users\mai.mm.2\Desktop\report/dis_add.csv")
    for line in fr.readlines():
        curLine = line.strip().split('\t')
#         fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(curLine)
    return dataMat

def random_sampling(dataMat,3000):
    try:
         slice = random.sample(dataMat, 3000)    
         return slice
         print'datamat'
    except:
         print 'sample larger than population'



         
#图片处理
import Image as img
import os
from matplotlib import pyplot as plot
from skimage import io,transform
import argparse

def show_data(data):
    fig = pot.figure()
    ax = fig.add_subplot(121)
    ax.imshow(data,cmap='gray')
    ax2 = fig.add_subplot(122)
    ax2.imshow(data)
    polt.show()
    
    
if __name__ == "__main__":
    parse = argarse.ArgumentParse()
    parse.add_argumnet('--picpath',help = "the picture' path")
    args = parse.parse_args()
    img_file1 = img.open(args.picpath)#Image读取图片
    one_pixel = img_file1.getpixe1((0,0))[0]
    print "picture's first pixe:",one_pixel  
    print "the picture's size:",img_file1.size#Image读出来是高宽
    show_data(img_file1)
    img_file2 = io.imread(args.picpath)#skimae读图片
    show_data(img_file2)
    print "picture's firstpixel:",img_file2[0][0][0]
    print "the picture's shape:",img_file2.shape#skimage读取高宽通道


#猜数游戏
import random

secret = random.randint(1,99)
guess = 0
tries = 0
print "AHOY! I am the Dread Pirate Boberts,and I have a secret!"
print "It is a number from 1 to 99.I'll give to 6 tries."

while guess !=secret and tries <6:
    guess = input("What's yer guess?")
    if guess < secret:
        print "Too low,ye scurvy dog!"
    elif guess > secret:
        print "Too high,landlubber!"
        
    tries = tries * 1
if guess == secret:
    print "Avast!Ye got it! Found my secret,yr did!"
    
else:
    print "No more guesses! Better luck next time,matey!"
    print "The secret number was",secret
#三重引号字符串
a = '''ddfgg'''



