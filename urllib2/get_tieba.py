# -*- coding: GBK -*-

import urllib
import urllib2

def loadPage(url, fileName):
  """
    ����: ���� URL�������󣬻�ȡ��������Ӧ�ļ�
    url: ��Ҫ��ȥ�� URL ��ַ
    filename: ������ļ���
  """
  print("��������" + fileName)
  headers = {  "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
  req = urllib2.Request(url, headers = headers)
  return urllib2.urlopen(req).read()

def writePage(html, fileName):
  """
    ���ã��� html ����д�뵽����
    html: ��������Ӧ�ļ�����
  """  
  print("���ڱ���" + fileName)
  with open(fileName, 'w+') as f:
    f.write(html)


def tiebaSpider(url, beginPage, endPage):
  """
    ���ã����������������������ϴ���ÿ��ҳ��� URL
    URL: ���� url ��ǰ����
    beginPage: ��ʼҳ
    endPage: ����ҳ
  """
  for page in range(beginPage, endPage + 1):
    pn = (page - 1) * 50
    fileName = '��' + str(page) + 'ҳ.html'
    
    print(fileName)

    fullUrl = url + "&pn=" + str(pn)
    # print(fullUrl)

    html = loadPage(fullUrl, fileName)
    writePage(html, fileName)


if __name__ == "__main__":
  kw = raw_input("��������Ҫ��ȡ����������")
  beginPage = int(raw_input("�����뿪ʼҳ��"))
  endPage = int(raw_input("���������ҳ��"))

  url = 'http://tieba.com/f?'
  key = urllib.urlencode({"kw": kw})
  fullUrl = url + key
  tiebaSpider(fullUrl, beginPage, endPage)

