# 一体机部署操作文档

## 前言

​	一体机部署为集成以及整合，开发，修改的功能．目前主要有Jupyter在线分析平台(Jupyter Notebook, Jupyter Lab)，JupyterHub多用户认证管理服务，NBViewer报告展示服务，GitLab项目规划和源代码管理工具．Nginx网站负载均衡调度工具．

​	[one_machine](http://106.15.198.200/lab_dev/one_machine)项目主要目标为部署的步骤简化，可复用性，便于实施的部署．实现快速可复制的部署一体机．项目中提供了JupyterHub，Nginx, GitLab的默认配置．

## 技术主体

### Linux(Ubuntu18.04 LTS)

​	底层操作系统．

#### 使用要点

​	基本liunx命令，命令行操作，安装所需软件(Docker)，基本用户权限管理(Docker安装需要手动添加用户至Docker组)．编辑文件能力．

### Docker

​	通过将应用程序和依赖关系捆绑到隔离但高度可移植的应用程序包中的轻量级方法.通过Docker实现上述多个服务的打包存储，可移植性．既获得即使用．

#### 使用要点

​	了解docker的基本使用．主要有一下场景：自定义启动容器，了解端口映射，数据卷映射，自定义构建镜像，镜像的推送和拉取．

### Python

​	`Jupyter`项目主要通过Python实现后台服务，所以需要了解Python基础，自定义配置修改

#### 使用要点

​	修改配置文件，

## 1. Docker环境配置

注：此文档是在Ubuntu18.04 LTS系统中实现．

### Ubuntu Docker 安装

#### 安装Docker

推荐使用APT安装：

```shell
sudo apt-get update
# 执行安装命令进行安装
sudo apt-get install docker.io
```

> 由于apt源使用HTTPS以确保软件过程中不被篡改，所以相对其他安装方式较为安全．

#### 启动Docker

```shell
sudo service docker start
```

#### 非root用户使用Docker

默认非root用户不可以使用docker命令的，我们需要将非root用户添加之docker组中，以便非root用户的使用．

```shell
# sudo usermod -g docker [用户名]
# 我们使用此命令将sgds用户添加之docker组中．
sudo usermod -g docker sgds
```

> 执行完成之后建议关键重启，以便与重新加载组信息．

**请注意:** 使用此方法安装不是docker发行版本的最新版．

#### 测试安装

使用一下命令测试安装，出现类似输出信息即为安装成功．

```shell
$ docker --version
Docker version 18.09.1, build 4c52b90
```

### 其他安装方式

Ubuntu安装[Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)参考．

## 2. Docker-compose环境配置

### Docker-compose

实现对 Docker 容器集群的快速编排与操作．

`Compose` 项目由 Python 编写，实现上调用了 Docker 服务提供的 API 来对容器进行管理。因此，只要所操作的平台支持 Docker API，就可以在其上利用 `Compose` 来进行编排管理。

此项目中通过`docker-compose`快速启动多个容器，并指定各容器之间配置．主要有数据卷映射，环境变量的修改，端口映射等一写信息．

### Ubuntu docker-compose 安装

#### 二进制安装

按照链接中的说明进行操作，该链接涉及`curl`在终端中运行命令以下载二进制文件。这些分步说明也包括在下面。

##### 运行次命令下载最新版的Docker Compose

```shell
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

##### 对二进制文件应用可执行权限

```shell
sudo chmod +x /usr/local/bin/docker-compose
```

#### PIP安装

这种方式是将 Compose 当作一个 Python 应用来从 pip 源中安装。

执行安装命令：

```bash
$ sudo pip install -U docker-compose
```

#### 测试安装

```shell
docker-compose --version
# 输出以下类似内容即为安装成功
# docker-compose version 1.23.2, build 1110ad01
```

## 3. 修改



​	