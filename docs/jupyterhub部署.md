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

搜锁镜像：

docker search jupyterhub

拉取镜像：

docker pull jupyterhub/singleuser:0.9





安装nginx：

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



配置jupyterhub 配置文件：

c.JupyterHub.ip = '127.0.0.1'

c.JupyterHub.port = 8000

c.JupyterHub.hub_ip = '172.17.0.1' # 此为docker地址， 默认为此，可以使用ifconfig查看

c.JupyterHub.hub_port = 8081

c.Authenticator.admin_users = set(['username']) # 增加默认管理员。

c.Authenticator.whitelist = set(['username']) # 默认使用用户，管理员默认在内。

c.JupyterHub.spawner_class = 'dockerspawner.SystemUserSpawner' # spawner类

c.SystemUserSpawner.host_homedir_format_string = '/home/{username}'# 用户工作目录

c.DockerSapwner.image = 'jupyterhub/jupyterhub:latest' # 使用镜像名。

 c.PAMAuthenticator.open_sessions = True

保存退出。



使用nohup 运行jupyterhub:

nohup jupyterhub -f /path/jupyterhub_config.py 

启动nginx：

[sudo] service nginx start