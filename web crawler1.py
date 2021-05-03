import requests
from bs4 import BeautifulSoup


def get_names():
    url = 'https://clamphook.com/about'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for names in soup.findAll('p', {'class': 'bp3-heading'}):
        href = names.get('href')
        print("https://fullstackopen.com/" + href)
        title = names.string
        print(title)


get_names()

def get_single_item_data():
    url = 'https://clamphook.com/about'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for items in soup.findAll('h',{'class':'bp3-heading'}):
        title = items.string
        print(title)


get_single_item_data()