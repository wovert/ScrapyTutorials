# 大数据时代
## 数据获取的方式
- 企业生产的用户数据：大型互联网公司有海量用户，所以他们积累数据有天然的优势
- 有数意识的中小型企业，也开始积累的数据

## 数据管理咨询公司
- 公司偶很庞大的数据采集团队，通过市场调研、问卷调查、固定的样本检测
- 各行各业公司进行合作、专家对话（数据积累很多年，最后得出科研结果）来采集数据

## 政府/机构提供的公开数据
- 通过各地政府统计上报的数据进行合并；机构都是权威的第三方网站


## 第三方数据平台购买数据
- 通过各个数据交易平台购买各行各业需要的数据

## 爬虫爬去数据
- 市场没有数据，价格太高
- 爬虫工程师，在互联网上定向采集数据


- index.baidu.com
- alizs.taobao.com
- data.weibo.com/index
- index.baidu.com

# 什么是爬虫
> 抓取网页数据的程序

# 爬虫是怎么抓取网页数据
## 网页三大特征
- 每个网页都有自己的**URL**（统一资源定位符）来进行定位
- 网页使用 **HTML** 来描述页面信息
- 网页使用**HTTP/HTTPS协议**来传输HTML数据

## 爬虫的设计思路
1. 确定 URL 地址
2. 通过 http/https 协议获取对应 html 页面
3. 提取 html 页面里有用的数据
	+ 如果需要的，就保存
	+ 页面里的其他 URL, 那就继续执行第二步

# 为什么选择 Python 做爬虫
- 可以做爬虫的语言很多：PHP、Java、C/C++、Python等等
- PHP 不擅长多线程、异步网络支持不够，并发处理能力弱
- 爬虫对速度和效率要求比较高
- Java 的网络爬虫生态圈也很完善，是 Python 爬虫对手，但是Java 语言本身很笨重，代码量很大，重构成本比较高，任何修改都会导致代码的大量变动，爬虫经常需要修改部分采集代码
- C/C++ 运行效率和性能几乎最强，但是学习成本很高，代码成型比较慢。
- Python 语法优美、代码简洁、开发效率高、支持的模块，相关的HTTP请求的模块和html的解析模块非常丰富。强大的Scrapy，以及成熟高效的 Scrpy redis 分布式策略。调用其它接口方便（胶水语言）


1. 抓取 HTML 页面：HTTP 请求的处理：urllib、urllib2、requests
2. 处理后的请求可以模拟浏览器发送请求，后去服务器响应的文件
3. 解析服务器响应的内容：re、xpath、BeautifulSoup4(bs4)、jsonpath、pyquery 等

4. 采集动态HTML、验证码的处理
通用的动态页面采集：**Selenium**, **PhantomJS(无界面)**模拟真实浏览器加载js、ajax等非静态的数据

- Tesseract：机器学习库，机器图像识别系统： 

- 打码平台

5. Scrapy 框架（Scrapy, Pyspider）
- 高定制性高性能（异步网络框架twisted），数据下载速度非常快，提供数据存储、数据下载、提取规则等组件。

6. 分布式策略
- Scrapy redis, 在Scrapy的基础上添加了一套以Redis 数据库为核心的一套组件。支持分布式的共能，主要在Redis里做请求指纹去重、请求分配、数据临时存储。

7. 爬虫、反爬虫、反反爬虫 之间的斗争
- 爬虫做到最后，最头疼的不是复杂的页面，而是与反爬虫运维工程师的斗争

- User Agent、代理、验证码、动态数据加载、加密数据
- 数据价值：是否值得去费劲做发爬虫

1.机器成本：人力成本、数据价值、就不反了，一般做到封IP就结束了
2.面子战争

- 爬虫与反爬虫之间的斗争，最后一定是爬虫获胜。为什么？只要是真实用户可以浏览到网页数据，爬虫就一定能爬下来


8. 根据使用场景：通用爬虫和聚焦爬虫
- 通用爬虫：搜索引擎用的爬虫系统
	+ 目标： 互联网上的所有资源下载，放到办呢第服务器形成备份，进行提取关键词、去掉广告，最后提供一个有用的东西
	+ 抓取流程：
		* 选择URL一部分已有的URL，把这些URL放到带爬虫队列中
		* 从队列里出去这些URL，然后解析DNS得到主机IP，然后去这个IP对应的服务器里下载HTML页面，包存到搜索引擎大哦本地服务器，之后吧这个爬过的URL放入已爬取队列
		* 分析这些网页内容，找出网页里与其他的URL连接，继续执行第二部，直到爬虫条件结束

	+ 搜索引擎如何获取一个新网的 URL
		* 主动向搜索引擎提交网址（zhanzhang.baidu.com->工具->链接提交）
		* 在其他网站里设置外链

		* 搜索引擎和 DNS 服务商进行合作，可以快速收录新的网站
			`搜索引擎 DNS`
	+ 遵守规则
		* **Robots 协议**：爬虫可以爬去网页权限
		* Robots.txt 并不是所有爬虫都遵守，一般只有大型的搜索引擎爬虫才遵守。
	+ 通用爬虫工作流程
		* 爬去网页
		* 存储数据
		* 内容处理
		* 提供检索
		* 排名服务

	+ 所有引擎排名：
		* **PageRank 值**：根据网站的流量（点击量/浏览量/人气）统计，流量越高，排名越靠前，网站越值钱
		* **竞价排名**
	+ 缺点
		* 只能提供文本相关的内容（HTML,WORK.PDF）不能提供多媒体文件（图片，音乐，视频）和二进制文件（程序、脚本）
		* 提供的结果千遍一律，不能针对不同背景领域的人提供不同的搜索结果
		* 不能理解人类语义上检索


- 聚焦爬虫：爬虫程序员写的针对某种内容爬虫
	+ 为了通用爬虫的缺点
	+ 面向需求爬虫，针对某种特定的内容爬去信息，而且保证信息和需求尽可能相关


# urllib2 库
> 所谓网页抓取，就是把URL地址中指定的网络资源从网络流中读取出来，保存到本地。 

- 在Python中有很多库可以用来抓取网页

- urllib2 是 Python2.7 自带的模块(不需要下载，导入即可使用)

- [urllib2 官方文档(https://docs.python.org/2/library/urllib2.html)

- [urllib2 源码](https://hg.python.org/cpython/file/2.7/Lib/urllib2.py)

- urllib2 在 Python3.x 中被改为 **urllib.request**


- 存放路径：/usr/lib/python2.7/urllib7.py
- 第三方模块：/usr/local/lib/python2.7/site-packages

`ua_headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}`

`# 通过 urllib2.Request() 方法构造一个请求对象
url = "http://www.baidu.com/"
req = urllib2.Request(url, headers=ua_headers)`

`# 向指定的URL地址发送请求，并返回服务器响应的类文件对象
res = urllib2.urlopen(req)`

`# 服务器的类文件对象支持 Python 文件对象的操作方法
# read() 方法读取文件里的全部内容，返回字符串
html = res.read()`

`# 返回响应码，200，404， 505
print(res.getcode())`

`# 返回实际数据的实际 UR，防止重定向问题L
print(res.geturl())`

`# 服务器响应的 http 包头
print(res.info())`

`# 打印响应内容python
#print(html)`


# 浏览器历史
- Mosaic 世界上第一个浏览器；美国国家计算机应用中心
- Netscape 网景：Netscape(支持框架)，慢慢开始流行...
- Microsoft : Internet Explorer
- 第一次浏览器大战：网景公司消失

- User Agent 决定用户的浏览器，为了更好的HtML效果
- IE 开了个好头，大家都开始给自己披着 Mozilla 的外皮


- Mozilla 基金组织：Firefox 火狐浏览器, Gecko 内核

- search: useragent大全

- Mozilla: Firefox(Gecko)
- IE: Trident
- Opera: Presto
- Linux: KHTML (like Gecko)
- Apple: Webkit (like KHTML)
- Google: Chrome (like webkit)
- 其他浏览器都是模仿 IE Chrome

# urllib2 模块
- 返回服务器响应的类文件对象
	+ `res = urllib2.urlopen(url)`
- 读取文件里的所有内容
	+ `html = res.read()`

- 设置代理服务
	+ `ua_headers = {"User-Agent":"..."}`
- 构造请求对象
	+ `urllib2.Request(url, headers=us_headers)`
- 向URL地址发送请求，并返回服务器响应的类文件对象
	+ `res = urllib2.urlopen(req)`

- 响应码：`res.getcode()`
- 响应 http 报头： `res.info()`
- 返回实际的URL: `res.geturl()`

- 添加/修改 HTTP 报头
`urllib2.add_header('User-Agent', user_agent);`

- 获取 http 报头信息: 首字母必须大写，其他必须小写
`req.get_header('User-agent')`

- encode 编码(接受的参数是字典)
```
import urllib
m = urllib2.urlencode({'wd':'微名'})
urllib.unquote(m).decode('utf-8')
```

# GET 和 POSt 请求的区别
- GET URL 带参数
	+ 参数在QueryString
- POST URL 不带参数

## POST 请求实例
- [有道翻译](http://fanyi.youdao.com)


# 爬虫关注的是数据来源

- 



