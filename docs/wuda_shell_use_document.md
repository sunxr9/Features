# 武大上传数据处理脚本使用说明

## 环境准备

**系统环境**：

+ CentOS 7

  自行安装计算机系统．参见CentOS[安装指南](<https://docs.centos.org/en-US/centos/install-guide/>)．

+ python3.6+

  1. 更新系统以及安装 ius(CentOS工具库) 管理工具

     ```bash
     yum update
     yum install https://centos7.iuscommunity.org/ius-release.rpm
     ```

  2. 安装Python36

     ```
     yum install python36u
     ```

  3. 测试安装

     ```bash
     # 执行python3命令，正确进入shell环境即为成功
     python3
     ```

     

**运行环境**：

Python 模块安装通过pip命令进行，在进行依赖模块安装前应测试**`pip`** 是否存在，执行 `pip --help` 确认是否出现帮助文档，如果没有请确认Python3 的安装，或自行安装Python3版本的pip．

+ numpy

  ```bash
  pip3 install numpy
  ```

+ pandas

    ```bash
    pip3 install pandas
    ```

+ sqlalchemy

    ```bash
    pip3 install sqlalchemy
    ```

+ psycopg2-binary

    ```bash
    pip3 install psycopg2-binary
    ```

+ xlrd

    ```bash
    pip3 install xlrd
    ```

## 获取脚本

使用git 命令获取[项目文件](<http://192.168.3.200/wuda/iot_visualization>)：

```bash
git clone http://192.168.3.200/wuda/iot_visualization
```

## 运行脚本

进入获取的项目根目录，使用Python3运行，执行数据处理脚本需要携带待处理文件的绝对路径，例：

```bash
python3 wuda.py /home/file/excel/20191023/43a6d2a544c74ad9a662e2d5913f9616.xlsx
```

## 自定义使用

当前处理程序最终结果是将处理后的数据导入数据，而数据库连接信息为固定配置，所以在数据库地址以及用户或密码信息发生改变的情况，当前处理程序将无法使用．需要手动修改数据库连接配置信息才可以进行使用．

编辑处理程序文件，找到 `create_engine` 关键词，连接数据库的配置信息即在此处修改，当前默认的连接信息配置为：

```python
'postgresql+psycopg2://postgres:123456@192.168.3.232/wddc'
```

上述连接信息的填写规则是 `数据库类型+连接模块://用户名:密码＠数据库地址/数据库库名` ，可依据此规则进行自定义修改．例修改IP地址：

```python
'postgresql+psycopg2://postgres:123456@139.196.76.242/wddc'
```

