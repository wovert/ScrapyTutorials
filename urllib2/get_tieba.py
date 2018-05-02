# -*- coding: GBK -*-

import urllib
import urllib2

def loadPage(url, fileName):
  """
    作用: 根据 URL发送请求，获取服务器响应文件
    url: 需要爬去的 URL 地址
    filename: 处理的文件名
  """
  print("正在下载" + fileName)
  headers = {  "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
  req = urllib2.Request(url, headers = headers)
  return urllib2.urlopen(req).read()

def writePage(html, fileName):
  """
    作用：将 html 内容写入到本地
    html: 服务器响应文件内容
  """  
  print("正在保存" + fileName)
  with open(fileName, 'w+') as f:
    f.write(html)


def tiebaSpider(url, beginPage, endPage):
  """
    作用：贴吧爬虫调度器，负责组合处理每个页面的 URL
    URL: 贴吧 url 的前部分
    beginPage: 起始页
    endPage: 结束页
  """
  for page in range(beginPage, endPage + 1):
    pn = (page - 1) * 50
    fileName = '第' + str(page) + '页.html'
    
    print(fileName)

    fullUrl = url + "&pn=" + str(pn)
    # print(fullUrl)

    html = loadPage(fullUrl, fileName)
    writePage(html, fileName)


if __name__ == "__main__":
  kw = raw_input("请输入需要爬取得贴吧名：")
  beginPage = int(raw_input("请输入开始页："))
  endPage = int(raw_input("请输入结束页："))

  url = 'http://tieba.com/f?'
  key = urllib.urlencode({"kw": kw})
  fullUrl = url + key
  tiebaSpider(fullUrl, beginPage, endPage)

