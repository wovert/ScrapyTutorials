# -*- coding: utf-8 -*-

import urllib2

# 代理开关，表示是否启用代理
proxy_status = True

# http://www.xicidaili.com/

#proxy_url = {"http": "user.password@218.72.66.141:18118"}
proxy_url = {"http": "218.72.66.141:18118"}
http_proxy_handler = urllib2.ProxyHandler(proxy_url)
null_proxy_handler = urllib2.ProxyHandler({})
if proxy_status:
  opener = urllib2.build_opener(http_proxy_handler)
else:
  opener = urllib2.build_opener(null_proxy_handler)

urllib2.install_opener(opener)

url = 'http://www.baidu.com/'
req = urllib2.Request(url)
res = urllib2.urlopen(req)
print(res.read())