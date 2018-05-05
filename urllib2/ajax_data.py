# -*_ coding: utf-8 -*-

import urllib
import urllib2

url = "https://movie.douban.com/j/search_tags?type=movie&source=index"
headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
  
  "Accept": "*/*",
  "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
  "Host": "movie.douban.com",
  "Referer": "https://movie.douban.com/",
  "User-Agent":"Mozilla/5.0 (Windows NT 6.3; W…) Gecko/20100101 Firefox/61.0",
  "X-Requested-With":	"XMLHttpRequest"
}

req = urllib2.Request(url, headers = headers)
data = urllib2.urlopen(req).read()
d = data.decode('utf-8')
print(d)


