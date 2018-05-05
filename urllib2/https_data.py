# -*_ coding: utf-8 -*-

import urllib2
import ssl

# 忽略安全认证
context = ssl._create_default_https_context()

url = "https://kyfw.12306.cn/otn/index/init"
#url = "http://www.lingyima.com"
headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
}
req = urllib2.Request(url, headers = headers)
res = urllib2.urlopen(req, context=context)
data = res.read()
d = data.decode('utf-8')
print(d)


