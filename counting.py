# -*- coding: utf-8 -*-
import urllib
import os
import sys

import urlparse


urls = [
    "http://www.google.com/a.txt",
    "http://gliacloud.com/haha.png",
    "http://www.google.com/b.txt",
    "http://www.google.co.jp/a.txt"
]

paths = {}

for url in urls:
    rst = urlparse.urlparse(url)
    path = rst.path.replace("/", "")
    if path in paths:
        paths[path] = paths[path] + 1
    else:
        paths[path] = 1

for k, v in paths.iteritems():
    print k, v