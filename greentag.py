# -*- coding: utf-8 -*-
'''
@Time   :  2019-May-16 02:40
@Author :  Shang Yehua
@Email  :  niceshang@163.com
@Desc   :  
        find_all
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(),'html.parser')
name_list = bs.find_all('span',{'class':'green'})
for name in name_list:
    print(name.get_text())