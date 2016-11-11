#!/usr/bin/env python
#-*- coding:utf-8 -*-

import  requests
from bs4 import BeautifulSoup

number=0

#page=raw_input("please input page:")

#req=requests.get('http://www.qiushibaike.com/hot/page/'+str(page)+'/?s=4915651')

req=

soup=BeautifulSoup(req.text,'html.parser')

items=soup.find_all('div',attrs={"class":"content"})

for item in items:
    number+=1
    span=item.get('span')

    print span

