## Thingsboard

### Thingsboard 使用docker镜像安装

1. 安装Docker

2. 安装Docker Compose（linux）

   运行此命令以下载最新版本的Docker Compose：

   > ```
   > sudo curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   > ```

   对二进制文件应用可执行权限：

   > ```
   > sudo chmod +x /usr/local/bin/docker-compose
   > ```

   测试安装

   > ```
   > $ docker-compose --version
   > docker-compose version 1.22.0, build 1719ceb
   > ```

3. 创建一个文件夹来存储docker文件：

   > mkdir <docker-folder>
   >
   > cd docker-folder

4. 从thingsboard repo下载一下文件

   1. **docker-compose.yml** - 主 **docker** -compose文件。
   2. **.env** - 包含cassandra数据文件夹和cassandra架构的默认位置的主env文件。
   3. **tb.env** - 默认的thingboard环境变量。

   > ```
   > curl -L https://raw.githubusercontent.com/thingsboard/thingsboard/release-2.0/docker/docker-compose.yml > docker-compose.yml
   > curl -L https://raw.githubusercontent.com/thingsboard/thingsboard/release-2.0/docker/.env > .env
   > curl -L https://raw.githubusercontent.com/thingsboard/thingsboard/release-2.0/docker/tb.env > tb.env
   > ```

5. 创建系统和演示数据并启动ThingsBoard节点执行next命令

   > ```
   > ADD_SCHEMA_AND_SYSTEM_DATA=true ADD_DEMO_DATA=true bash -c 'docker-compose up -d tb'
   > ```

   安装过程中可能会出现以下错误，请作参考

   **Install Error：**

   > open /var/lib/docker/tmp/GetImageBlob957423011：no such file or directory

   **Answer：**

   > sudo service docker stop
   >
   > sudo service docker start

   执行完毕之后再次执行`ADD_SCHEMA_AND_SYSTEM_DATA=true ADD_DEMO_DATA=true bash -c 'docker-compose up -d tb'`命令，出现error

   **Install error**

   > Conldn't connect to docker daemon at http+docker://localhost - is it running?
   >
   > 该错误的出现是因为没有将当前用户加入到docker组

   **Answer：**

   > 将当前用户加入docker组
   >
   > sudo gpasswd -a <user> docker 
   >
   > 出现 `Adding user <user> to group docker`代码提示
   >
   > 然后退出当前用户比如切换为root 在此切换为当前用户
   >
   > $ sudo su 
   >
   > $ su <user>

   解决完毕之后在此执行``ADD_SCHEMA_AND_SYSTEM_DATA=true ADD_DEMO_DATA=true bash -c 'docker-compose up -d tb`

6. 使用Docker镜像启动

   > docker run thingsboard/application

   **Error**

   > Unable to find image 'thingsboard/application:latest' locally

   **Answer:**

   > docker pull thingsboard/application

   之后再执行`docker run thingsboard/application`

* 

* | 用户名                   | 密码     |
  | ------------------------ | -------- |
  | sysadmin@thingsboard.org | sysadmin |

在租户添加下面账号

- Username: **tenant@thingsboard.org**
- Password: **tenant**

### Thingsboard 端口冲突

查看Thingsboard运行状态

- docker命令查看运行状态

> docker ps -a 

- docker命令删除某一进程

> docker container rm <name>

docker 镜像启动（run）之后就不用再使用docker run 命令启动

### 使用deb文件安装`thingsboard`

- 更新到最新版本的套件

> sudo apt-get update
>
> sudo apt-get dist-upgrade
>
> sudo apt-get upgrad
>
> 我是会再多做一次重新开机sudo reboot

- 安装Oracle JDK

> sudo apt-get install default-jdk 
>
> sudo add-apt-repository ppa:webupd8team/java
>
> sudo apt-get update
>
> sudo apt-get install oracle-java8-installer 

安装完成之后 修改环境变量

> sudo update-alternatives –config java
>
> sudo nano /etc/environment

增加一行`JAVA_HOME="/usr/lib/jvm/java-8-oracle" `

执行

> source /etc/environment 

检查一下是否有设定正确

> echo $JAVA_HOME 

- 安装Thingsboard

> cd 到一个路径下
>
> wget < https://github.com/thingsboard/thingsboard/releases/download/v2.1/thingsboard-2.1.deb>
>
> sudo dpkg -i thingsboard-2.1.deb
>
> sudo /usr/share/thingsboard/bin/install/ install.sh –loadDemo
>
> sudo service thingsboard start 开启服务
>
> sudo service thingsboard stop 停止服务
>
> sudo service thingsboard restart  重启服务

（备注：执行deb文件的时候 要在deb文件所在的路径下执行）

到这里为止，`Thingsboard`就安装完成了，打开浏览器输入`http://localhost：8080`就可以进入到Thingsboard的登录页面。

系统管理员默认帐号－－登录ID和PWD分别是：sysadmin@thingsboard.org和sysadmin

租户管理员－－登录ID和pwd分别是：**tenant@thingsboard.org**和**tenant**。

登陆成功之后显示全英文，可以在右上角`竖三点`按钮中选择`profile`选择合适语言。

### 超级管理员（tenant）、租户和用户之间的关系

超级管理员下面多个租户（CUSTOMERS），可以对每个租户进行管理，每一个租户可以可以创建多个用户。

超级管理员和用户的登录成功之后显示功能选项不同。

### 创建租户

- 在左侧菜单栏点击`CUSTOMERS`按钮，显示该管理员下的所有租户；
- 右下角点击`红底白色+号`按钮（create new customer），弹出窗口，填写租户信息；
- 点击`ADD`添加完成。

### 创建用户

创建用户必须通过某个租户，属于上下级关系。

- 点击租户信息页面`Manager Customer user`按钮，显示该租户下面所有用户，点击右下方`红底白色加号`按钮；
- 填写`Add User`信息，选择激活方法。推荐选择`显示激活链接`,`ADD`添加；
- 使用激活链接在网页设置登录密码、确认登录密码；
- 使用邮箱地址和登录密码登录。

### Paho-mqtt 发送数据至本地Thingsboard

- 安装pip、paho-mqtt 

> 在python环境下安装pip
>
> 安装完成安装paho-mqtt 
>
> pip install paho-mqtt 

安装完成使用python运行py文件

运行脚本上传至gitlab `http://106.15.198.200/wangshaosong/Thingsboard.git`

### Thingsboard与PostgreSQL数据库（Ubuntu）

- 安装PostgreSQL

> ```
> sudo apt-get update
> sudo apt-get install postgresql postgresql-contrib
> sudo service postgresql start
> ```

### 使用MQTT（Mosquitto）协议传输数据至Thingsboard

> 安装mosquitto客户端
>
> sudo apt-get install mosquitto -clients

## Postgresql数据库

#### Ubuntu

##### 服务启动、停止和重启命令

> /etc/init.d/postgresql start|stop|restart

##### 安装

> sudo apt-get install postgresql

##### 卸载

* 删除相关的安装

> sudo apt-get --purge remove postgresql\* 

* 删除配置及相关文件

> sudo rm -r /etc/postgresql/ 
>
> sudo rm -r /etc/postgresql-common/ 
>
> sudo rm -r /var/lib/postgresql/ 

* 删除用户所在组

> sudo userdel -r postgres 
>
> sudo groupdel postgres 

##### 修改Postgresql数据库默认用户Postgres密码

安装完成Postgresql数据库成功是，会默认创建一个postgres用户，作为数据库的管理员，密码是随机的，所以需要修改密码。

* 登录Postgresql

> sudo -u postgres psql

* 修改登录PostgreSQL密码 

> ALTER USER postgres WITH PASSWORD '';

**注意：**

* 密码要用引号引起来
* 命令最后有分号

##### 添加用户

##### 常用数据类型

数值型

* integer（int）
* real
* serial

文字型

* varchar
* char
* text

布尔型

* Boolean

日期型

* data
* datetime
* timestamp

##### 创建表的约束条件

* not null：不能为空
* unique： 在所有数据中至必须为一
* check：字段设置条件
* default：字段默认值
* primary 可以（not null，unique）：主键，不能为空，且不能重复

> create table posts(
>
> ​	id serial primary key,
>
> ​	title varchar(255) not null,
>
> ​	content test check(length(content) > 8),   #content长度必须大于8个长度
>
> ​	is_draft boolean default TRUE,
>
> ​	create_data timestamp default 'now'
>
> )

##### 查询

查询语句和一般sql语句大同小异

where：

> select * from table;
>
> select * from table where 条件;
>
> select * from table where 条件1 and 条件2;
>
> select * from table where 条件1 or 条件2;

order by、limit、offset

> select *from users order by score asc;# 按照成绩升序
>
> select *from users order by score desc;# 按照成绩降序
>
> select *from users order by team, score;# 按照对和成绩升序排序
>
> select *from users order by team, score desc;# 按照对升序，成绩降序排序；
>
> select *from users order by team desc, score desc;# 按照球队降序、成绩降序；
>
> select *from users order by score desc limit 3;# 成绩降序排列 取前三
>
> select *from users order by score desc limit 3 offset 2;# 成绩降序排列 从第三名开始取 取前三名；默认offset为0

##### 数据库备份与恢复（Ubuntu）

###### 备份

* 进入**bin**目录，执行以下命令

> sudo pg_dump -h **ip** -U **user**-d **databasename** -f **filename.sql**

###### 恢复

* 进入**bin**目录，执行以下命令

> psql -h **ip** -U **user**-d **databasename** > **filename.sql** 

ip：需要访问的ip地址

user：登录postgresql数据库的用户

databasename：需要备份的数据库名称

filename.sql：文件名

执行以上命令在该目录生成以filename.sql文件

**备注：**

* 命令中加粗字体为修改部分，需根据实时修改。
* 恢复数据库数据需要提前创建要恢复的空数据库。
* 若远程数据需要，必须保证数据库允许外部访问。

### Windows

##### 安装

官网下载postgresql数据库安装包，下载exe文件，双击安装！

* 选择安装目录
* 选择数据存放目录
* 填写postgres用户的密码。

下载链接：**https://www.enterprisedb.com/downloads/postgres-postgresql-downloads**

##### 使用

postgresql数据库安装完成后，会带有相对应的工具。其中**SQL shell（psql）**，提供命令操作。

![1545379299710](.\assets\1545379299710.png)

##### 添加环境变量

在环境变量**path**中添加postgresql安装目录中**bin**文件目录（为了可以直接在cmd窗口中使用命令行操作）

* 登录  

> psql -U postgres 

![1545379601955](.\assets\1545379601955.png)

使用postgres用户登录，输入postgres密码。（安装过程中设置的postgres超级用户的密码）

##### 常用命令

* 查看当前用户下有多少数据库

> \l

* 创建数据库

> create database databasename 

* 进入数据库

> \c databasename 

## Bokeh

### bokeh实现x轴y轴百分数刻度

> from bokeh.models import NumeralTickFormatter
>
> p.yaxis[0].formatter = NumeralTickFormatter(format="0.0%")
>
> p.xaxis[0].formatter = NumeralTickFormatter(format="0.0%")

### bokeh 设置次要线

> p.ygrid.minor_grid_line_color = 'navy'  #  颜色
> p.ygrid.minor_grid_line_alpha = 0.1  # 透明度

### bokeh 添加图片（logo）

- 图片（logo）随着拖拽移动

> ```
> from bokeh.models.glyphs import ImageURL
> from bokeh.models import ColumnDataSource
> from bokeh.plotting import figure, show
> import numpy as np
> 
> logo_source = ColumnDataSource(dict(url=["http://bokeh.pydata.org/en/latest/_static/images/logo.png"]))
> x = np.random.normal(loc=5000.0, size=400)
> y = np.random.normal(loc=5000.0, size=400)
> 
> # This works
> logo_image  = ImageURL(url="url", x=5000, y=5000, w=50, h=50, w_units='screen', h_units='screen', global_alpha=0.2, )
> # This does not work. Not possible to set x_units='screen'
> #logo_image  = ImageURL(url="url", x=5000, y=5000, w=50, h=50, w_units='screen', h_units='screen', global_alpha=0.2, x_units='screen', y_units='screen' )
> 
> p = figure(plot_width=600, plot_height=600)
> p.scatter(x,y)
> p.add_glyph(logo_source, logo_image)
> show(p)
> ```

- 图片（logo）随着拖拽不移动‘

> ```
> from bokeh.plotting import figure, show
> from bokeh.models import Range1d, ImageURL
> 
> url = "http://bokeh.pydata.org/en/latest/_static/images/logo.png"
> 
> width = 600 
> height = 400 
> 
> p = figure(plot_width=width, plot_height=height)
> p.scatter([1, 2, 3], [4, 5, 6], size=10)
> 
> img = p.image_url(url=dict(value=url), x=width-50, y=50, w=50, h=50, w_units='screen', h_units='screen', global_alpha=0.5)
> 
> p.extra_x_ranges["x_screen"] = Range1d(0, width, bounds="auto")
> p.extra_y_ranges["y_screen"] = Range1d(0, height, bounds="auto")
> 
> img.x_range_name = "x_screen"
> img.y_range_name = "y_screen"
> 
> show(p)
> ```



## 爬虫

### 爬虫 Requests

* headers请求头、代理IP

> headers = {
>
> "User-Agent":"",
>
> }
>
> proxies = { 
>
> "https":"122.72.32.75:80" 
>
> }
>
> 第一步：response = request.get(url,headers=headers,proxies = proexis)   # 伪造请求头和代理IP，这个得到是一个响应
>
> 第二步：response.encoding("XXX")改变响应的编码（根据网页编码格式）
>
> 通过text打印响应中的数据

* get 、post带参数

> 



## Ubuntu操作命令

### 有关查看硬盘使用情况的命令

* 查看硬盘分区

> sudo fdisk -l

* 查看硬盘所使用大小比例

> df -hl



### Ubuntu安装Google浏览器

> sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
>
> sudo dpkg -i google-chrome-stable_current_amd64.deb

若缺少依赖关系

> sudo agt-get -f install 

### 实现Windows和Ubuntu相互粘贴复制

> 第一步： sudo apt-get autoremove open-vm-tools 
>
>  第二步：sudo apt-get install open-vm-tools-desktop  
>
> 然后重启  

### 安装Ubuntu常见问题

* E: 无法获得锁 /var/lib/dpkg/lock - open (11: 资源暂时不可用) E: 无法锁定管理目录(/var/lib/dpkg/)，是否有其他进程正占用它？

  强制解锁

  > 命令:sudo rm /var/lib/dpkg/lock

## 各种库的安装

### 安装nodejs（Ubuntu）

> sudo apt install nodejs-legacy

### 安装npm（Ubuntu）

> sudo apt install npm

### 安装MQTT协议

> sudo npm install mqtt -g

## Sqlit数据库

### 创建连接数据库、插入数据、查找数据

>import sqlite3
>
>创建并连接数据库
>
>conn = sqlite3.connect('test.db')
>cursor = conn.cursor()
>
>创建表格
>
>cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
>cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
>
>查看插入数据条数
>
>cursor.rowcount
>
>查找
>cursor.execute('select * from user ')
>values = cursor.fetchall()
>
>values
>[('1', 'Michael'), ('2', 'Michael2')]
>
>cursor.close()
>conn.close()

### 创建表

> ```
> conn = sqlite3.connect('cable_test.db')
> cursor = conn.cursor()
> cursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + " (id INTEGER PRIMARY KEY AUTOINCREMENT, year VARCHAR(20) NOT NULL,week VARCHAR(20) NOT NULL," \
>                                                  "place VARCHAR(20) NOT NULL,pro VARCHAR(20) NOT NULL,data INTEGER(20))")
> cursor.close()
> conn.commit()
> conn.close()
> print("创建表格成功")
> ```

### 插入数据

> ```
> conn = sqlite3.connect(d_bases)
> cursor = conn.cursor()
> cursor.execute("INSERT INTO " + table + " (year,week,place,pro,data) VALUES ('%s', '%s','%s','%s', '%s')" % ('2018', week_num, column, pro, df.loc[week_num][column]))
> cursor.close()
> conn.commit()
> conn.close()          
> ```

`备注：一定要提交事务。`

### 查看数据

> ```
> conn = sqlite3.connect(d_bases)
> # 创建一个Cursor:
> cursor = conn.cursor()
> cursor.execute("select * from " + table)
> cursor.execute("select * from " + table + " where place=? and week=?",(place, "第" + str(week) + "周"))
> values = cursor.fetchall()
> print(values)
> print(len(values))
> cursor.close()
> conn.close()
> ```

### 更新数据

> ```
> conn = sqlite3.connect("cable_test.db")
> cursor = conn.cursor()
> oee_date = 0.6666777888999
> pro = "CL"
> place = "wuhan"
> week = 10
> year = 2018
> cursor.execute("update table1 set data=?" + " where year=? and pro=? and place=? and week=?",(year,oee_date ,pro, place, "第"+str(week) +"周"))
> cursor.close()
> conn.commit()
> conn.close()
> ```

### 删除数据

> ```
> conn = sqlite3.connect("cable_test.db")
> cursor = conn.cursor()
> week = "第49周"
> cursor.execute("""DELETE FROM table WHERE week = "第43周" """)
> cursor.close()
> conn.commit()
> conn.close()
> print("已经删除")
> return
> ```

### 删除表

> ```
> conn = sqlite3.connect("cable_test.db")
> # 创建一个Cursor:
> cursor = conn.cursor()
> print(cursor.execute("SELECT name FROM sqlite_master  WHERE type = 'table' ORDER BY name").fetchall())
> cursor.close()
> conn.close()
> ```

## Matplotlib

Matplotlib 是一个 Python 的 2D绘图库，它以各种硬拷贝格式和跨平台的交互式环境生成出版质量级别的图形。

### matplotlib中文乱码问题

> * 下载**simhei.ttf**文件
>
> * 将文件**simhei.ttf**文件拷贝到路径lib/python2.7/site-packages/matplotlib/mpl-data/fonts/ttf 目录下
>
> * 删除~/.cache/matplotlib的缓冲目录 
>
> * 修改配置文件 ：
>
>   找到如下两项，去掉前面的#，并在font.sans-serif冒号后面加上SimHei。 
>
>   font.family         : sans-serif        
>   font.sans-serif     : SimHei, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif     
>
>   找到axes.unicode_minus，将True改为False。
>
>   保持退出。
>
> * 文件中添加代码：
>
>   from pylab import * 
>   mpl.rcParams['font.sans-serif'] = ['SimHei']

### 背景

#### 背景网格设置

> plt.grid(**color**='red',**linestyle**='--')

### X轴

#### x轴字体刻度大小

plt.xticks(fontsize=13)

#### 设置x轴刻度倾斜

> plt.setp(ax.get_xticklabels(), **rotation**=45, **horizontalalignment**='right')

**rotation：**倾斜度

**horizontalalignment：**偏向右、偏向左

### Y轴

#### y轴字体刻度大小

> plt.xticks(fontsize=13)

#### 自定义y轴取值范围

> plt.ylim(0.4, 0.9)

### 折线图

> ax.plot(index_ls,y)

### 圆点图

> ax.scatter(index_ls,y,color = "red",s=60,alpha = 0.8)

### 柱状图

ax.bar(index_ls,y,width = 0.3)

参数列表

- x
  包含所有柱子的下标的列表
- height
  包含所有柱子的高度值的列表
- width
  每个柱子的宽度。可以指定一个固定值，那么所有的柱子都是一样的宽。或者设置一个列表，这样可以分别对每个柱子设定不同的宽度。
- align
  柱子对齐方式，有两个可选值：`center`和`edge`。`center`表示每根柱子是根据下标来对齐, `edge`则表示每根柱子全部以下标为起点，然后显示到下标的右边。如果不指定该参数，默认值是`center`。

- color
  每根柱子呈现的颜色。同样可指定一个颜色值，让所有柱子呈现同样颜色；或者指定带有不同颜色的列表，让不同柱子显示不同颜色。
- edgecolor
  每根柱子边框的颜色。同样可指定一个颜色值，让所有柱子边框呈现同样颜色；或者指定带有不同颜色的列表，让不同柱子的边框显示不同颜色。
- linewidth
  每根柱子的边框宽度。如果没有设置该参数，将使用默认宽度，默认是没有边框。
- tick_label
  每根柱子上显示的标签，默认是没有内容。
- xerr
  每根柱子顶部在横轴方向的线段。如果指定一个固定值，所有柱子的线段将一直长；如果指定一个带有不同长度值的列表，那么柱子顶部的线段将呈现不同长度。
- yerr
  每根柱子顶端在纵轴方向的线段。如果指定一个固定值，所有柱子的线段将一直长；如果指定一个带有不同长度值的列表，那么柱子顶部的线段将呈现不同长度。
- ecolor
  设置 xerr 和 yerr 的线段的颜色。同样可以指定一个固定值或者一个列表。
- capsize
  这个参数很有趣, 对`xerr`或者`yerr`的补充说明。一般为其设置一个整数，例如 10。如果你已经设置了
  yerr 参数，那么设置 capsize 参数，会在每跟柱子顶部线段上面的首尾部分增加两条垂直原来线段的线段。对 xerr 参数也是同样道理。可能看说明会觉得绕，如果你看下图就一目了然了。

- error_kw
  设置 xerr 和 yerr 参数显示线段的参数，它是个字典类型。如果你在该参数中又重新定义了 ecolor 和 capsize，那么显示效果以这个为准。
- orientation
  设置柱子是显示方式。设置值为 vertical ，那么显示为柱形图。如果设置为 horizontal 条形图。不过 matplotlib 官网不建议直接使用这个来绘制条形图，使用`barh`来绘制条形图。

### 分组柱状图(bar)

案例

>ind = np.arange(len(y)) 
>
>width = 0.2 
>
>fig, ax = plt.subplots(figsize=(12,4))
>
>rects1 = ax.bar(** ind - width/2, y1, width,color='SkyBlue', label='WH_CL')
>
>rects2 = ax.bar(ind + width/2, y2, width,color='IndianRed', label='WH_SC')
>
>ax.set_xticks(ind)
>
>ax.set_xticklabels(df_CL.index[0:10])
>
>plt.show()

![1544515229423](.\assets\1544515229423.png)



### 堆叠柱状图(bar)

添加属性**bottom，**设置第二个柱状图的y轴的起始位置。

> rects1 = ax.bar(ind, y1, width,color='SkyBlue', label='WH_CL')
>
> rects2 = ax.bar(ind, y2, width,color='IndianRed', label='WH_SC',**bottom=y1**)

![1544516416424](.\assets\1544516416424.png)

### 横向柱状图(barh)

> fig, ax = plt.subplots()
>
> index_ls = df_CL.index[0:10]
>
> ax.**barh**(index_ls,y,height = 0.3,color = "SkyBlue")
>
> plt.xticks(fontsize=12)
>
> plt.yticks(fontsize=12)
>
> plt.title('Scores by group and gender',fontsize = 20 )
>
> plt.show()

![1544517345109](.\assets\1544517345109.png)

## D3.js

### x轴生成

* 第一步：生成X轴比例尺

> var xScale = d3.scaleBand().domain(Xdatas).rangeRound([0, 1100])
>
> xScale：变量名
>
> domain(Xdatas)：Xdatas为一个列表，表示输域
>
> rangeRound([0, 1100]：表示x坐标轴的长度

* 第二步：在svg标签下添加group组

> var g = svg.append('g')
>             		.attr('transform', 'translate(33,40)');

* 第三步：添加x轴（同时添加x_lable）

> g.append('g')
> 		            .attr('class', 'axisX')
> 		            .attr('transform', 'translate(1,300)')
> 		            .call(d3.axisBottom(xScale))
> 		            .attr("font-size", '14px')
> 			     .append("text")
> 			     .attr("font-size", '16px')
> 		            .attr("text-anchor", "start")
> 		            .attr("y", 40)
> 		            .attr('x', "44.5%")
> 		            .attr('transform', "translateX(-50%)")
> 		            .attr('fill','red')
> 		            .text("时间（周数）");

### Y轴生成

- 第一步：生成y轴比例尺

	 var	yScale = d3.**scaleLinear**().domain([0, 1]).rangeRound([**height**, 0])
>
> xScale：变量名
>
> domain([0,1])：Xdatas为一个列表，表示输域
>
> rangeRound([300, 0])：表示x坐标轴的长度

- 第二步：在svg标签下添加group组

> var g = svg.append('g')
>             		.attr('transform', 'translate(33,40)');

- 第三步：添加x轴（同时添加x_lable）

> g.append('g')
> 		            .attr('class', 'axisY')
> 		            .call(d3.axisLeft(yScale).ticks(10))
> 		            .attr("font-size", '14px');

ticks():表示将y轴分为多少份

### 图标添加标题（title）

添加中文标题是在**svg**标签里面添加**text**

> title = d3.select('#bar svg').append('text')
>             .attr('x', width / 2)
>             .attr('y', 20)
>             .attr('font-size',20) #字体大小
>             .style('text-anchor', 'middle')
>             .text('2018年 武汉光缆生成oee指标（柱状图）');

### 绘制柱状图

* 第一步 ：创建存放矩形的容器

  > var chart = g.selectAll('bar')
  >             .data(data)
  >             .enter().append('g')

* 第二步：通过容器添加矩形元素（具有动画效果）

> chart.append('rect')
>             .attr('class', 'bar')
>             .attr('x', function (d) {
>                 return xScale(d.key);
>             })
>
> ​	//动画开始
>
> ​	 .attr("y", function (d) {
>    ​         var min = yScale.domain()[0];
>    ​         return yScale(min);
>    ​     })
>    ​     .attr("height", function (d) {
>    ​         return 0;
>    ​     })
>    ​     .transition()
>    ​     .delay(function (d, i) {
>    ​         return i * 200;
>    ​     })
>    ​     .duration(2000)
>    ​     .ease(d3.easeBounceIn)
>
> //            动画结束
>             .attr('y', function (d) {
>                 return yScale(d.value);
>             })
>             .attr('height', function (d) {
>             	console.log(yScale(d.value));
>                 return **height** - yScale(d.value);
>             })
>             .attr('width', xScale.bandwidth())
>             .attr("fill","steelblue");

**height**需要与 创建比例尺的**height**保持一致

### 绘制折线图

* 添加折线（同时选择折线类型）

> var line = d3.svg.line()
>             .x(function (d) {
>                 return xScale(d.x)
>             })
>             .y(function (d) {
>                 return yScale(d.y);
>             })

* 在group组中添加元素

> main.append('path')
>             .attr('class', 'line')
>             .attr('d', line(CL_data));

**main:**group组的类名

添加**path**标签，class为**line**

#### 在折线上添加点

> main.selectAll('circle')
>             .data(CL_data)
>             .enter()
>             .append('circle')
>             .attr('cx', function (d) {
>                 return xScale(d.x);
>             })
>             .attr('cy', function (d) {
>                 return yScale(d.y);
>             })
>             .attr('r', 4)
>             .attr('fill', function (d, i) {
>                 return getColor(i);
>             });

**注意：**

可视化出来的折线和点可能与x轴不在一个竖直的直线上

![1547630962094](./assets\1547630962094.png)

需要对线和点进行横向偏移

> .attr('transform', 'translate('+width/data1.length/2+',0)')
>
> width ：x轴的宽度
>
> data1.length：data1数据的长度（元素个数）





### 添加背景网格

#### x轴网格

> // 添加x轴上的背景网格
> function make_x_gridlines(){
> 		return d3.axisBottom(xScale)
> 			.ticks(10)
> }
> // add the X gridlines
> g.append("g")
> 	.attr("class", "grid")
> 	.attr("transform", "translate(1," + height + ")")
> 	.call(make_x_gridlines()
> 		.tickSize(-400)
> 		.tickFormat("")
> 		)

#### y轴网格





### 绘制饼图

饼图室友封闭的两条弧线组成的，所以，弧线的起始位置（startAngle）、弧线的结束位置（endAngle）和饼图的内外半径(innerRadius、outerRadius)。

