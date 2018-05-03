# -*_ coding: utf-8 -*-

import urllib
import urllib2

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
  "Accept":	"application/json, text/javascript, */*; q=0.01",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "Host": "fanyi.youdao.com",
  "Referer": "http://fanyi.youdao.com/",
  "User-Agent": "Mozilla/5.0 (Windows NT 6.3; W…) Gecko/20100101 Firefox/60.0",
  "X-Requested-With":	"XMLHttpRequest"
}
key = raw_input("Please Input you word:")
formdata = {
  "keyfrom": "fanyi.web",
  "action": "FY_BY_REALTIME",
  "client": "fanyideskweb",
  "doctype":	"json",
  "from":	"AUTO",
  "smartresult":	"dict",
  "to":	 "AUTO",
  "typoResult": "false",
  "version": "2.1",
  "i":	  key,
  "salt":"1525350541578",
  "sign":"4646125a297f7c11475187f7d9352f5e",
}

data = urllib.urlencode(formdata)
req = urllib2.Request(url, data = data, headers = headers)
print(urllib2.urlopen(req).read())


