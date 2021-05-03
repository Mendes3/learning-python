import requests
from bs4 import BeautifulSoup   # a module to go through a website and sort datas like all header, titles , links etc


def trade_spider():
    url = 'https://fullstackopen.com/en/#course-contents'
    source_code = requests.get(url)
    plain_txt = source_code.text           # we also need the plain texts which includes images, texts etc.
    # BeautifulSoup is a class and soup here is an object.
    # soup object is created by passing a parameter, plain text to BeautifulSoup
    soup = BeautifulSoup(plain_txt,"html.parser")
    # plain_text contains whole source code of the webpage/website.
    # now u can use soup to sort and find all the links or headers in soup
    for classes in soup.findAll('p', {'class': "content-liftup__name"}):
        #href = classes.get('href')
        title = classes.string
        print(title)
        #print(href)

# now building a dynamic web crawler. we can crawl through any website in internet


def get_single_item_data():
    url = 'https://fullstackopen.com/en/#course-contents'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for items in soup.findAll('a',{'class':"nav-item-hover"}):
        href = items.get('href')
        print("https://fullstackopen.com/" + href)
        title = items.string
        print(title)


get_single_item_data()


