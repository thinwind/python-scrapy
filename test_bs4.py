# -*- coding: utf-8 -*-
'''
@Time   :  2019-May-15 22:15
@Author :  Shang Yehua
@Email  :  niceshang@163.com
@Desc   :  
        测试BeautifulSoup
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError,URLError

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
    bs4 = BeautifulSoup(html.read(),'html5lib')
    print(bs4.h1)
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
else:
    print('It Worked!')