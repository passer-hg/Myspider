#!/usr/bin/env python3
# -*- coding: utf8 -*-
# 需要考虑一下怎么存储数据，我留这些数据怎么用，怎么保存
# import os
import requests
from bs4 import BeautifulSoup


def get_url(url):
    url1 = url + '/interns'
    lists = []
    for i in range(1, 11):
        data = {'p': i, 'k': 'python'}
        r = requests.get(url1, params=data)
        # print(r.url)
        soup = BeautifulSoup(r.text, 'lxml')
        lists += soup.find_all('div', class_="names cutom_font")
    url_iterm = []
    for list in lists:
        href1 = list.a['href']
        url2 = 'https://www.shixiseng.com'+href1
        # print('url2:  ', url2)
        url_iterm.append(url2)
    return url_iterm


def get_content(url_iterms):
    for url3 in url_iterms:
        print(url3)
        r = requests.get(url3)
        soup = BeautifulSoup(r.text, 'lxml')
        jobname = soup.find('span', class_='job_name').text
        city = soup.find('span', class_='city').text
        demand = soup.find('div', class_='dec_content').text
        print(demand)


if __name__ == '__main__':
    url = 'https://www.shixiseng.com'
    url_iterms = get_url(url)
    get_content(url_iterms)
