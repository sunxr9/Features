## 环境配置

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

### 其他安装方式

Ubuntu安装[Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)参考．



## 1. Docker使用

> **注意**: 请自行注册Docker帐号，本文档不提供[注册](https://hub.docker.com/signup)和[登录](https://id.docker.com/login/?next=%2Fid%2Foauth%2Fauthorize%2F%3Fclient_id%3D43f17c5f-9ba4-4f13-853d-9d0074e349a7%26next%3D%252Fsignin%253Fref%253Dlogin%26nonce%3DeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiI0M2YxN2M1Zi05YmE0LTRmMTMtODUzZC05ZDAwNzRlMzQ5YTciLCJleHAiOjE1NDc2MjAwMzEsImlhdCI6MTU0NzYxOTczMSwicmZwIjoiVEtENllqTi0wR1RmSEZnRElJWWdhUT09IiwidGFyZ2V0X2xpbmtfdXJpIjoiL3NpZ25pbj9yZWY9bG9naW4ifQ.MQnULUALtZHo_vI6XoxbtR4eZ2E1j7Bgh_P2cNqWWac%26redirect_uri%3Dhttps%253A%252F%252Fhub.docker.com%252Fsso%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%26state%3DeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiI0M2YxN2M1Zi05YmE0LTRmMTMtODUzZC05ZDAwNzRlMzQ5YTciLCJleHAiOjE1NDc2MjAwMzEsImlhdCI6MTU0NzYxOTczMSwicmZwIjoiVEtENllqTi0wR1RmSEZnRElJWWdhUT09IiwidGFyZ2V0X2xpbmtfdXJpIjoiL3NpZ25pbj9yZWY9bG9naW4ifQ.MQnULUALtZHo_vI6XoxbtR4eZ2E1j7Bgh_P2cNqWWac)描述．

### 1. Dokcer简述

​	Docker 是一个应用程序开发、部署、运行的平台，使用 go 语言开发。相较于传统的主机虚拟化，Docker 提供了轻量级的应用隔离方案，并且为我们提供了应用程序快速扩容、缩容的能力。

### 2. Docker基本概念

#### 1. 镜像

​	镜像是一个用来构建容器的只读模版，通常一个镜像会依赖其他的镜像。例如我们编写的一个Python Web程序需要依赖Python环境以及Web框架工具，那在构建这个应用镜像时就需要依赖基础的Python镜像。

​	我们可以创建自己的镜像，也可以使用仓库中已经创建好的镜像。创建镜像需要创建一个 `Dockerfile` 文件。`Dockerfile`中的每个RUN命令定义镜像文件中的一层，当定义发生变化的时候，只需要更新着一层的文件即可。所以`Docker`镜像是一个特殊的文件系统，除了提供容器运行是所需的程序，库，资源，配置等文件外，还包含了一些为运行准备的一些配置参数（如匿名卷，环境变量，用户等）．镜像不包含任何动态数据，其内容在构建之后也不会被改变．	

#### 2. 容器

​	容器是一个运行时状态下的镜像，通过docker命令我们可以创建、启动、停止、删除容器．

​	容器的实质是进程，但与直接在宿主执行的进程不同，容器进程运行于属于自己的独立的 [命名空间](https://en.wikipedia.org/wiki/Linux_namespaces)。因此容器可以拥有自己的 `root` 文件系统、自己的网络配置、自己的进程空间，甚至自己的用户 ID 空间。容器内的进程是运行在一个隔离的环境里，使用起来，就好像是在一个独立于宿主的系统下操作一样。这种特性使得容器封装的应用比直接在宿主运行更加安全。也因为这种隔离的特性，很多人初学 Docker 时常常会混淆容器和虚拟机。

​	每一个容器运行时，是以镜像为基础层，在其上创建一个当前容器的存储层，我们可以称这个为容器运行时读写而准备的存储层为**容器存储层**。容器存储层的生存周期和容器一样，容器消亡时，容器存储层也随之消亡。因此，任何保存于容器存储层的信息都会随容器删除而丢失。

按照 Docker 最佳实践的要求，容器不应该向其存储层内写入任何数据，容器存储层要保持无状态化。所有的文件写入操作，都应该使用 [数据卷（Volume）](https://yeasy.gitbooks.io/docker_practice/data_management/volume.html)、或者绑定宿主目录，在这些位置的读写会跳过容器存储层，直接对宿主（或网络存储）发生读写，其性能和稳定性更高。数据卷的生存周期独立于容器，容器消亡，数据卷不会消亡。因此，使用数据卷后，容器删除或者重新运行之后，数据却不会丢失。

#### 3. 仓库

​	镜像构建完成后，可以很容易的在当前宿主机上运行，但是，如果需要在其它服务器上使用这个镜像，我们就需要一个集中的存储、分发镜像的服务，[Docker Registry](https://yeasy.gitbooks.io/docker_practice/repository/registry.html) 就是这样的服务。

​	一个 **Docker Registry** 中可以包含多个**仓库**（`Repository`）；每个仓库可以包含多个**标签**（`Tag`）；每个标签对应一个镜像。

​	通常，一个仓库会包含同一个软件不同版本的镜像，而标签就常用于对应该软件的各个版本。我们可以通过 `<仓库名>:<标签>` 的格式来指定具体是这个软件哪个版本的镜像。如果不给出标签，将以 `latest` 作为默认标签。	

​	以 [Ubuntu 镜像](https://hub.docker.com/_/ubuntu) 为例，`ubuntu` 是仓库的名字，其内包含有不同的版本标签，如，`16.04`, `18.04`。我们可以通过 `ubuntu:14.04`，或者 `ubuntu:18.04` 来具体指定所需哪个版本的镜像。如果忽略了标签，比如 `ubuntu`，那将视为 `ubuntu:latest`。

​	仓库名经常以 *两段式路径* 形式出现，比如 `jwilder/nginx-proxy`，前者往往意味着 Docker Registry 多用户环境下的用户名，后者则往往是对应的软件名。但这并非绝对，取决于所使用的具体 Docker Registry 的软件或服务。

##### Docker Registry 公开服务

​	Docker Registry 公开服务是开放给用户使用、允许用户管理镜像的 Registry 服务。一般这类公开服务允许用户免费上传、下载公开的镜像，并可能提供收费服务供用户管理私有镜像。

​	最常使用的 Registry 公开服务是官方的 [Docker Hub](https://hub.docker.com/)，这也是默认的 Registry，并拥有大量的高质量的官方镜像。除此以外，还有 [CoreOS](https://coreos.com/) 的 [Quay.io](https://quay.io/repository/)，CoreOS 相关的镜像存储在这里；Google 的 [Google Container Registry](https://cloud.google.com/container-registry/)，[Kubernetes](https://kubernetes.io/) 的镜像使用的就是这个服务。

​	由于某些原因，在国内访问这些服务可能会比较慢。国内的一些云服务商提供了针对 Docker Hub 的镜像服务（`Registry Mirror`），这些镜像服务被称为**加速器**。常见的有 [阿里云加速器](https://cr.console.aliyun.com/#/accelerator)、[DaoCloud 加速器](https://www.daocloud.io/mirror#accelerator-doc) 等。使用加速器会直接从国内的地址下载 Docker Hub 的镜像，比直接从 Docker Hub 下载速度会提高很多。在 [安装 Docker](https://yeasy.gitbooks.io/docker_practice/install/mirror.html) 一节中有详细的配置方法。

​	国内也有一些云服务商提供类似于 Docker Hub 的公开服务。比如 [时速云镜像仓库](https://hub.tenxcloud.com/)、[网易云镜像服务](https://c.163.com/hub#/m/library/)、[DaoCloud 镜像市场](https://hub.daocloud.io/)、[阿里云镜像库](https://cr.console.aliyun.com/) 等。

##### 私有 Docker Registry

​	除了使用公开服务外，用户还可以在本地搭建私有 Docker Registry。Docker 官方提供了 [Docker Registry](https://hub.docker.com/_/registry/)镜像，可以直接使用做为私有 Registry 服务。在 [私有仓库](https://yeasy.gitbooks.io/docker_practice/repository/registry.html) 一节中，会有进一步的搭建私有 Registry 服务的讲解。

​	开源的 Docker Registry 镜像只提供了 [Docker Registry API](https://docs.docker.com/registry/spec/api/) 的服务端实现，足以支持 `docker` 命令，不影响使用。但不包含图形界面，以及镜像维护、用户管理、访问控制等高级功能。在官方的商业化版本 [Docker Trusted Registry](https://docs.docker.com/datacenter/dtr/2.0/) 中，提供了这些高级功能。

​	除了官方的 Docker Registry 外，还有第三方软件实现了 Docker Registry API，甚至提供了用户界面以及一些高级功能。比如，[VMWare Harbor](https://github.com/goharbor/harbor) 和 [Sonatype Nexus](https://yeasy.gitbooks.io/docker_practice/repository/nexus3_registry.html)。

#### 4. 应用数据

Docker在默认情况下，应用的所有数据都之后存储在可写层中。所以会出现一下情况：

1. 数据不会持久存在，随容器消失而消失。
2. 与容器紧密耦合，无法轻松转移数据。
3. 写入容器需要liunx内核提供联合文件系统，这样额外的降低了性能。

##### 解决方案

**volumes(卷)**：由Docker创建和管理。储存在(在linux下`/var/lib/docker/volumes`),是Docker中保留数据的最佳方式．

**mount（挂载）**：可以存储在主机系统的任何位置，Docker进程和非Docker进程都可以随时修改他们。

**tmpfs挂载**：仅存储在主机系统的内存中，永远不会写入主机系统的文件系统。

一般

### 3. Docker 镜像构建，分享以及获取

#### 构建

​	自定义构建镜像主要通过`Dockerfile`文件编写实现，通过`docker`命令操作进行构建．

​	`Dockerfile`文件定义容器内环境中发生的事情。对网络接口和磁盘驱动器等资源的访问在此环境中进行虚拟化，该环境与系统的其他部分隔离，因此您需要将端口映射到外部世界，并具体说明要“复制”哪些文件到环境中的具体位置。但是，在执行构建此操作之后，您可以预期`Dockerfile`在此处定义和构建的应用程序在其任何位置运行都会完全相同。

##### Dockerfile

​	创建一个空目录，并`cd`至新创建的目录中，创建名为`Dockerfile`的文件，将以下内容复制并粘贴到该文件中，然后保存，请注意每个语句的注释，留意每个语句的关键词．下面会详细介绍关键词的作用．

```dockerfile
# 使用官方指定的Python作为父镜像
FROM python:2.7-slim

# 设置工作目录，请注意使用绝对路径．
WORKDIR /app

# 复制当前目录下的内容到容器中的/app目录下．中间使用空格分开的．
COPY . /app

# 安装requirements.txt中指定的所需包．
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
# 将容器内部的８０端口暴露给容器外部主机．
EXPOSE 80

# 定义环境变量
ENV NAME World

# 定义容器在启动是，容器内部执行的命令．
CMD ["python", "app.py"]
```

##### 应用程序

​	在`Dockerfile`同级目录下创建两个文件，分别为`requirements.txt`，`app.py`．这是一个非常简单应用程序．当上述`Dockerfile`构建镜像，由于`Dockerfile`的COPY命令，`app.py`和`requirement.txt`存在，并且由于EXPOSE命令，`app.py`的输出可通过HTTP访问．

**requirements.txt**

```
Flask
Redis
```

**app.py**

```python
from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

现在我们看到`pip install --trusted-host pypi.python.org -r requirements.txt`为Python安装Flask和Redis库，应用程序打印环境变量`NAME`，以及调用的输出`socket.gethostname()`。最后，以为Redis没有运行，我们会得到他的尝试失败并产生错误信息．

##### 构建应用程序

准备构建应用程序，确认你处于`Dockerfile`文件目录下．当前应存在以下文件：

```shell
$ ls
Dockerfile		app.py			requirements.txt
```

现在运行`build`构建命令，这将创建一个Docker镜像，并使用`--tag`选项直接命名．另可以使用`-t`代替上述选项．

```shell
# 注意最后的一个点
docker build --tag=hello .
```

等待构建完成．

##### 查看镜像

构建的镜像存在本地Docker Registry中：

```shell
$ docker image ls

REPOSITORY            TAG                 IMAGE ID
hello         		latest              326387cea398
```

注意默认的标签名称为`latest`,标签的完整语法为`--tag=hello:V1.0.0`，使用**`:`**进行分割．

##### 测试镜像运行

运行应用程序，使用`-p`命令将计算机(物理机或宿主机)的端口4000映射到容器发布的端口80, 示例:

```shell
docker run -p 4000:80 hello
```

现在通过浏览器访问`http://localhost:4000`，应该得到Python的应用程序正在为你提供服务返回的信息．但是该消息来自容器内部，该容器不知道容器的端口80映射到计算机的端口4000，从而我们使用`http://localhost:4000`访问．

最后使用`CTRL + c`停止容器运行．

#### 分享

通过Docker Registry公开服务，我们可以上传构建的图像并在其他地方获取，运行．

Docker Registry是存储库的集合，存储库是图像的集合 - 类似于GitHub存储库，除了代码已经构建。注册表上的帐户可以创建许多存储库。该`docker`CLI使用泊坞窗的公共注册表默认情况下。

##### 标记镜像

​	将本地映像与Docker Registry上的存储库相关联的表示法是 `username/repository:tag`。标签是可选的，但建议使用，因为它是注册管理机构用来为Docker镜像提供版本的机制。为上下文提供存储库和标记有意义的名称，例如 `get-started:part2`。这会将图像放入`get-started`存储库并将其标记为`part2`。

现在使用命令来标记镜像，docker tag image 使用您的用户名，存储库和标记名称来运行，以便将图像上传到所需的目标位置，该命令的语法示例：

```shell
docker tag image register/username:tag
```

为上述构建的镜像做标记：

```shell
docker tag hello sunxr/hello:V1.0.0
```

使用`docker image ls`查看新标记的镜像．

```shell
$ docker image ls

REPOSITORY               TAG                 IMAGE ID            CREATED             SIZE
hello            		latest              d9e555c53008        3 minutes ago       195MB
sunxr/hello         	V1.0.0               d9e555c53008        3 minutes ago       195MB
python                   2.7-slim            1c7128a655f6        5 days ago          183MB
```

##### 上传镜像

将标记的图像上传到存储库：

```shell
docker push register/username:tag
```

示例：

```shell
docker push sunxr/hello:V1.0.0
```

完成之后，此上传的结果将公开发布．登录[Docker Hub](https://hub.docker.com/)，则会看到新图像及其pull命令．

> **注意**:　推送之前请在[本地登录](https://docs.docker.com/get-started/part2/#log-in-with-your-docker-id)．

#### 获取

##### 获取镜像

现在开始，可以使用`docker run`命令在任何计算机上使用和运行上述的应用程序．

```shell
docker　run -p 4000:80 register/username:tag
```

如果镜像不在需要运行的计算机上，Docker则会自行从存储库中拉取镜像．我们也可以自行使用`docker pull`自行拉取，完成后执行上述命令进行运行．

docker pull 示例：

```shell
docker pull register/username:tag
```

docker run 示例：

```shell
$ docker run -p 4000:80 gordon/get-started:part2
Unable to find image 'gordon/get-started:part2' locally
part2: Pulling from gordon/get-started
10a267c67f42: Already exists
f68a39a6a5e4: Already exists
9beaffc0cf19: Already exists
3c1fe835fb6b: Already exists
4c9f1fa8fcb8: Already exists
ee7d8f576a14: Already exists
fbccdcced46e: Already exists
Digest: sha256:0601c866aab2adcc6498200efd0f754037e909e5fd42069adeff72d1e2439068
Status: Downloaded newer image for gordon/get-started:part2
 * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
```

> **注意**:　无论`docker run`还是`docker pull`命令，在需要获取远程存储库镜像的时候，都需要本地进行登录，请参考[本地登录](https://docs.docker.com/get-started/part2/#log-in-with-your-docker-id)．

#### Dockerfile 主要关键词说明

**FROM**:　指定基础镜像．所有的的程序都需要底层环境支撑，例如Python的程序需要使用有Python语言的环境，而Python又需要在操作系统中(Ubuntu,Mac,Windows)，所以基础镜像是必须的，并且是第一条指令．

```
FROM python:2.7-slim
```

**LABEL**: 帮助按项目组织图像，记录许可信息，帮助实现自动化或出于其他原因。对于每个标签，添加`LABEL`以一个或多个键值对开头的行。目前主要有两种写法：

```
# 多行
LABEL com.example.version="0.0.1-beta"
LABEL vendor1="ACME Incorporated"
LABEL vendor2=ZENITH\ Incorporated
# 一行　使用空格分割
LABEL vendor=ACME\ Incorporated \
      com.example.is-beta= \
      com.example.is-production="" \
```



**RUN**: `RUN`将复杂语句或长语句拆分成多行，并是用反斜杠（\ 命令行中的不换行符号）和＆＆链接起来，以使`Dockerfile`更具可读性，可理解性和可维护性。

```
 RUN apt-get update && apt-get install -y \
        package-bar \
        package-baz \
        package-foo=1.3.*
```

**CMD**: `CMD`指令应用与容器启动时，需要运行的程序的启动命令以及传递的参数．

官方推荐使用exec 格式，这类格式解析时会被解析成`JSON`数组，所以要使用**双引号**，不能使用单引号．

```
CMD ["jupyterhub", "-f", "/etc/jupyterhub/jupyterhub_config.py"]
```

> **注意**：　`CMD`在每个`Dockerfile`中只有最后一个生效．

**EXPOSE**: 指示容器侦听连接的端口。因此，您应该为您的应用程序使用通用的传统端口。例如，包含Apache Web服务器`EXPOSE 80`的图像将使用，而包含MongoDB的图像将使用`EXPOSE 27017`，依此类推。

**ENV**: 该`ENV`指令将环境变量`<key>`设置为该值 `<value>`。此值将在构建阶段中所有后续指令的环境中，并且也可以在后续中进行替换。跟随镜像一直存在．

**COPY**:　将本地文件复制到容器指定位置，主要格式如下：

```
COPY [--chown=<user>:<group>] <源路径>... <目标路径>
COPY [--chown=<user>:<group>] ["<源路径1>",... "<目标路径>"]
```

目前主要使用第一种，其中的修改文件权限和用户的选项很少使用，所以简化为下属格式：

```
COPY <源路径> <目标路径>
```

> **注意**: `<源路径>`可以是`Dockerfile`文件的相对路径，但是`<目标路径>`的相对路径是根据`WORKDIR`指定的路径，所以推荐使用绝对路径来进行复制．目标路径不需要实现创建，如果目标路径不存在，复制文件之前会先行创建缺失目录．

**ADD**：`ADD` 指令和 `COPY` 的格式和性质基本一致。但是在 `COPY` 基础上增加了一些功能，主要有可以使用`URL`直接向容器内部添加文件,文件解压缩(限tar提取和URL支持)等．



**VOLUME**: 该`VOLUME`指令创建具有指定名称的安装点，并将其标记为从本机主机或其他容器保存外部安装的卷。该值可以是JSON数组，`VOLUME ["/var/log/"]`或具有多个参数的普通字符串，例如`VOLUME /var/log`或`VOLUME /var/log /var/db`。

**USER**：切换容器内部的用户，构建最后应避免使用`root`用户运行应用．

**WORKDIR**: 切换执行目录，相当与liunx下的`cd`.

**ARG**:  `Dockerfile`中的变量．

```
ARG user1=someuser
ARG buildno=1
```

### 4. docker 运行

#### 启动容器

`docker run`指令启动容器：

```
# docker run 镜像名称
docker run jupyterhub
```

#### 查看运行容器

`docker ps `查看运行容器，在没有参数的情况下，默认只显示最近启动的容器，

`-a`参数查看所有容器。

`-l`查看在运行容器。

> 注意：请注意默认生成的容器名称。

#### 停止容器

`docker stop [容器名称]`指令停止正在运行的容器。

> 注意: 此处的容器名称在未使用`-n`或`--name` 指定的情况下，需要使用上述指令查看容器名称，

#### 指定容器名称

`--name`参数指定容器运行名称。

```
# docker run -n name 镜像名称
docker run -n jupyterhub jupyterhub
```

#### 指定端口启动

使用`-p`或`--publish`参数指定端口启动，可多此次使用。

```
# docker run -p 主机端口:容器内部端口 镜像名称
docker run -p 8000:8000 jupyterhub
```

> 注意：请注意容器内部端口为EXPOSE指定的暴露端口，一般设置为熟知端口，比如`nginx`为80端口，所以我们只需要将主机端口对应的80端口映射至容器内部80端口即可。

#### 挂载数据启动

使用`-v`或`--volume`参数指定挂载文件或目录。

```
# docker run -p 主机端口：容器内部端口 -v 主机路径：容器内部路径 镜像名称
docker run -p 8000:8000 -v /etc/jupyterhub:/etc/jupyterhub jupyterhub
```

> 注意：挂载的目录的情况下，主机路径的最后不可为**`/`**符号（liunx环境下）

#### 守护进程运行

`-d`参数。

```
# docker run -d -p 主机端口：容器内部端口 -v 主机路径：容器内部路径 镜像名称
docker run -d -p 8000:8000 -v /etc/jupyterhub:/etc/jupyterhub jupyterhub
```

#### 非守护进程启动

`-i -t`参数，可简写为`-it`.

```
# docker run -it -p 主机端口：容器内部端口 -v 主机路径：容器内部路径 镜像名称
docker run -it -p 8000:8000 -v /etc/jupyterhub:/etc/jupyterhub jupyterhub
```

#### 进入容器

1.  `docker exec `指令.

   ```
   # docker exec -it 容器名称 执行的命令
   docker exec -it 容器名称 /bin/bash
   ```

2. `docker attch`指令。

   ```
   # docker attch 容器名称
   ```

#### 退出容器

1. `docker exec`指令进入容器类似于`ssh`登录，可以使用`exit`命令退出，并不会影响容器的运行，但是不能停止容器内运行的应用程序。

2. `docker attch`指令进入容器不可以使用使用上述方式退出，想要在不影容器运行的情况下退出只能使用`ctrl + q`方式退出。

### 5. Docker 常用命令和说明

参见docker文件．

## 2. Docker-compose使用

### 1. Docker-compose简述

实现对 Docker 容器集群的快速编排与操作．

使用一个 `Dockerfile` 模板文件，可以让用户很方便的定义一个单独的应用容器。然而，在日常工作中，经常会碰到需要多个容器相互配合来完成某项任务的情况。例如要实现一个 Web 项目，除了 Web 服务容器本身，往往还需要再加上后端的数据库服务容器，甚至还包括负载均衡容器等。

`Compose` 恰好满足了这样的需求。它允许用户通过一个单独的 `docker-compose.yml` 模板文件（YAML 格式）来定义一组相关联的应用容器为一个项目（project）。

`Compose` 中有两个重要的概念：

- 服务 (`service`)：一个应用的容器，实际上可以包括若干运行相同镜像的容器实例。
- 项目 (`project`)：由一组关联的应用容器组成的一个完整业务单元，在 `docker-compose.yml` 文件中定义。

`Compose` 的默认管理对象是项目，通过子命令对项目中的一组容器进行便捷地生命周期管理。

`Compose` 项目由 Python 编写，实现上调用了 Docker 服务提供的 API 来对容器进行管理。因此，只要所操作的平台支持 Docker API，就可以在其上利用 `Compose` 来进行编排管理。

### 2. Ubuntu docker-compose 安装

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

### 3. Docker-compose使用

#### 示例

先通过一个简单的web应用示例来展示

##### web 应用

新建文件夹，在该目录中编写 `app.py` 文件

```python
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! 该页面已被访问 {} 次。\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```

##### Dockerfile

编写 `Dockerfile` 文件，内容为

```dockerfile
FROM python:3.6-alpine
ADD . /code
WORKDIR /code
RUN pip install redis flask
CMD ["python", "app.py"]
```

##### docker-compose.yml

编写 `docker-compose.yml` 文件，这个是 Compose 使用的一个简单配置文件。

```yaml
version: '3'
services:

  web:
    build: .
    ports:
     - "5000:5000"

  redis:
    image: "redis:alpine"
```

##### 运行 compose 项目

```bash
$ docker-compose up
```

此时访问本地 `5000` 端口，每次刷新页面，计数就会加 1。

#### docker-compose 说明：

由`Docker-compose`简述中了解到，compose文件中主要有两个部分，服务(servers)和项目(projects)．以上述的`docker-compose.yml`为例，项目为`servers`关键词开始，在项目中运行名为`web`和`redis`的两个服务．

> 请严格遵循[YAML](https://yaml.org/spec/1.0/)语法．

​	在两个服务中只有最简单的配置，`web`服务提够了构建服务，并指定容器暴露端口．`redis`服务指定使用镜像名称．

> **注**:　`docker-compose`中的构建依赖于`Dockerfile`文件,不是独立存在．

​	在服务中可定义以下选项以及简要说明，详情参考[官方文档](https://docs.docker.com/v17.09/compose/overview/)：

+ `build`

  指定`Dockerfile`所在目录的路径(相对路径绝对路径都可)．`Compose`将利用它自动构建镜像并使用．

​	服务容器一旦构建后，将会带上一个标记名，例如`servers`服务中的web容器，那标记就可能为`servers_web`．

+ command

  用于覆盖容器启动时默认执行的命令．如:

  ```
  # jupyterhub容器的默认指令是
  command:
    jupyterhub -f /etc/jupyterhub/jupyterhub_config.py
  ```

  我们可通过`command`来自定义指定启动命令，例：

  ```
  # 改变启动的的时候读取的配置文件目录
  command:
    jupyterhub -f /home/name/jupyterhub_config.py
  ```

+ container_name

  指定容器名称。默认将会使用 `项目名称_服务名称_序号`．

+ devices

  指定设备映射关系．如：

  ```
  devices:
    - "/dev/USB1:/dev/USB0"
  ```

+ depends_on

  解决容器之间的依赖，启动的先后问题．在选项中只需要按照想要的启动顺序一次填写即可，如：

  ```
  depends_on:
    - mysql
    - redis
  # 例子中会先启动mysql,在启动redis.
  ```

+ dns

  自定义`DNS`服务器．可以是一个值，也可是列表．

+ tmpfs

  挂载一个tmpfs文件系统到容器．

+ env_file

  从文件中获取环境变量，可以为单独的文件路径或列表．如：

  ```
  # 独立文件
  env_file: .env
  
  # 多个路径
  env_file:
    - ./apps/web.env
    - /opt/secrets.env
  ```

+ environment

  设置环境变量．可使用数组或字典两种格式．只给定名称的变量会自动获取运行Compose主机上的对应变量值，可用来在`docker-compose`文件中隐藏变量值．

  ```
  # 字典
  environment:
    RACK_ENV: development
    SESSION_SECRET:
  # 数组
  environment:
    - RACK_ENV=development
    - SESSION_SECRET
  ```


> 注：如果在env文件中的变量名称与enviroment指令相冲突，则以后者为准．

+ expose

  暴露端口，但不映射到宿主机，只被链接的服务访问．仅可以制定内部端口为参数．

  ```
  expose:
    - "3000"
    - "8000"
  ```

+ external_links

  链接到`docker-compose.yml`外部的容器，甚至并非`Compose`管理的外部容器．

  ```
  external_links:
    - redis_1
    - project_db_1: mysql
    - project_db_1: postgresql
  ```

+ extra_hosts

  添加容器内部的host名称映射信息，类似Docker中的`--add-host`参数．

  ```
  extra_hosts:
    - "googleedns:8.8.8.8"
  ```

  会在启动之后在容器内部的`/etc/hosts`文件中添加如下条目:

  ```
  8.8.8.8 googleedns
  ```

+ healthcheck

  通过命令检查容器的运行：

  ```
  healthcheck:
    test: ["CMD", "curl", "-f", "http://localhost"]
    interval: 1m30s
    timeout: 10s
    retries: 3
  ```

+ image

  指定使用的镜像名称或镜像ID．如果本地不存在，`Compose`将会尝试获取这个镜像．

+ labels

  为容器添加Docker元数据信息，例如可以容器添加辅助说明信息．

+ logging

  配置日志选项：

  ```
  logging:
    driver: syslog
    options:
    syslog-address: "tcp://192.168..0.42:1000"
  ```

  目前支持三种日志驱动类型：

  ```
  driver: "json-file"
  driver: "syslog"
  driver: "none"
  ```

  `options`配置日志驱动的相关参数：

  ```
  options:
    max-size: "200k"
    max-file: "10"
  ```

+ network_mode

  设置网络模式，和`docker run`指令启动是制定的`--network`参数是一致的．

  ```
  network_mode: "bridge"
  network_mode: "host"
  network_mode: "none"
  network_mode: "service:[service name]"
  network_mode: "container:[container name/id]"
  ```

+ networks:

  配置容器连接的网络．

  ```
  version: "3"
  services:
  
    some-service:
      networks:
       - some-network
       - other-network
  
  networks:
    some-network:
    	external: true
    	
    other-network:
  ```

  > 注：在项目中(`servers`同级的networks)为定义　需要使用的网络名称和网络配置，在本地没有的情况，Docker会自行创建网络．
  >
  > 在服务中的`networks`为指定需要使用的网络名称．

+ pid

  跟主机系统共享进程命名空间．打开该选项的容器之间以及容器和宿主机系统之间可以通过进程ID来相互访问和操作．

  ```
  pid: "host"
  ```

+ ports

  映射容器在宿主机上的通信的端口．

  格式为： 宿主机端口：容器端口(HOST: CONTAINER)格式，或者仅仅指定容器的端口（宿主机将会随机选择端口）．

  ```
  ports:
    - "2000"
    - "3000:3000"
    - "4000:80"
    - "127.0.0.1:5000:5000"
  ```

+ secrets

  存储敏感数据．

  ```
  version: "3.1"
  services:
  
  mysql:
    image: mysql
    environment:
      MYSQL_ROOT_PASSWORD_FILE: /run/secrets/db_root_password
    secrets:
      - db_root_password
      - my_other_secret
  
  secrets:
    my_secret:
      file: ./my_secret.txt
    my_other_secret:
      external: true
  ```

+ security_opt

  指定容器模板标签（label）机制的默认属性（用户，角色，类型，级别等），例如配置标签的用户名和角色名：

  ```
  security_opt:
    - label:user:USER
    - label:role:ROLE
  ```

+ stop_signal

  设置另一个信号来停止容器．在默认情况下使用的是SIGTERM停止容器．

  ```
  stop_signal: SIGUER1
  ```

+ ulimits

  指定容器的ulimits限制值．例如，指定最大进程数65535,指定文件句柄数为20000(软限制，应用可以随时修改，不能超过硬限制)和40000（系统硬限制，只能root用户提供）．

  ```
  ulimits:
    nproc: 65535
    nofile:
      soft: 20000
      hard: 40000
  ```

+ volumes

  数据卷所挂载的路径设置．可以设置素主机路径（HOST：CONTAINER）或加上访问模式(HOST:CONTAINER:ro)．

  ```
  volumes:
    - /var/lib/mysql
    - cache:/tmp/cache
    - ~/configs:/etc/configs:ro
  ```

  > 注: 该指令中路径支持相对路径．不推荐在容器内部的使用相对路径．

+ 其他说明

  此外`docker run`中对应的参数同样可以在文件中配置．

  + 指定服务容器启动后执行的入口文件．
  ```
    entrypoint: /code/entrypoint.sh
  ```

  + 指定容器中运行应用的用户名.

  ```
  user: username
  ```

  + 指定容器内部工作目录

  ```
  working_dir: /home/name
  ```

  + 指定容器内搜素域名，主机名，mac地址等．

  ```
  domainname: your_website.com
  hostname: test
  mac_address: 08-00-27-00-0C-0A
  ```

  + 允许容器中运行一些特权命令。

  ```yaml
  privileged: true
  ```

  + 指定容器退出后的重启策略为始终重启。该命令对保持服务始终运行十分有效，在生产环境中推荐配置为 `always` 或者 `unless-stopped`。

  ```yaml
  restart: always
  ```

  + 以只读模式挂载容器的 root 文件系统，意味着不能对容器内容进行修改。

  ```yaml
  read_only: true
  ```

  + 打开标准输入，可以接受外部输入。

  ```yaml
  stdin_open: true
  ```

  + 模拟一个伪终端。

  ```yaml
  tty: true
  ```

  + 读取系统的环境变量和当前目录的`.env`文件中的变量．

  ```
  version: "3"
  services:
  db:
    image: "mongo:${MONGO_VERSION}"
  ```

  

  