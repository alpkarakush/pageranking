# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem
from bs4 import BeautifulSoup


class cleanHTML(object):
    def process_item(self, item, spider):
        item[ 'text' ] = [ ' '.join( item['text'] ) ]
        soup = BeautifulSoup( item[ 'text' ][0] )
        item['text'] = soup.get_text()
        return item