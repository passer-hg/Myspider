#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup


def get_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    url1 = []
    for k in soup.find_all('article'):
        l = k.a['href']
        url1.append(l)
    # print(url1)
    return url1


def get_content(url1):
    lists = []
    for url2 in url1:
        r = requests.get(url2)
        soup = BeautifulSoup(r.text, 'lxml')
        for content in soup.find_all('article'):
            for cont in content.find_all('img'):
                lists.append(cont['src'])
    return lists


def get_gif(l):
    lists = l
    for list in lists:
        beauty = requests.get(list)
        if beauty.status_code == 200:
            savepath = '/home/hg/gif/{}.gif'.format(lists.index(list))
            with open(savepath, 'xb') as f:
                f.write(beauty.content)


if __name__ == '__main__':
    url = 'http://hnbang.com/category/meinv'
    url1 = get_url(url)
    list = get_content(url1)
    get_gif(list)