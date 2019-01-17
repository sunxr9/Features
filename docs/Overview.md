一体机部署的软件功能：

1．docker: 实现用户独立虚拟操作环境，

2．GitLab: 提供用户认证机制以及Git仓库管理．

3．nginx: 网站使用的负载均衡．

4．nbviewer: 报告的独立页面展示平台． 

5．JupyterHub: 提供身份验证和用户管理机制

6．Jupyter Lab: 提供在线交互式分析操作页面

7．Jupyter Notebook: 提供在线交互式分析核心和基础．



# 概述

​	一体机主要功能为实现软件整合，将所有的功能进行封装，做到单台服务运行所有功能，并尽可能实现一键部署或部署简单以及复用．

# 主要构成

## 技术构成

### docker

​	使用docker容器进行部署，提高可复用程度，减轻多次部署的重复无用功．

#### Nginx(docker 镜像)

​	提供web的反向代理功能，提高所有服务的稳定行以及安全性．

#### Jupyterhub(docker 镜像)

​	提供能对Jupyter Lab的多用户认证和管理．

#### JupyterLab(docker 镜像)

​	提供Jupyter的在线交互式分析．

#### GitLab-ce(docker 镜像)

​	提供用户认证和注册，及Git独立仓库等功能．

#### NBViewer(docker 镜像)

​	提供报告在线展示功能．

### docker-compose

​	多容器部署工具，简化部署步骤．

## 部署方案

​	通过docker技术实现．所有的服务全部为独立的镜像，并且所有镜像可独立运行，做到即开急用．减少环境依赖问题，增加各服务独立性，隔离性，复用性．

​	通过docker-compose实现多容器一条命令部署．并通过docker-compose.yml文件控制多个容器．并多个容器的进行运行配置，运行操作等功能．