import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    words_lists = []
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    for items in soup.findAll('span',{'class':'mw-headline'}):
        content = items.string
        if content:
            words = content.split()
        for each_word in words:
            words_lists.append(each_word)
            print(each_word)
    clear_symbols(words_lists)


def clear_symbols(words_lists):
    clean_lists = []

    for word in words_lists:
        symbols = "~!@#$%^&*()_+:\"<>?/*-=-;,.\'/"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_lists.append(word)
    create_dictionary(clean_lists)


def create_dictionary(clean_lists):
    word_count = {}
    for word in clean_lists:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(),key=operator.itemgetter (1 )):
        print(key,value)


start('https://en.wikipedia.org/wiki/Main_Page')
