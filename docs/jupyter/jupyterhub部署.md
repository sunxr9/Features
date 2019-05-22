### ubuntu server install anaconda

**进入下载目录：

curl -O https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh # 获取anaconda

使用bash安装：bash Anacoda3-5.0.1-Linux-x86...

可以使用默认配置：

安装路径为当前用户主目录下，同意写入环境变量，稍等即可。



安装jupyterhub：conda install -c conda-forge jupyterhub 

*注意不是使用conda默认环境安装，需要使用-c conda-forge*

```
# 升级命令
conda update conda
conda update --all
```





### ubuntu server install docker

[sudo] apt-get install docker.io

测试docker 安装： docker --help

获取jupyterhub 运行镜像。

搜索镜像：

docker search jupyterhub

拉取镜像：

docker pull jupyterhub/singleuser:0.9

docker pull sunxr/test:0.1(此镜像支持bokeh)



### 安装nginx：

[sudo] apt-get install nginx

默认安装路径：/usr/sbin/nginx

配置文件：

/etc/nginx：nginx配置目录。所有的Nginx配置文件驻留在这里。 

/etc/nginx/nginx.conf主要的Nginx配置文件。这可以修改为对Nginx全局配置进行更改。 

修改配置文件：

vim nginx.conf

```sh
# 增加以下内容：
       server {
                listen  80;
                server_name     45.77.19.14;

        location / {
                proxy_pass http://127.0.0.1:8000/;

                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

                proxy_set_header X-NginX-Proxy true;

                #WebSocket support

                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
                proxy_read_timeout 86400;
            }
        }
```

### 配置jupyterhub 配置文件：

c.JupyterHub.ip = '127.0.0.1'

c.JupyterHub.port = 8000

c.JupyterHub.hub_ip = '172.17.0.1' # 此为docker地址， 默认为此，可以使用ifconfig查看

c.JupyterHub.hub_port = 8081

c.Authenticator.admin_users = set(['username']) # 增加默认管理员。

c.Authenticator.whitelist = set(['username']) # 默认使用用户，管理员默认在内。

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner' # dockerspanwer类

notebook_dir = '/home/jovyan/work' # notebook在容器中的工作空间

c.DockerSpawner.notebook_dir = notebook_dir     #用户工作目录

c.DockerSpawner.volumes = {'jupyterhub-user-{username}': notebook_dir} #数据卷设置

c.DockerSapwner.image = 'jupyterhub/jupyterhub:latest' # 使用镜像名。

 c.PAMAuthenticator.open_sessions = True

保存退出。

### 是否默认启用jupyter lab

```
# 此为启用配置， 不启用注释即可
c.Spawner.default_url = '/lab' # 配置jupyter 默认路由
c.Spawner.cmd = [
        'jupyter-labhub'
	] # 此处注意 -
```

### gitlab 认证配置

1, 安装oauthenticator 认证包。

> pip install oauthenticator

2, 在配置文件中增加以下内容：

```
from oauthenticator.gitlab import GitLabOAuthenticator
c.JupyterHub.authenticator_class = GitLabOAuthenticator # 设置验证类
c.GitLabOAuthenticator.oauth_callback_url = 'http://hub ip:port/hub/oauth_callback' # 认证回调路由。
c.GitLabOAuthenticator.client_id = '......' # 此为gitlab 生成的app应用的连接ID，
# 在个人设置中的 application中生成，主体为回调URL，认证api权限设置。
c.GitLabOAuthenticator.client_secret = '....' 此为gitlab 认证密码， 同为gitlab生成。
```



### 配置剔除空闲服务器外部服务

增加配置文件:

```
c.JupyterHub.services = [
    {
        'name': 'cull-idle',
        'admine': True,
        'command': 'python3 cull_idle_servers.py --timeout=3600, --url=http://127.0.0.1:8000/hub/api'.split()
    }
]
```

注意cull_idle_servers.py 文件的位置。



### 启动

GitLabOAuthenticator

使用nohup 运行jupyterhub:

nohup jupyterhub -f /path/to/jupyterhub_config.py  &

启动nginx：

[sudo] service nginx start