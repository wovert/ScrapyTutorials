# 安装 Python 环境

## Windows OS 安装 Python

### Anaconda 安装

国内镜像源下载更快：[清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)

- Scripts 目录有各种可执行文件；如果没有在 path 环境变量，添加 Scripts 目录到 path 环境变量
  - ANACONDA : C:\usr_local\Anaconda3\Scripts
  - Path : %ANACONDA%\Scripts;

- conda 命令
  - 查看安装包: `conda list`
  - 安装包：`conda install requests`

### 官网下载 Python

下载 python-361

Python 目录和 Python\Scripts目录配置到 path 环境变量中

### PyCharm 开发集成工具

## Ubuntu 下安装 Python

root 账户

``` Ubuntu
- Python 安装依赖库
# apt-get install python3-dev build-essential libssl-dev libffi-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev

- 安装 Python
# apt-get install python3

- Python 包管理工具
# apt-get install python3-pip
```

## MacOS 下安装 Python

[Homebrew](https://brew.sh/)

`# brew install python3`

`# python3`

# MongoDB 环境安装

## Windows 下安装 MongoDB

MongoDB 官网下载 Windows 版 MongoDB

安装路径下 MongoDB\Server\3.4 创建数据(与bin同级目录)文件目录 data\db

在MongoDB\Server\3.4\bin 目录下右键打开命令行窗口输入：`mongod --dbpath MongoDB\Server\3.4\data\db`

验证是否安装成功：localhost:27017

``` mongodb
> db
test
> db.test.insert({'a':'b'});
```

启动 mongodb 服务不方便，解决方法

1. 管理员身份运行 cmd; `cd MongoDB\Server\3.4\bin`

2. 新建日志文件：`MongoDB\Server\3.4\data\logs\mongo.log`

3. 配置

``` batch
MongoDB\Server\3.4\bin> mongod --bind_ip 0.0.0.0 --logpath MongoDB\Server\3.4\data\logs\mongo.log --logappend --dbpath MongoDB\Server\3.4\data\db --port 27017 --serviceName "MongoDB" --serviceDisplayName "MongoDB" --install`

--bind_ip IP 绑定ip
--logpath PATH 日志文件目录
--logappend 日志文件追加方式
--dbpath PATH 数据库目录
--port 端口
--serverName 服务名
--serviceDisplayName 服务显示名
--install 安装服务

```

在服务和应用程序 -> 服务 可以查看 MongoDB 服务，这样可以通过服务的形式启动

[Robo 3T](https://robomongo.org/) 可视化查看 MongoDB 数据库工具

## Linux 下安装 MongoDB

``` shell
# apt-get install mongodb

# mongo
> show dbs
> use local
> db.test.insert({'a':'b'})


```

## MacOS 下安装 MongoDB

``` shell
# brew install mongodb
```

# Redis 安装

## Windows 下安装 Redis
[Redis 官网下载]https://redis.io/

可视化界面 [RedisDesktopManager](https://github.com/uglide/RedisDesktopManager)

## Linux 下安装 Redis

``` shell
# apt-get install redis

# redis-cli
> set 'a' 'b'
> get 'a'

- redis 配置文件
# vim /etc/redis/redis.conf
bind 127.0.0.1 注释掉，可以远程连接

requirepass mypassword 连接密码

# sudo service redis restart

# redis-cli
> get 'a'
[error] NOAUTH Authentication required.

# redis-cli -a mypassword
> get 'a'

```

## MacOS 下安装 Redis

``` shell
# brew install redis

```

# MySQL 安装

## Windows 下安装 MySQL

官网下载 MySQL 安装包

安装之后在服务中可以查看 MySQL服务

MySQL 可视化界面 MySQL-Front

## Linux 安装 MySQL

``` shell
# apt-get install mysql-service mysql-client

# mysql -u root -p

# cd /etc/mysql/mysql.conf.d/mysqld.cnf

bind-address= 可以注释调可以远程访问

```

## MacOS 安装 MySQL

`# brew install mysql`