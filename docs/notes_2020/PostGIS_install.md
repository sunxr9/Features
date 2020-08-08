# PostGIS 安装文档

PostGIS 数据库安装文档，PostGIS 为 PostgreSQL 扩展，增加空间地理数据支持。



## 环境

本次安装系统为 Ubuntu 18.04 Server。



## PostgreSQL 

PostgreSQL 可直接通过 `APT` 存储库安装。本次安装为 PostgreSQL 11 版本。

### 安装

+ 安装工具
```bash
sudo apt-get install curl ca-certificates gnupg
```

+ 获存储库密钥并添加

```bash
curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

+ 添加存储库地址信息，`$(lsb_release -cs)` 命令获取当前系统实际发行版。

```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

+ 更新软件包列表，安装PostgreSQL。如需指定版本，自行替换 `postgresql-11` 中的 11 。

```
sudo apt-get update
sudo apt-get install postgresql-11 pgadmin4
```

### 配置远程登录

+ 修改 `postgresql.cong` 文件中监听地址`listen_addresses`信息，使用PostgreSQL 接受任意IP的连接。该文件存放于`/etc/postgresql/11/main/`目录下。

  ```
  listen_addresses = '*'
  ```

+ 修改`pg_hba.conf` 文件，添加服务端认证模式，该文件与`postgresql.conf` 文件处于同级目录。编辑该文件，增加以下内容：

  ```
  # TYPE  DATABASE  USER  CIDR-ADDRESS  METHOD
  host  	all  	  all 	 0.0.0.0/0 		md5
  ```

  完成后执行 `sudo service postgresql restart` 重启PostgreSQL 数据库，即可尝试远程连接。

## PostGIS 安装

使用 `apt `命令安装 Postgis。

+ 添加存储库并更新软件列表

  ```bash
  sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable | sudo apt update
  ```

+ 安装 PostGIS

  ```bash
  sudo apt install postgis postgresql-11-postgis-3
  ```

  此步骤容易出现依赖缺失，推荐使用 `sudo apt install -f ` 命令自动安装，部分需手动进行安装。 

  安装过程中遭遇依赖缺失为：`libxml2-dev`、`geos-config`、`libgdal20`，其中`libgdal20` 模块依赖于 `gdal-data` ，需要手动安装。进入gdal-data [下载页面](https://answers.launchpad.net/ubuntu/bionic/amd64/gdal-data/2.2.3+dfsg-2)获取deb 包，使用 `sudo dpkg -i [deb package name] ` 命令进行安装。

+ 创建 PostGIS 扩展

  使用 su 命令切换至 PostgreSQL 数据库默认用户，执行 `psql` 命令进入数据库命令行进行创建 PostGIS 扩展。

  ```sql
  # 创建扩展件
  CREATE EXTENSION postgis;
  # 启用栅格支持
  CREATE EXTENSION postgis_raster;
  # 启用拓扑
  CREATE EXTENSION postgis_topology;
  # 启用并非在所有发行版中都可用的PostGIS Advanced 3D和其他地理处理算法sfcgal
  CREATE EXTENSION postgis_sfcgal;
  # Tiger所需的模糊匹配
  CREATE EXTENSION fuzzystrmatch;
  # 基于规则的标准化者
  CREATE EXTENSION address_standardizer;
  # 规则数据集示例
  CREATE EXTENSION address_standardizer_data_us;
  # 启用美国Tiger Geocoder
  CREATE EXTENSION postgis_tiger_geocoder;
  ```

+ 验证 PostGIS，使用SQL 语句查询PostGIS 插件版本
  
  ```b
  SELECT PostGIS_version();
  ```
  
  输出以下结果：
  
  ```
              postgis_version            
  ---------------------------------------
   3.0 USE_GEOS=1 USE_PROJ=1 USE_STATS=1
  (1 row)
  ```
  
  

