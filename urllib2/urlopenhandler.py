# -*- coding: utf-8 -*-

import urllib2

# 构建一个 HTTPHandler 构建起对象，支持处理HTTP的请求
# debuglevel=1 自动打开debug log 模式
http_handler = urllib2.HTTPHandler(debuglevel=1)

# 使用build_opener() 方法构建一个自定义的opener
opener = urllib2.build_opener(http_handler)

url = 'http://www.baidu.com'
req = urllib2.Request(url)
res = opener.open(req)
content = res.read()
#print(content)