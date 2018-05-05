# -*_ coding: utf-8 -*-

import urllib
import urllib2

url = "http://yanji.gqsj.cc/user/info"
headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
  "Accept":	"application/json, text/javascript, */*; q=0.01",
  "Content-Type":	"application/x-www-form-urlencoded; charset=UTF-8",
  "Cookie":	"defArea1=%7B%22id%22%3A%22981%22%2C%22parentId%22%3A%2294%22%2C%22path%22%3A%221-8-94-981%22%2C%22name%22%3A%22%5Cu5ef6%5Cu5409%5Cu5e02%22%2C%22fullName%22%3A%22%5Cu5ef6%5Cu5409%5Cu5e02%22%2C%22pinyin%22%3A%22yanjishi%22%2C%22url%22%3A%22yanji%22%2C%22subgroup%22%3A%22Y%22%2C%22enable%22%3A%221%22%2C%22categoryFrame%22%3A%22%22%2C%22hot%22%3A%221%22%2C%22serviceTel%22%3A%220433-2020889%22%2C%22adTel%22%3A%220433-2020889%22%2C%22companyTel%22%3A%220433-6099938%22%2C%22fax%22%3A%22%22%2C%22email%22%3A%22gqsjtech%40163.com%22%2C%22qq%22%3A%22578856191%22%2C%22address%22%3A%22%5Cu5409%5Cu6797%5Cu7701%5Cu5ef6%5Cu5409%5Cu5e02%5Cu6cb3%5Cu5357%5Cu885724%5Cu53f7%5Cu5e02%5Cu653f%5Cu5e9c%5Cu5bf9%5Cu97622%5Cu697c%22%2C%22qr%22%3A%22Uploads%5C%2Fother%5C%2F2018-04-28%5C%2F1524895591_66223.png%22%2C%22money%22%3A%222950.00%22%2C%22levelId%22%3A%223%22%2C%22monthHouseTotalQuota%22%3A%229%22%2C%22monthJobTotalQuota%22%3A%228%22%2C%22yearHouseTotalQuota%22%3A%2210%22%2C%22yearJobTotalQuota%22%3A%229%22%2C%22isAgent%22%3A%22yes%22%7D; Hm_lvt_ea1395decb34bdac57ff724c45a96da3=1525524828; Hm_lpvt_ea1395decb34bdac57ff724c45a96da3=1525525015; UM_distinctid=163305d946911f-05ed896034df878-143f7240-fa000-163305d946a33; mapCity=1; CNZZDATA3332684=cnzz_eid%3D863286765-1525524036-http%253A%252F%252Fchangchun.gqsj.cc%252F%26ntime%3D1525524036; CNZZDATA1260812059=707272905-1525524036-http%253A%252F%252Fchangchun.gqsj.cc%252F%7C1525524036; PHPSESSID=tph8eop2jbkg16vjjra8nt9o21",
  "Host":	"yanji.gqsj.cc",
  "User-Agent":	"Mozilla/5.0 (Windows NT 6.3; W…) Gecko/20100101 Firefox/61.0",
  "X-Requested-With":	"XMLHttpRequest"
}

req = urllib2.Request(url, headers = headers)
data = urllib2.urlopen(req).read()
# d = data.decode('utf-8')

f = 'getfile.html'
fileObj = open(f, 'w+')
fileObj.write(data)
fileObj.close()