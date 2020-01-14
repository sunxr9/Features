人流量分析目标

黏性：访问频率，时间间隔

活跃：停留时间，次数

产出：订单，数量

天流量对比



热力图



##### 191203

GDAL 安装命令：

```bash
pip install GDAL==$(gdal-config --version | awk -F'[.]' '{print $1"."$2}') --global-option=build_ext --global-option="-I/usr/include/gdal"
```

需要使用apt 安装依赖：

```bash
sudo apt-get install libgdal-dev
```

测试依赖命令：

```bash
gdal-config --version
```

如输出版本号即为依赖存在，可使用安装命令．

对Python 包的依赖为 `numpy`.



##### 191210

ubuntu 终端翻墙

临时翻墙使用环境变量：``

##### 191219

192.168.3.119 postgres 数据库密码：sgds1234

虚拟机用户postgres 密码：sgds

安装PostGIS

+ 添加仓库

  ```bash
  sudo apt -y install gnupg2
  wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
  
  echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
  ```

+ 安装PostgreSQL

+ 安装PostGIS

  将其中的**11** 替换为当前安装的PostgreSQL 版本。

  ```bash
  sudo apt update
  sudo apt install postgis postgresql-11-postgis-2.5
  ```

+ 启动PostGIS

  1. 切换当前用户。

  ```bash
  sudo -i -u postgres
  ```

  2. 创建数据库

  ```bash
  createdb test_db -O postgres
  ```

  3. 连接数据库

  ```bash
  psql -d test_db
  ```

  4. 在 test_db 数据库中启用PostGIS

  ```
  test_db=# CREATE EXTENSION postgis;
  ```

  5. 验证PostGIS

  ```
  test_db=# SELECT PostGIS_version();
  ```

  输出：

  ```
              postgis_version            
  ---------------------------------------
   2.5 USE_GEOS=1 USE_PROJ=1 USE_STATS=1
  (1 row)
  ```

  

##### 20191227

Notebook share 更名为　NBP(Notebook Public)



bokeh 连线样式

line_dash='dashed' 虚线

