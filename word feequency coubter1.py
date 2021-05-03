import requests
from bs4 import BeautifulSoup
import operator

def get_words_from_webpage(url):
    words_lists = []

    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for word in soup.findAll('a',{'class':'xs-text-charcoal decoration-none'}):
        title = word.string
        if title:
            words = title.lower().split()
        for each_word in words:
            words_lists.append(each_word)
            #print(each_word)
    clean_symbols(words_lists)


def clean_symbols(words_lists):
    clear_lists = []
    for each_word in words_lists:
        symbols = "'`!~#$%^&*()_+{}|:\"<>?-=[];,./"
        for i in range(0,len(symbols)):
            each_word = each_word.replace(symbols[i], "")
        if len(each_word) > 0:
            clear_lists.append(each_word)
        #print(each_word)
    frequency_counter(clear_lists)

def frequency_counter(clear_lists):
    word_count = {}
    for word in clear_lists:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key,value in sorted(word_count.items(),key=operator.itemgetter(0)):
        print(key, value)



get_words_from_webpage('https://www.timeout.com/newyork/movies/best-movies-of-all-time')