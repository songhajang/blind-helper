import codecs
from os import truncate
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

positive =[]
negative =[]
posneg = []
pos = codecs.open("./positive_words_self.txt",'rb',encoding='UTF-8')

while True:
    line = pos.readline()
    line = line.replace('\n', '')
    positive.append(line)
    posneg.append(line)

    if not line: break
pos.close()

neg = codecs.open("./negative_words_self.txt",'rb',encoding='UTF-8')

while True:
    line = neg.readline()
    line = line.replace('\n','')
    negative.append(line)
    posneg.append(line)

    if not line:break
neg.close()


label = [0]*4000


my_title_dic ={"title":[], "label":label}

j = 0

for i in range(4):
    num = i * 10 + 1    
    url3 = "https://search.naver.com/search.naver?&where=news&query=%EB%B2%84%EA%B1%B0%ED%82%B9&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=23&start=" + str(num)
    req = requests.get(url3)
    soup = BeautifulSoup(req.text, 'lxml')
    titles = soup.select(".news_tit")

    print(titles)
    print("\n\n\n")

    for title in titles:

        print(title)
        title_data = title.text
        print(title_data)
        print("-----------------")
        print("\n\n\n")
        title_data = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“》]', '', title_data)
        print(title_data)
        my_title_dic['title'].append(title_data)