# -*- coding: utf8 -*-
import urllib2

# 向指定的URL地址发送请求，并返回服务器响应的类文件对象
res = urllib2.urlopen("http://www.baidu.com/")

# 服务器的类文件对象支持 Python 文件对象的操作方法
# read() 方法读取文件里的全部内容，返回字符串
html = res.read()

# 打印响应内容python
print(html)
