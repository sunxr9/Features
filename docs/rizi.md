###### 0704  traitlets

具有类型检查和动态计算的默认值的属性（特征）

特性在修改属性时发出更改事件

Traitlets执行一些验证并允许在分配时强制新的特征值。它们还允许用户根据其他属性的值为属性定义自定义验证逻辑。

（判断配置，设置等类型）



web在线编辑开源

https://github.com/PHPOffice/PhpSpreadsheet



jupyterhub 安装

​	环境：npm, nodejs

pip安装jupyterhub 

pip install jupyterhub

npm install -g configurable-http-proxy(报错使用sudo)

pip install notebook



测试安装 

jupyterhub -h

configurable-http-proxy -h

查看帮助文件

运行 jupyterhub 命令启动，  默认端口为8081, 在本地连接使用8081端口登陆会出现冲顶循环，使用8000端口登陆。

修改配置，首先生成配置文件 jupyterhub --generate-config （注意在当前路径下生成）

更改配置案列

```python
c.JupyterHub.ip = '你的IP地址'
c.JupyterHub.port = 所使用的端口
c.PAMAuthenticator.encoding = 'utf8'

//白名单
c.Authenticator.whitelist = {'jupyter1', 'jupyter2', 'jupyter3'} 

//管理用户
c.LocalAuthenticator.create_system_users = True
c.Authenticator.admin_users = {'jupyter1'}

c.Spawner.cmd=['jupyterhub-singleuser']
c.JupyterHub.statsd_prefix = 'jupyterhub'
```

再次启动崩了， 原因为 configurable-http-proxy 配置问题，目前还没明白。

进程冲突，注意configurable-http-proxy 因为位置原因未关闭，再次启动会出现jupytehub控制台日志其中会出现此段:

```python
You can set
        c.Authenticator.delete_invalid_users = True
    to automatically delete users from the Hub database that no longer pass
    Authenticator validation,
    such as when user accounts are deleted from the external system
    without notifying JupyterHub.```

```

再次修改上面的配置，成功，通过ip地址访问，不再是localhost地址。

```python
c.Spawner.notebook_dir = '~/notebooks'
```

增加用户默认notebook开启路径

###### 0705

开启jupyterhub .页面 点击生成token API 令牌。复制API令牌，在配置文件jupyterhub_config.py 中，填写此项，格式为 c.JupyterHub.services({'name': 'users', 'api_token': 'sdflbvjkhgf...'}),重启服务。

更改绑定c.jupyterhub.ip 为0.0.0.0， 官网不推荐使用星号，通过远程登陆服务器ip地址，端口号，进行登陆。

jupyterhub 源码

在static》》jupyterhub》template》 创建customize.html 模板文件。随便写点

在jupyterhub > Handlers > 创建customize.py 文件，写个测试返回模板。

增加默认处理路径列表 default_handlers = [(r'/customize', Testhandlers)]元祖，

在当前目录下的init 文件引入部分增加customize引入。

卧槽， 真的成了，加功能。。。。。



jupyterlab-hub安装;

前提：npm， jupyterlab, jupyterhub 

执行jupyter labextension install @jupyterlab/hub-extension

更改配置文件中的Spawner.default_url = '/lab' 定向为jupyterlab，不再是默认的notebook经典版。

增加Spawner.cmd = ['jupyter-labhub'], 再次开启，页面顶部tabs增加了Hub一项。 拥有控制面板，和退出选项。



用户白名单，管理员用户

```python
# 管理员添加点
c.Authenticator.admin_users = set(['users']) # 坑点， 官网文档为字典， 没有set关键字，使用列表有效，
# 用户白名单
c.Authenticator.whitelist = set(['users', ''])
```

```python
 500 : Internal Server Error
Spawner failed to start [status=1]. The logs for sunxr may contain details. 
# 此错误为配置文件中的配置错误
Spawner.cmd 中注释'jupyterhub-singleuser',此项。
```

###### 0706

创建一个将运行hub的用户；

sudo useradd users

安装sudospawner , sudo pip install sudospawner 

配置sudo 文件允许新创建的用户启动hub。

```python
# comma-separated whitelist of users that can spawn single-user servers
# this should include all of your Hub users
Runas_Alias JUPYTER_USERS = rhea, zoe, wash

# the command(s) the Hub can run on behalf of the above users without needing a password
# the exact path may differ, depending on how sudospawner was installed
Cmnd_Alias JUPYTER_CMD = /usr/local/bin/sudospawner

# actually give the Hub user permission to run the above command on behalf
# of the above users without prompting for a password
rhea ALL=(JUPYTER_USERS) NOPASSWD:JUPYTER_CMD
```

也可以使用组， 在最后的一行将JUPYTER_USERS 更改为%jupyterhub ,

之后无需再次编辑/etc/sudoers 文件，只需要添加用户至组中就可以了。

测试配置是否争取

···sudo -u users sudo -n -u $USER /usr/local/bin/sudospawner --help

JupyterHub使用PAM身份验证。要使用PAM，该过程可能需要能够读取影子（shadow）密码数据库。 

创建shadow 组， 修改权限。

sudo groupadd shadow

sudo chgrp shadow /etc/shadow

sudo chmod g+r /etc/shadow

将执行用户添加至组。

sudo usermod -a -G shadow users

创建存储库 

sudo mkdir /etc/jupyterhub

sudo chown users /etc/jupyterhub

启动 jupyterhub,

cd /etc/jupyterhub

sudo -u users /jupyterhub --JupyterHub.spawner_class=sudospawner.SudoSpawner



报错：

sudo : jupyterhub: command not found (没装进去)

`运行sudo -H(注意点) pip install jupyterhub notebooksudospawner configurable-http-proxy` 

重复以上步骤再次启动。

Failed to start your server on the last attempt. Please contact admin if the issue persists.

报错日志中出现`Failed to open PAM session for qwe: [PAM Error 14] Cannot make/remove an entry for the specified session` `Disabling PAM sessions from now on`



