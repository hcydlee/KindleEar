#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return ChinaDaily

class ChinaDaily(BaseFeedBook):
    title                 = 'China Daily'
    description           = 'China Daily China News'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_chinadaily.gif"
    coverfile             = "cv_chinadaily.jpg"
    feeds = [
        ('China Daily', 'http://www.chinadaily.com.cn/rss/china_rss.xml')
        ]

