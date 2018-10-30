# 概述

本次主体为**influxDB**，简述influxDB的市场情况。

# 目的

## 1. 了解事件序列数据库

​	时间序列数据库（TSDB）是针对带时间戳或时间序列数据优化的数据库。时间序列只是随时间跟踪，监控，下采样和聚合的度量或事件。这可以是服务器指标，应用程序性能监控，网络数据，传感器数据，事件，点击，市场交易以及许多其他类型的分析数据。

​	随着系统监控以及物联网的发展，已经开始受到更多的关注。 维基百科上对于时间序列的定义是‘一系列数据点按照时间顺序排列’， 但是我个人的理解是**存储在服务端的客户端历史**。 时间序列数据就是历史，它具有**不变性**, **唯一性**以及**可排序性**。 并且**数据到达服务器的顺序并不影响正确性**，根据数据本身可以直接进行排序和去重。

## 2. 时序数据库的优势

### 1. 低冗余

​	同一数据源的tags不再冗余存储。一个Block内的数据都共用一个SeriesKey，只需要将这个SeriesKey写入这个Block的Trailer部分就可以。大大降低了时序数据的存储量。

### 2. 独立储存

​	时间序列和value可以在同一个Block内分开独立存储，独立存储就可以对时间列以及数值列分别进行压缩。InfluxDB对时间列的存储借鉴了Beringei的压缩方式，使用delta-delta压缩方式极大的提高了压缩效率。而对Value的压缩可以针对不同的数据类型采用相同的压缩效率。

### 3. 高效

​	对于给定数据源以及时间范围的数据查找，可以非常高效的进行查找。

## 3. 传统数据库的劣势

### 1. 高并发和大规模

​	时间序列数据累计速度非常快。（例如，一辆联网汽车[每小时能收集25G），常规数据库在设计之初并非处理这种规模的数据，关系型数据库处理大数据集的效果非常糟糕。

### 2. 可用性

​	TSDB通常还包括一些共通的对时间序列数据分析的功能和操作：数据保留策略、连续查询、灵活的时间聚合等。即使当下不考虑规模（例如，您刚开始收集数据），这些功能仍可提供更好的用户体验，使你的生活更轻松。

# 主要方式

### 1. github

### 2. API文档

### 3. API测试

### 4. 论坛介绍

# 主要内容

## 1. 运行influxdb

​	此次测试使用docker 镜像进行测试，未做实际部署。

### 1. 获取influxdb 的docekr镜像

> docker pull influxdb

​	容器运行：

```
docker run -p 8086:8086 -v $PWD:/var/lib/influxdb  influxdb
```

### 2. 操作

#### 1. 使用HTTP API操作

​	执行查询，`GET`请向`/query`端点发送请求，将URL参数设置`db`为目标数据库，并将URL参数设置`q`为查询。您也可以`POST`通过发送相同参数作为URL参数或作为正文的一部分来使用请求`application/x-www-form-urlencoded`：

```shell
curl -G 'http://localhost:8086/query?pretty=true' --data-urlencode "db=mydb" --data-urlencode "q=SELECT \"value\" FROM \"cpu_load_short\" WHERE \"region\"='us-west'"
```

​	InfluxDB返回JSON, 查询结果显示在`"results"`数组中。在单个API调用中向InfluxDB发送多个查询。只需使用分号分隔每个查询。

​	InfluxDB支持多种查询：时间戳格式， 最大行限制。分块等。

​	创建数据库，`POST`请向`/query`端点发送请求并将URL参数设置`q`为`CREATE DATABASE <new_database_name>`。下面的示例向运行的InfluxDB发送请求`localhost`并创建数据库`mydb`：

```shell
curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE mydb"
```

​	InfluxDB 同时支持多种编写数据：同时写入多个点， 从文件中写入等。

​	具体内容请参考官网[InfluxDB HTTP API 参考](https://docs.influxdata.com/influxdb/v1.6/tools/api/)。



#### 2. InfluxDB-python 操作

​	InfluxDB-Python是一个与[InfluxDB](https://influxdata.com/time-series-platform/influxdb/)交互的客户端。

​	要连接到InfluxDB，您必须创建一个 [`InfluxDBClient`](https://influxdb-python.readthedocs.io/en/latest/api-documentation.html#influxdb.InfluxDBClient)对象。默认配置`localhost`使用默认端口连接到InfluxDB。

```
from influxdb import InfluxDBClient

# using Http
client = InfluxDBClient(database='dbname')
client = InfluxDBClient(host='127.0.0.1', port=8086, database='dbname')
client = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database='dbname')
```

​	要编写pandas DataFrames或将数据读入pandas DataFrame，请使用[`DataFrameClient`](https://influxdb-python.readthedocs.io/en/latest/api-documentation.html#influxdb.DataFrameClient)对象。这些客户端的启动方式与 [`InfluxDBClient`](https://influxdb-python.readthedocs.io/en/latest/api-documentation.html#influxdb.InfluxDBClient)：

```
from influxdb import DataFrameClient

client = DataFrameClient(host='127.0.0.1', port=8086, username='root', password='root', database='dbname')
```

​	以下是使用InfluxDB-python案例：

```
user = 'root'
password = 'root'
dbname = 'example'
dbuser = 'smly'
dbuser_password = 'my_secret_password'
query = 'select value from cpu_load_short;'
json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "Float_value": 0.64,
            "Int_value": 3,
            "String_value": "Text",
            "Bool_value": True
        }
    }
]

client = InfluxDBClient(host, port, user, password, dbname)

print("创建数据库: " + dbname)
client.create_database(dbname)

print("创建保留策略")
client.create_retention_policy('awesome_policy', '3d', 3, default=True)

print("切换用户: " + dbuser)
client.switch_user(dbuser, dbuser_password)
print("写入: {0}".format(json_body))
client.write_points(json_body)

print("查询数据: " + query)
result = client.query(query)
print("Result: {0}".format(result))

print("切换用户: " + user)
client.switch_user(user, password)

print("删除数据库: " + dbname)
client.drop_database(dbname)
```

​	由此看出InfluxDB 操作简单。易于学习。 	并且InfluxDB支持R， Ruby， Java， Javascripy/node.js，MATLAB，Perl，PHP等多种主流语言。详情请参考[InfluxDB API客户端库](https://docs.influxdata.com/influxdb/v1.6/tools/api_client_libraries/)。

#### 3. InfluxDB命令行操作（CLI/shell）

​	InfluxDB的命令行界面（`influx`）是HTTP API的交互式shell。使用`influx`写在不同格式的数据（手动或从文件中），交互查询数据，和视图查询输出。

​	要访问CLI，首先启动`influxd`数据库进程，然后`influx`在终端中启动。进入shell并成功连接到InfluxDB节点。并且`influx`启动时可以传递几个参数：

```
-compressed 如果导入文件已压缩，则设置为true。使用-import。

-consistency 'any|one|quorum|all' 设置写入一致性级别。

-database 'database name'influx连接 的数据库。

-execute 'command' 执行InfluxQL命令并退出
```

此文档只列出一部分， 详情请参考[InfluxDB的命令行操作](https://docs.influxdata.com/influxdb/v1.6/tools/shell/#influx-arguments)。

# 总结

​	InfluxDB在单个节点上速度**非常快**，并且具有许多非常多的功能和高效的存储空间。InfluxDB使用一种易于入门的SQL样式查询语言。查询语法简单，功能强。后端时序数据操作、写入块。

​	简化的**冲突解决方案**可提高写入性能。无法存储重复数据; 可能会在极少数情况下覆盖数据。

​	限制对**删除**的访问可以提高查询和写入性能。删除功能受到严重限制。

​	限制对**更新**的访问可以提高查询和写入性能。更新功能受到严重限制。

​	绝大多数写入**用于具有最新时间戳**的数据，并且数据按时间升序添加。按时间升序添加数据的性能要高得多。

​	规模至关重要。该数据库必须能够处理**大容量的读取和写入**。可以处理**大容量的读取和写入**。如果数据库负载很重，查询返回可能不包括最新的点。

​	能够编写和查询数据比拥有强一致的视图。编写和查询数据库可以由多个客户端在高负载下完成。

​	许多时间序列都是**短暂的**。通常情况下，时间序列只出现几个小时然后消失。InfluxDB擅长管理**不连续数据**。无架构设计意味着不支持某些数据库功能，例如没有交叉表连接。

​	InfluxDB有非常强大的工具来处理**聚合数据**和**大数据集**。点没有传统意义上的ID，它们按时间戳和系列区分。

**大规模的可扩展性和性能：**有效的时间序列数据库使应用程序可以轻松扩展，以便在连续流中支持数**百万个物联网设备**或**时间序列数据点**，并执行实时分析。

**减少停机时间：**在停机时间不可接受的情况下，为时间序列数据构建的数据库体系结构可确保即使在**网络分区或硬件故障**时数据始终可用。

**降低成本：**

1. **资源成本：**高弹性转化为管理中断所需的资源更少。使用商用硬件快速轻松地进行扩展可降低扩展或缩小的操作和硬件成本。
2. **学习成本：** InfluxDB中InfluxQL是一种类SQL的语言。对于来自其他SQL或类SQL环境的用户来说，它已经被精心设计，而且还提供特定于存储和分析时间序列数据的功能。将学习使用成本极度降低。

**改进的业务决策：**通过使组织能够实时分析数据，时间序列数据库可帮助组织**更快，更准确地调整**能耗，设备维护，基础架构变更或影响业务的其他重要决策。

# 运行参数

InfluxDB的单节点是完全开源的，InfluxDB的集群版本是闭源的商业版。单节点的实例没有冗余，如果服务不可用，写入和读取数据都会马上失败。

InfluxDB的集群提供了高可用和冗余，多个数据副本分布多态服务器上，任何一台服务器的丢失都不会对集群造成重大的影响。

> 负载：基于每秒的写入的数据量、每秒查询的次数以及唯一series的数目。基于你的负载，我们给出CPU、内存以及IOPS。
>
> 官方建议：InfluxDB应该泡在SSD上， 任何其他存储配置将具有较低的性能特征，并且在正常处理中可能设置无法从小的中断中恢复。

## 单节点

| 负载   | 每秒写入的字段数 | 每秒中等查询数 | series数量 |
| ------ | ---------------- | -------------- | ---------- |
| 低     | < 5千            | <5             | <10万      |
| 中等   | <25万            | <25            | <1百万     |
| 高     | >25万            | >25            | >1百万     |
| 相当高 | >75万            | >100           | >1千万     |

> 说明：查询对于系统性能的影响很大
> 简单查询：
>
> - 几乎没有函数和正则表达式
> - 时间限制在几分钟，或是几个小时，又或者到一天
> - 通常在几毫秒到几十毫秒内执行
>
> 中等查询：
>
> - 有多个函数或者一两个正则表达式
> - 有复杂点的`GROUP BY`语句或是时间有几个星期的数据
> - 通常在几百毫秒到几千毫秒内执行
>
> 复杂查询：
>
> - 有多个聚合函数、转换函数或者多个正则表达式
> - 时间跨度很大有几个月或是几年
> - 通常执行时间需要几秒
> - 通常执行时间需要几秒

### 低负载推荐

- CPU：2~4核
- 内存：2~4GB
- IOPS：500

### 中等负载推荐

- CPU：4~6核
- 内存：8~32GB
- IOPS：500~1000

### 高负载推荐

- CPU：8+核
- 内存：32+GB
- IOPS：1000+

### 超高负载

要达到这个范围挑战很大，单节点无法完成。

## 集群

### 元节点

集群至少要有三个独立的元节点才能允许一个节点的丢失，如果要容忍`n`个节点的丢失则需要`2n+1`个元节点。集群的元节点的数目应该为奇数。不要是偶数元节点，因为这样在特定的配置下会导致故障。

元节点不需要多大的计算压力，忽略掉集群的负载，我们建议元节点的配置：

- CPU:1~2核
- 内存：512MB~1GB
- IOPS：50

### 数据节点

一个集群运行只有一个数据节点，但这样数据就没有冗余了。这里的冗余通过写数据的RP中的`副本个数`来设置。一个集群在丢失`n-1`个数据节点后仍然能返回完整的数据，其中`n`是副本个数。为了在集群内实现最佳数据分配，我们建议数据节点的个数为偶数。

对于集群的数据节点硬件的推荐和单节点的类似，数据节点应该至少有两个核的CPU，因为必须处理正常的读取和写入压力，以及集群内的数据的读写。由于集群通信开销，集群中的数据节点处理的吞吐量比同一硬件配置上的单实例的要少。

| 负载   | 每秒写入的字段数 | 每秒中等查询数 | series数量 |
| ------ | ---------------- | -------------- | ---------- |
| 低     | < 5千            | <5             | <10万      |
| 中等   | <10万            | <25            | <1百万     |
| 高     | >10万            | >25            | >1百万     |
| 相当高 | >50万            | >100           | >1千万     |

> 说明：查询对于系统性能的影响很大
> 简单查询：
>
> - 几乎没有函数和正则表达式
> - 时间限制在几分钟，或是几个小时，又或者到一天
> - 通常在几毫秒到几十毫秒内执行
>
> 中等查询：
>
> - 有多个函数或者一两个正则表达式
> - 有复杂点的`GROUP BY`语句或是时间有几个星期的数据
> - 通常在几百毫秒到几千毫秒内执行
>
> 复杂查询：
>
> - 有多个聚合函数、转换函数或者多个正则表达式
> - 时间跨度很大有几个月或是几年
> - 通常执行时间需要几秒

### 低负载推荐

- CPU：2~4核
- 内存：2~4GB
- IOPS：1000

### 中等负载推荐

- CPU：4~6核
- 内存：8~32GB
- IOPS：1000+

### 高负载推荐

- CPU：8+核
- 内存：32+GB
- IOPS：1000+

### 企业Web节点

企业Web服务器主要充当具有类似负载要求的HTTP服务器。 对于大多数应用程序，它不需要性能很强。 一般集群将仅使用一个Web服务器，但是考虑到冗余，可以将多个Web服务器连接到单个后端Postgres数据库。

> 注意：生产集群不应该使用SQLite数据库，因为它不被冗余的Web服务器允许，也不能像Postgres一样处理高负载。

推荐配置：

- CPU：1~4核
- 内存：1~2GB
- IOPS：50

> 企业Web节点是给集群提供一个**交互**中转。是于InfluxDB数据操作独立的处理模块。

## 内存

影响内存的最主要的因素是series基数，series的基数大约或是超过千万时，就算有更多的内存也可能导致OOM，所以在设计数据的格式的时候需要考虑到这一点。

内存的增长和series的基数存在一个指数级的关系。

## 磁盘

InfluxDB被设计运行在SSD上，InfluxData团队不会在HDD和网络存储上测试InfluxDB，所以不太建议在生产上这么去使用。在机械磁盘上性能会下降一个数量级甚至在中等负载下系统都可能死掉。为了最好的结果，InfluxDB至少需要磁盘提供1000 IOPS的性能。

> 注意集群的数据节点在做故障恢复的时候需要更高的IOPS，所以考虑到可能的数据恢复，我们建议磁盘至少有2000的IOPS，低于1000的IOPS，集群可能无法即时从短暂的中断中恢复。

### 存储空间

数据库的名字、measurement、tag keys、field keys和tag values只被存储一次且只能是字符串。只有field values和timestamp在每个数据点上都有存储。

非字符串类型的值大约需要3字节，字符串类型的值需要的空间由字符串的压缩来决定。



## 实际测试使用

| 写入的数据量 | series数量 | 时间             |
| ------------ | ---------- | ---------------- |
| 10000（条）  | 42（列）   | 2.638164（秒）   |
| 1000（条）   | 42（列）   | 0.31367850（秒） |

写入稳定，花费时间稳定。



