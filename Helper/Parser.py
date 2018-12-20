# -*- coding: utf-8 -*-
import urllib3
from bs4 import BeautifulSoup

from Helper.CSVWriter import CSVWriter


class Parser:

    def __init__(self, base_url):
        self.url = base_url

    @staticmethod
    def get_html(url):
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        return response

    def quantity_pages(self):
        html = self.get_html(self.url)
        text = BeautifulSoup(html.data)
        href = text.find('div', class_='pagination js-pages').find_all('a', class_='pagination-page')[-1].get('href')
        num = href.split('=')[-1]
        return int(num)

    @staticmethod
    def parsing_ad(ads):
        for ad in ads:
            try:
                year = ad.find('a').get('title').split(' ')[2]
            except:
                year = ''

            try:
                price = ad.find('span', class_='price ').get('content')
            except:
                price = ''

            try:
                about_list = ad.find('div', class_='specific-params specific-params_block').text.strip().split(',')
                if 'км' in about_list[0]:
                    mileage = about_list[0].strip()
                    engine = about_list[1].strip()
                    body_type = about_list[2].strip()
                else:
                    mileage = about_list[1].strip()
                    engine = about_list[2].strip()
                    body_type = about_list[3].strip()
            except:
                mileage = ''
                engine = ''
                body_type = ''

            try:
                url = 'https://www.avito.ru' + ad.find('a').get('href')
            except:
                url = ''

            data = {
                'year': year,
                'price': price,
                'mileage': mileage,
                'engine': engine,
                'body_type': body_type,
                'url': url
            }

            CSVWriter.write_csv(data)

    def parsing_page(self, html):
        text = BeautifulSoup(html.data)
        ads1 = text.find('div', class_='js-catalog_before-ads').find_all('div', class_='item_table-wrapper')
        ads2 = text.find('div', class_='js-catalog_after-ads').find_all('div', class_='item_table-wrapper')
        self.parsing_ad(ads1)
        self.parsing_ad(ads2)
