# # Naver Dictionary Crawling

import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

os.chdir("C:/Users/test/desktop")

# Core Code

want_word = input("word: ")
want_page = int(input("pages: "))
want_title = input("title: ") + ".xlsx"

eng_list = []    
source_list = []
korea_list = []

for i in range(1, want_page + 1):
    req = requests.get('http://endic.naver.com/search_example.nhn?sLn=kr&examType=example&query=' + str(want_word) + '&pageNo=' +str(i))
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    total_package = soup.select("li.utb")
    
    for i in total_package:
        if i.find('a', class_= 'user_ts'):
            print('fuck that')
            pass
        else:
            english= i.find(
                'span', class_='_ttsText'
            )
            source = i.find(
                'a', class_='source'
            )
            korea = i.find(
                'a', class_= 'N=a:xmp.detail'
            )
            
        eng_list.append(english.text)
        if source == None:
            source_list.append("Can't find the source")
        else:
            source_list.append(source.text)
        korea_list.append(korea.text)

df = pd.DataFrame({'English Sentence':eng_list,
                   'Korean': korea_list, 
                   'Source': source_list})
df = df.drop_duplicates(['English Sentence'], keep = 'first')


df.to_excel(want_title, sheet_name = want_title)

