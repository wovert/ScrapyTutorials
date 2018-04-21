# -*- coding: utf8 -*-
import urllib2
import random

'''
Host: www.baidu.com
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=313EECE6DD32D3CE3B11210E5D44F90E:FG=1; BIDUPSID=313EECE6DD32D3CE3B11210E5D44F90E; PSTM=1519995714; BD_UPN=12314553; BDUSS=FHakI0aFZzd0pCUk5tNGVybTZuRm9CdmwzcEF3RH5mWi1wYTBsaUdSbEVOdXBhQVFBQUFBJCQAAAAAAAAAAAEAAAAPPQTCbGluZ3lpbWFkczIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAESpwlpEqcJaME; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; B64_BOT=1; cflag=15%3A3; BD_HOME=1; H_PS_PSSID=1469_21122_26105; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; PSINO=2
'''
# User-Agent 列表，也可以是代理列表
ua_list = [
  'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
  'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
]
# 在Uer-Agent 列表里随机选择一个 User-Agent
user_agent = random.choice(ua_list);

# 通过 urllib2.Request() 方法构造一个请求对象
url = "http://www.baidu.com/"
req = urllib2.Request(url)

# 添加/修改 HTTP 报头
req.add_header("User-Agent", user_agent);

# 向指定的URL地址发送请求，并返回服务器响应的类文件对象
res = urllib2.urlopen(req)

# get_header 获取一个已有的 http 报头的信息；头字母必须大些，其他的必须小写
print(req.get_header('User-agent'))

# 服务器的类文件对象支持 Python 文件对象的操作方法
# read() 方法读取文件里的全部内容，返回字符串
html = res.read()

# 返回响应码，200，404， 505
print(res.getcode())

# 返回实际数据的实际 UR，防止重定向问题L
print(res.geturl())

# 服务器响应的 http 包头
print(res.info())

# 打印响应内容python
#print(html)
