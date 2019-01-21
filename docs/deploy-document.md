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

> 注：此文档是在Ubuntu18.04 LTS系统中实现．
>
> 注：此项目所有容器均在官方[DokcerHub](https://hub.docker.com),请自行[登录](https://id.docker.com/login/)/[注册](https://hub.docker.com/signup)，并在本地进行[登录](https://docs.docker.com/engine/reference/commandline/login/#description)，否则无法获取镜像．

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

### 使用详情

参考docker-use文件docker-compose配置详情．

## 3. 获取项目

```shell
git clone http://106.15.198.200/sunxr/test.git
```

## 4. 运行准备

### 配置Jupyterhub

#### 容器控制

定义配置文件主要是自定义Jupyterhub启动选项，其中主要为选择认证方式，默认配置文件中携带的为使用GitLab认证方式，

Jupyterhub配置项目中默认携带以下配置文件：

```
import os
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"
notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR") or "/home/jovyan/work"
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = {"user-{username}": notebook_dir}
```

上述配置依次为**选择用户环境产生方式**,**设置用户的工作目录**，**设置用户的独立数据目录格式**．当前选择的为`dockerspawner`,在`Docker`容器中生成单用户服务器．另外还支持更多[**产生方式**](https://github.com/jupyterhub/jupyterhub#spawners)，请自行查看．

​	`dockerspawner`为容器中单用户服务，所以需要设置在容器中设置用户的工作目录，由此`c.DockerSpawner.notebook_dir`为设置用户在容器中的工作起始目录．

> 注：notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR") or "/home/jovyan/work"为变量，不对jupyterhub的运行作出任何影响．

​	设置完用户的工作目录之后就要考虑用户的数据保存问题，`docker`会自行替我们做了这些事情，但是保存下来的为`hash`值数据目录，不方便查找，所以我们需要设置用户数据保存数据的目录格式化，这样就能方便的查找．

> 注：目录名称的格式化遵循的是Python的格式化语法，所以此处设置中的***{username}***为必须遵守的，前面的**user**可替换为任何值．

单单设置好用户的数据保存目录名称是不够的，因为它不知道需要保存容器的什么数据，在什么地方．因此我们还需要告诉程序需要保存的数据在容器内部的哪个目录之下．所以此处的参数为字典形式．键为用户在主机上保存数据的目录名称格式化样式，值为容器内部那个目录下的数据需要保存．这样就用户数据就可以在主机上进行持久保存．

```
c.DockerSpawner.container_image = 'sunxr/dass:V0.5'
network_name = os.environ["DOCKER_NETWORK_NAME"]
c.DockerSpawner.network_name = network_name
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.extra_host_config = {"network_mode": network_name}
```

在设置使用什么程序进行产生服务，用户工作目录，数据持久化之后，就需要告诉程序使用什么`Docker`镜像进行工作，设置好使用什么镜像之后，那镜像启动之后的容器之间通信，连接等,所以需要设置`network_name`，`use_internal_ip`和`extra_host_config`．解决`Docker`容器通信，连接问题．

> 注:由于本次选择的`Jupyterhub`容器来管理，所以每个单用户服务的产生更像是在`JupyterHub`容器内部再创建单用户服务，但是`Docker`容器之间的嵌套并不是在容器内部在创建容器，而是通过主机上的`/var/run/docker.sock`来进行操作，所以`docker-compose`文件中`hub`服务的volumes添加了`docker.sock`文件的映射．详情请参考[套接字选项](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option)．

```
c.JupyterHub.hub_ip = "jupyterhub"
c.JupyterHub.hub_port = 8080

data_dir = os.environ.get('DATA_VOLUME_CONTAINER', '/data')
c.JupyterHub.cookie_secret_file = os.path.join(data_dir,
    'jupyterhub_cookie_secret')
```

设置完成网络之后，`Jupyterhub`操作主机上的镜像解决了，但是新创建的容器如何进行访问`Jupyterhub`还没有解决，所以通过设置`hub_ip`，用户的容器将通过容器名称进行访问．此处的容器名称应合`docker-compose`文件hub服务的容器名称一致．

>  注：上述的容器名称，通过`docker-compsoe`文件hub服务选项中的container_name来指定．

通信的端口为正常的端口设置．

> 注：`Docker`容器之间的端口默认是相互开放的，没有限制，所以在`docker-compose`文件中没有指定通信端口并不影响．[详情](https://docs.docker.com/v17.09/engine/userguide/networking/default_network/container-communication/#communication-between-containers).

`c.JupyterHub.cookie_secret_file `设置`JupyterHub`的cookie文件存放位置，并在`docker-compose`文件hub服务的`volumes`选项映射在主机之上．

以上将`JupyterHub`控制容器，容器与容器之间通信，数据保存定义完成．

#### 容器内部

我们还需要定义容器内部的启动，因为容器内部的启动默认`Jupyter Lab`．但是没有前往`Jupyterhub`控制页面的菜单，所以我们需要更改启动入口，使用`Jupyter`中`labhub`的入口启动程序，增加`Jupyter Lab`的`hub`菜单选项．

```
c.Spawner.cmd = ['jupyter-labhub']

c.Spawner.default_url = '/lab'
```

而`default_url`选项只是通过`url`设定，将首次打开服务的路由定为'http://ip/lab',从而确定进入入`Jupyter Lab`页面，而不是`notebook`页面．

#### 用户认证配置

本项目中默认携带的为使用GItLab提供的第三方认证方式是，在配置文件中主要有一下几点：

```python
from oauthenticator.gitlab import GitLabOAuthenticator
c.JupyterHub.authenticator_class = GitLabOAuthenticator
c.GitLabOAuthenticator.oauth_callback_url = 'http://192.168.31.163/hub/oauth_callback'
c.GitLabOAuthenticator.client_id = '10dca90acef97c2cb533a0e67306d37db6db00ea21ca89774c0ed0f4b869a8c5'
c.GitLabOAuthenticator.client_secret = '2a265ee30c505f8ffd26c8ac972725b56f271131b0285dd9005007f8dd4f0835'
```

由于默认的`JupyterHub`认证为`PAMAuthenticator`，所以我们需要导入使用的认证包．并通过`c.JupyterHub.authenticator_class = GitLabOAuthenticator`告诉`JupyterHub`需要使用的认证处理方法．其他[认证方式](https://github.com/jupyterhub/jupyterhub#authenticators)同理.

认证处理方法告诉`Jupyterhub`，当时这个认证方法所需要的一下要求我们还没有给出．主要有以下三个参数：

1. 认证完成后的回调`ｕrl`，此参数告诉GitLab认证完成之后如何回到原有的服务地址，并携带认证信息．
2. 连接需要认证的`id`．`GitLab`需要此信息进行确认，是否需要给你进行认证服务．
3. 连接需要认证的`secret`．与上同理，二者需要都有．

上述的参数配置`url`请自行确认运行主机的`IP`地址，只需将`IP`跟换即可，路由信息不可变动．而`GitLab`的`client_id`和`client_secret`如需要更改，需自行去GitLab进行创建`Application`认证．在`Jupyterhub`配置文件中不需要修改，此认证`client_id`和`client_secret`有效．

**用户配置白名单**

配置使用认证方式之后还需要配置用户权限管理：

```
c.Authenticator.whitelist = whitelist = set()
c.Authenticator.admin_users = admin = set()
c.JupyterHub.admin_access = True

path = os.path.dirname(__file__)
with open(os.path.join(path, "userlist")) as f:
    for line in f:
        if not line:
            continue

        parts = line.split()
        if len(parts) >= 1:
            name = parts[0]
            whitelist.add(name)
            if len(parts) > 1 and parts[1] == "admin":
                admin.add(name)
```

`Jupyterhub`提供白名单和管理员两种权限，目前添加的方式为在`JupyterHub`配置文件同级目录下的userlist文件中填写，填写方式为:

```
# 用户名称　用户权限 
# 白名单用户只需要填写用户名称即可，管理员用户需要在用户名称之后使用空格分隔，并声明为`admin`用户．如：
# 白名单用户
username
# 管理员用户
username admin
```

### 配置NBViewer

NBViewer没有配置文件，它的配置信息只需要在`docker-compose`文件中nbviewer服务中`command`选项修改即可．`docker-compose`文件中默认启动配置如下：

```shell
python -m nbviewer --port=9000 --no_cache=True --localfiles="/notebook" --base_url="/nbviewer"
```

> 默认配置说明：NBViewer使用9000端口，不对文件进行缓存，localfiles路径为'/notebook'(此为容器内部的路径)，设置默认`url`为`/Nbviewer`．

可增加配置如下：

```
--debug		是否以debug默认模式启动，默认为False
--localfile_follow_symlinks		使用realpath解析/遵循指向其目标文件的符号链接, 默认为False.
--localfile_any_user	提供本地文件系统上“其他”无法读取的文件,默认为False.
--host		在指定的接口上运行，类型为str.默认为０．０．０．０．
--cache_expiry_min		最小缓存到期时间，默认为10*60秒．
--cache_expiry_max		最大缓存时间，默认为2*60*60秒．
--mc-threads		用于Async　Memcached的线程数，默认为１，类型为整数．

--no-check-certificate		不验证SSL证书．默认为False.

--processes		使用进程代替线程进行渲染，默认为０，类型为整数．
--proxy-host                   代理主机，类型为字符
--proxy-port                   代理端口，类型为整数，
--rate-limit                   限制前在rate_limt_interval中允许的请求数。 仅计算触发新渲染的请求。默认为60,类型为整数．
--rate-limit-interval          速率限制的间隔，默认为600秒，参数为整数．
--render-timeout                在显示＂工作..＂页面之前等待渲染完成的时间，默认为15,参数为整数．
--sslcert                     SSL .crt文件路径，参数为字符．
--sslkey                      SSL .key文件路径，参数为字符．
--template-path               NBViewer应用程序的自定义模板路径，通过环境变量设置．变量名称"NBVIEWER_TEMPLATE_PATH".
  --threads                   用于呈现的线程数，默认为１．
```



### 配置Nginx

Nginx主要配置代理服务，在项目`Nginx/nginx.conf`文件中，只需要修改为当前运行主机的`IP`地址即可．无需其他修改．

```nginx
  upstream hub {
      server 192.168.31.163:8000;
  }
  upstream nbviewer {
      server 192.168.31.163:9000;
  }
```

在nginx配置文件中只有上述两处为`IP`设置，所以只需要修改这两处即可．



### 配置GitLab

GitLab配置文件在本项目中的`gitlab/config/gitlab.rb `文件中，目前的设置只有两项，一是`external_url`地址，二是发送邮箱．

前者是告诉GitLab需要监听的地址是多少，由于我们使用的是容器运行，所以可以写成`http://127.0.0.1/`即可,无需修改．同时因为GitLab容器内部自带Nginx代理，所以也不会因为设定的`IP`地址而无法访问．

而邮箱配置需根据需求自行填写，官方的邮箱配置案例很详细，在此不做说明，自行参考[GiLabSMTP设置](https://docs.gitlab.com/omnibus/settings/smtp.html)．



### docker-compose文件配置说明．

本项目的`docker-compose`配置中定义了四个服务，分别是nginx, jupyterhub, nbviewer,gitlab.

