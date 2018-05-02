# -*- coding: utf-8 -*-

import urllib
import urllib2

url = 'http://www.baidu.com/s'
headers = {"User-Agent": "Mozilla..."}

keyword = raw_input('请输入需要输入的字符串：')
wd = {"wd": keyword}

# urlencode 字典类型变量转换为encode
wd = urllib.urlencode(wd)
fullUrl = url + '?' + wd;

req = urllib2.Request(fullUrl, headers = headers)
res = urllib2.urlopen(req)
print res.read()
print(fullUrl)

