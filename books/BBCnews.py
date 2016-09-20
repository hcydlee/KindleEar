#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return BBCnews

class BBCnews(BaseFeedBook):
    title                 = 'BBC News'
    description           = 'BBC News for up-to-the-minute news, breaking news, and feature stories'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_bbcnews.gif"
    coverfile             = "cv_bbcnews.jpg"
    feeds = [
        ('BBC News', 'http://feeds.bbci.co.uk/news/rss.xml?edition=asia')
        ]

