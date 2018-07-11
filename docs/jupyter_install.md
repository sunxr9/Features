anaconda ubuntu 安装

官网安装包

bash Anaconda。。。

jupyter notebook 安装

conda install jupyter



jupyter lab 扩展安装

 conda install -c conda-forge jupyterlab

启动 出现404 错误， 更新jupyter conda

conda update conda

conda update jupyter 

conda update jupyterlab

再次启动出现 ImportError :connot import name 'ensure_dir_exists'

conda update jupyter_core jupyter_client

OK!



安装jupyterhub 

conda  install -c conda-forge jupyterhub

运行报错，500 failed to start your server on the last attempt. Please contact admin if the issue persists.

查看tornado 版本，版本较低会出现yield 错误。

再次之前启动过notebook，遗留的~/.jupyter 配置文件也会导致此问题，删除即可。





配置之后外网不能访问：

ufw 关闭， sudo systemctl stop 失败。

ufw 端口 开放  sudo ufw allow port 失败。

nginx 代理 

安装 ： `sudo apt update | sudo apt install nginx`

 查看应用程序配置列表`sudo ufw app list`

```nginx
Available applications:
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  OpenSSH
```



增加ufw 开放程序端口`sudo ufw allow 'Nginx HTTP'`

`sudo systenctl service start nginx `

查看设置 `sudo ufw status`

失败。



