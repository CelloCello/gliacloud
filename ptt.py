# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

board = "Gossiping"
url = "https://www.ptt.cc/bbs/{}/index.html".format(board)
print url

req = requests.session()

r = req.get(url)
print r.url
content = r.content
if 'over18' in r.url:
    print 'over18'

    load = {
        'from': '/bbs/{}/index.html'.format(board),
        'yes': 'yes'
    }
    r = req.post('https://www.ptt.cc/ask/over18', verify=False, data=load)
    content = r.content

#print content
soup = BeautifulSoup(content, 'html.parser')
articles = soup.find_all(class_="r-ent")
print len(articles)
for article in articles:
    meta_obj = article.find(class_="meta")
    date = meta_obj.find(class_="date").text.strip()
    author = meta_obj.find(class_="author").text.strip()
    title = article.find(class_="title").text.strip()
    content_link = article.find("a")['href']
    print title, date, author
    content_url = "https://www.ptt.cc" + content_link
    print content_url
    content_rsp = req.get(content_url)
    content_soup = BeautifulSoup(content_rsp.content, 'html.parser')
    print content_soup.find(id="main-content").text.encode('utf-8')