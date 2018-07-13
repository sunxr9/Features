### docker

独立进程， 组件： （完整的操作系统，只读）镜像， （来运行）容器，仓库（存放地）

docker search 镜像名称

docker pull 镜像名称

docker images  查看镜像

镜像名称， 镜像标签， 镜像ID，时间，镜像大小

docker rmi 删除镜像

docker run 镜像名称  <镜像路径> ‘’

如本地没有运行镜像名称，默认会拉取后运行

docker ps -a 查看容器，

容器ID， 镜像名，运行的命令，创建时间， 状态， 

### 进入容器（以centos镜像为例）

docker run --name mydocker -it 镜像名称（centos） 命令（/bin/bash）

--name 创建的镜像名称

-i 输入终端保持打开状态 输入命令

-t 开一个伪终端 输入命令

进入容器内部，可以使用centos（一个小虚拟机）命令

docker run 命令只能在终端为关闭，或退出的状态运行

docker run -d --name mydocker1 centos 

-d 参数进行后台运行

执行此命令会返回一个hash值，很长



查看docker进程 docker ps -a  可以增加管道命令。 

docker ps -l 查看最后运行的容器

docker attach | exec  容器ID 进入容器，有可能进入失败，ctrl+c 终止程序会导致容器终止。

使用 nsenter  容器PID 进入容器

获取容器ID 获取命令docker inspect --format "{{.State.Pid}}" 镜像名称

进入容器命令 nsenter --target 容器pid --mount --uts --ipc --net --pid

此进入命令不影响容器运行。

```shell
# 获取容器pid 脚本
#! /usr/bash
CNAME=$1
CPID=$(docker inspect --format "{{.State.Pid}}" $CNAME)
nsenter --target "$CPTD" --mount --uts --ipc --net --pid
```

brctl show 查看docker的网桥， 默认有一个docker0 的网桥。

```shell
# iptables 命令 查看配置
iptables -L -t nat -n
# 容器内部
ip ro li # 查看网桥
```

docker 端口映射，将容器的端口映射到宿主机端口。

docker run -P -d --name mycentos centos # 随机映射，没有指定端口默认采用随机映射。端口不会冲突。注意是大写P

docker run -d -p 8000:80 --name mycentos centos # 指定映射， 前8000为宿主机的端口，后80为docker容器端口，小写。

指定规则：

```shell
# 指定映射
-p  hostPort:containerPort
-p	ip:hostPort:containerPort
-p	ip::containerPort # 绑定ip 端口随机
-p	hostPort:containerPort -p ...
```

-h 指定容器名

docker run -it --name mydocker -h hostname -v /data  docker(镜像名)  

-v 在容器根目录创建一个data 目录，可以在宿主机中查看，

docker inspect -f {{.Volumes}} 容器名（mydocker）查看容器的信息，获取宿主机和容器之间共享文件路径，

docker run -it --name mydocker -h hostname -v /opt:/opt docker指定宿主机和容器的数据挂载指定目录， 前为宿主机的目录路径，后为容器内的目录路径。注意路径后面不可以有斜线，例/opt/:/opt/，错误的

docker run -it --name mydocker2 --volumes-from mydocker1 docker

容器之间的共享数据。



自定制docker container 

docker run --name centos-test -it centos

安装配置

yum install wget gcc gcc-c++ make openssl-devel

pcre nginx 安装依赖。

使用wget 下载nginx压缩包。

tar zxf 解压下载文件

useradd -s /usr/nologin -M www



### 将容器做镜像。

docker commit -m '注释' 容器id 镜像名称(例 sunxr/my-容器名称：v1（版本）)

返回值为hash值。



DockerFile创建

创建docker-file 目录

创建Dockerfile 文件 注意D为大写。

```shell
# This is My first Dockerfile
# 第一步 告诉使用什么镜像 
FROM centos # 镜像名称，基础镜像
# 第二步
# maintainer 维护者信息
随便写

# 第三步 需要往容器中添加的文件。。
# ADD（压缩文件会自动解压）文件需和dockerfile 同级目录
ADD 文件名称， 存放文件路径

# 第四部
# run 告诉容器做点什么
RUN yum install -y wget gcc gcc-c++ make..
RUN useradd -s /sbin/

# 第五步 工作目录， 执行命令目录
#work dir 
WORKDIR /usr/local/src
RUN 需要执行命令

# 环境命令
ENV PATH /usr/local/nginx/sbin：$PATH
# 第六步
# EXPORT 映射端口
EXPORT 80

# CMD 执行的命令（）
CMD ['nginx']
```

完成之后执行 docker build -t nginx-file:v1 /opt/docker-file/nginx/

-t 为标签，或者可以理解为名称， 后问dockerfile 文件路径，（nginx为实例名称）



docker 资源隔离 LXC Kernel namespace 

`Pid、Net、Ipc、Mnt、Uts（容器自己名字）、User（）`