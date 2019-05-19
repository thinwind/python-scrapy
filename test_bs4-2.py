# -*- coding: utf-8 -*-
'''
@Time   :  2019-May-15 23:59
@Author :  Shang Yehua
@Email  :  niceshang@163.com
@Desc   :  
        测试bs4
'''

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    
    try:
        bs = BeautifulSoup(html.read(),'html.parser')
        title = bs.body.h1
        return title
    except:
        return None

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not found')
else:
    print(title)