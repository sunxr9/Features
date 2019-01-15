# 一体机部署操作文档

## 前言

​	一体机部署为集成以及整合，开发，修改的功能．目前主要有Jupyter在线分析平台(Jupyter Notebook, Jupyter Lab)，JupyterHub多用户认证管理服务，NBViewer报告展示服务，GitLab项目规划和源代码管理工具．Nginx网站负载均衡调度工具．

​	[one_machine](http://106.15.198.200/lab_dev/one_machine)项目主要目标为部署的步骤简化，可复用性．便于实施的部署指导．实现快速可复制的部署一体机．项目中提供了JupyterHub，Nginx, GitLab的默认配置．

## 技术主体

### Linux

​	底层操作系统．

#### 使用要点

​	基本liunx命令，命令行操作，安装所需软件(Docker)，基本用户权限管理(Docker安装需要手动添加用户至Docker组)．编辑文件能力．

### Docker

​	通过将应用程序和依赖关系捆绑到隔离但高度可移植的应用程序包中的轻量级方法.通过Docker实现上述多个服务的打包存储，可移植性．既获得即使用．

#### 使用要点

​	了解docker的基本使用．主要有一下场景：自定义启动容器，了解端口映射，数据卷映射，自定义构建镜像，镜像的推送和拉取．

### Python

​	主要使用语法．用于修改配置文件．

#### 使用要点

​	修改配置文件，

## 1. Docker使用

### 1. Dokcer简述

Docker 是一个应用程序开发、部署、运行的平台，使用 go 语言开发。相较于传统的主机虚拟化，Docker 提供了轻量级的应用隔离方案，并且为我们提供了应用程序快速扩容、缩容的能力。

### 2. Docker基础名词

### 3. Docker 镜像构建，存储以及获取

### 4. Docker 网络设置

## 2. Docker-compose使用

### 1. Docker-compose简述

### 2. Docker-compose构建和使用

## 3. 一体机配置说明

### 1. JupyterHub

### 2. Nginx

### 3. GitLab

### 4. NBViewer



​	