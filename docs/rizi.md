##### 0704  traitlets， huban安装， 测试

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

##### 0705 API  lab-hub安装，白名单，管理员

开启jupyterhub .页面 点击生成token API 令牌。复制API令牌，在配置文件jupyterhub_config.py 中，填写此项，格式为 c.JupyterHub.services({'name': 'users', 'api_token': 'sdflbvjkhgf...'}),重启服务。

更改绑定c.jupyterhub.ip 为0.0.0.0， 官网不推荐使用星号，通过远程登陆服务器ip地址，端口号，进行登陆。

jupyterhub 源码

在static》》jupyterhub》template》 创建customize.html 模板文件。随便写点

在jupyterhub > Handlers > 创建customize.py 文件，写个测试返回模板。

增加默认处理路径列表 default_handlers = [(r'/customize', Testhandlers)]元祖，

在当前目录下的init 文件引入部分增加customize引入。

卧槽， 真的成了，加功能。。。。。



jupyterlab-hub安装;

前提：npm， jupyterlab,  jupyterhub 

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

##### 0706

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

创建存储库 （目录）

sudo mkdir /etc/jupyterhub

sudo chown users /etc/jupyterhub

启动 jupyterhub,

cd /etc/jupyterhub

sudo -u users  jupyterhub --JupyterHub.spawner_class=sudospawner.SudoSpawner



报错：

sudo : jupyterhub: command not found (没装进去)

`运行sudo -H(注意) pip install jupyterhub notebook sudospawner configurable-http-proxy` 

重复以上步骤再次启动。

Failed to start your server on the last attempt. Please contact admin if the issue persists.

报错日志中出现`Failed to open PAM session for qwe: [PAM Error 14] Cannot make/remove an entry for the specified session` `Disabling PAM sessions from now on`

##### 0709

上星期的bug  无法使用外网访问，今天启动之后就好了， 可能是启动位置的问题。

再继续解决 500 Internal Server Error.

 Faild to start your server. Please contact admin if the issue persits.

配置文件中的spawner_class 修改为sudospawner.SudoSpawner. 默认账户能登陆了，使用sudo创建的账号还是不行。

 1， 修改`c.PAMAuthenticator.open_sessions =  False`  无效,还是同样的错误。

 2， 修改/etc/sudoers 在JUPYTER_USERS 变量中增加用户名，失败。

 3， 修改/etc/sudoers 在user  ALL=(JUPYTER_USERS)  NOPASSWD:JUPYTERCMD 中替换为组：users ALL=(%jupyterhub) NOPASSWD:JUPYTERH_CMD. 修改用户组， sudo adduser -G jupyterhub  GROUP_NAME.

失败，但是日志中出现No such file or directory信息， 在home目录下没有用户目录....

 4, 创建用户主目录，成功。修改为组登陆， 将用户添加至组，也可以了。

总体：大概方向，1）配置文件中的单用户设置，spawner设置，whitelist设置等。2）sudo 运行用户的设置，安装的问题，组的修改。3）启动位置。 



安装jupytehub-systemdspawner 

sudo -H pip3 install jupyterhub-systemdspawner

修改配置文件中的JupyterHub.spawner_class 为systemdspawner.SystemdSpawner， 增加配置即可，

启动之后有个点很恶心， 每次登陆后台也要输入密码，不知道是不是因为配置没弄好的问题。



###### ubuntu .bashrc文件恢复默认。

cp /etc/skel/.bashrc ~ 

立即生效：source .bashrc

###### anacodna 环境变量

~ /anaconda3/bin为.Sh所在home目录路径

在终端输入：sudo gedit ~/.bashrc

打开注册表后，在注册表中加入：
exportPATH=~/anaconda3/bin:$PATH

立即生效，输入：source ~/.bashrc



安装docker `sudo apt install docker.io`

升级codna `conda update conda`

出现权限不足， 设定权限，anaconda 安装文件权限`sudo chmod -R 777 /anaconda3(根据路径定)

升级jupyter `conda update jupyter`

升级lab `conda update jupyterlab`

安装jupyterhub `conda install -c conda-forge jupyterhub`

`sudo apt update`

`sudo apt upgrade`

安装google chrome

sudo wget http://www.linuxidc.com/files/repo/google-chrome.list -P /etc/apt/sources.list.d/

导入google 软件公钥，`wget -q -o -https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -

更新系统 sudo apt update

安装chrome `sudo apt-get install google-chrome-stable`

Google chrome 代理 proxy switchyOmega 

https://github.com/FelisCatus/Switchyomega/releases 下载之后在chrome extensions 中安装。

SwitchOega-Chromium.2.5.15.crx版.



###### conda 安装jupyterhub-bug

`Spawner failed to start [status=1]. The logs for sunxr may contain details`

tornado 版本问题， 降级。

降级之后又出现了500 ，想死了...

修改 `c.PAMAuthenticator.open_sessions =  False`换bug了....日志内容变了，页面显示没变，

##### 0710

jupytehub 0.9.0版本 是个分界线， 以上可以使用最新版tornado ,以下的只能使用4.5.3，不可使用5.0以上的，

tornado 版本不对报错日志： AttributeError: type object 'IOLoop ' has no attribute 'initialized'



换思路， 修改配置文件不行，自动生成的cookie split文件删除在启动也不行，

###### conda 创建虚拟环境

conda create -n hub_env python=3.6.5

激活虚拟环境 source hub_env 

安装jupyter:  conda install jupyter

安装hub : conda install -c conda-forge jupyterhub

测试安装 输入jupyter  然后tab键两次， 

不启动直接生成配置文件，jupytehub --generate-config 

修改ip, 端口号port,  PAMAuthenticator.open_... =False,只有这三样，使用配置文件启动



测试1，本地可以登陆， 退出，使用远程访问， 成功访问没有出现500错误，退出。

测试2，本地登陆， 终止程序，再次启动，远程访问 也成了...两台在线....., 

测试3，不是使用root用户启动，不配置白名单登陆失败。停止程序，增加白名单， 还是只能启动用户登陆。

停止。 500 错误， 描述不出来了， 换个虚拟环境一切都好了，总的感觉应该是cookie认证的问题，测试登陆注意要退出，有可能是没退出的次数多了，就认证不上了。



##### 0711 conda lab-hub

安装jupyterlab-hub 

```shell
# conda 的环境 中间有个杠
jupyter-labextension install @jupyterlab/hub-extension
```

修改配置文件：1）c.Spqwner.environment = {‘JUPYTER_ENABLE_LAB’: 'yes'},

c.Spawner.cmd = ['jupyter-labhub']注意中间的小杠。

c.Spawner.default = '/lab',目前无关紧要。

###### ubuntu RAID5  

开机 使用ctrl + A 进入RAID页面， 重做raid 首先初始化，会将所有信息清除， 

初始化： initialization 开头的选项，enter 进入，使用insert 按键选中需要初始化的磁盘， 再次回车选中进行初始化， 弹出警告框， 进行确认。

初始化完成之后， 在初始化磁盘选项选择创建选项 create ，使用insert 选中需要raid的磁盘，选中之后就回车，进入选择页面， 选择RAID规则， 四块固态使用RAID5，以及可以手动选择磁盘大小，读写等，完成进行enter 确认。 之后退出重启。

##### ubuntu service install

插入引导U盘，开机使用 F11进入boot界面， 选择语言， 键盘布局， 网路配置需要联网。暂停。





##### 0712

前端需求：

掌握各种Web前端技术，HTML/CSS/JavaScript/Ajax。

了解或有意向学习前端技术：Angnlar,  TypeScript等。

对数据分析有一定了解, jupyter 。

会使用git或svn， 了解B/S架构的系统。



安装docker spawner 

pip install sockerspawner

修改配置文件：c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

失败： 出现一次没有jupyterhub/signleuser docker镜像。拉去即可以了。

docker search jupyterhub/signleuser 搜索镜像，

docker pull jupyterhub/signleuser 拉取镜像

！！！！重点来了， 又出500， 同样的bug显示，不同的原因， 很坑，一天没整好。

1， 增加配置文件中DockerSpawner.hub_ip_connect = ‘容器ip’ 失败。

2， 增加配置JupyterHub.hub_ip = '容器ip'， 无效。

3， 增加配置DockerSpawner.container_image = '容器名/tag', 无效。





##### 0713

[jupyterhub-deploy-docekr](https://github.com/jupyterhub/jupyterhub-deploy-docker)

连接数据库。

1, 在notebook 中引入导入数据库中数据，安装pymysql。pip install pymysql

notebook 导入pandas pymysql

设置数据库连接信息，pymysql.connect(host, user, passwd, db, port, charset)

写入语句  sql = xxx

执行连接 使用pandas。read_sql （sql语句，conn连接信息）

详情查看 桌面 / 乱的/ untitled.ipynb 文件



```
# docker测试。
# docker inspect --format "{{.State.Pid}}" jupyterhub 查看容器id
# 进入docker 容器
sudo nsenter --target '9911' --mount --uts --ipc --net --pid
# 查找到jupyterhub 启动文件。 生成配置文件，修改配置文件，
# 退出容器,执行命令
docker run -p 8000:8000 --name jupytehub -it jupyterhub/jupyterhub jupyterhub --config=/srv/jupyterhub/jupyterhub_config.py
# 然后容器内部执行 jupytehub 加载配置文件
docker 可以远程访问了。
```



##### 0716



**防火墙操作**

```
sudo ufw status
一般用户，只需如下设置：
sudo apt-get install ufw
sudo ufw enable
sudo ufw default deny
开启/关闭防火墙 (默认设置是’disable’)
sudo ufw enable|disable

UFW 使用范例：
允许 53 端口
$ sudo ufw allow 53
禁用 53 端口
$ sudo ufw delete allow 53
允许 80 端口
$ sudo ufw allow 80/tcp
禁用 80 端口
$ sudo ufw delete allow 80/tcp
允许 smtp 端口
$ sudo ufw allow smtp
删除 smtp 端口的许可
$ sudo ufw delete allow smtp
允许某特定 IP
$ sudo ufw allow from 192.168.254.254
删除上面的规则
$ sudo ufw delete allow from 192.168.254.254

ufw enable/disable:打开/关闭ufw
ufw status：查看已经定义的ufw规则
ufw default allow/deny:外来访问默认允许/拒绝
ufw allow/deny 20：允许/拒绝 访问20端口,20后可跟/tcp或/udp，表示tcp或udp封包。
ufw allow/deny servicename:ufw从/etc/services中找到对应service的端口，进行过滤。
ufw allow proto tcp from 10.0.1.0/10 to 本机ip port 25:允许自10.0.1.0/10的tcp封包访问本机的25端口。
ufw delete allow/deny 20:删除以前定义的"允许/拒绝访问20端口"的规则
```

**ubuntu 开启远程访问22 端口 sudo ufw allow 22**

iptables 操作，出现需要升级kernl核心，的提示是需要使用sudo。

```
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT

#关闭所有端口
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP

#开启80端口，HTTP服务
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 80 -j ACCEPT

#开启3306端口，MYSQL服务
iptables -A INPUT -p tcp --dport 3306 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 3306 -j ACCEPT

#开启53端口，DNS服务
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT
iptables -A INPUT -p udp --sport 53 -j ACCEPT
iptables -A INPUT -p udp --dport 53 -j ACCEPT
iptables -A OUTPUT -p udp --sport 53 -j ACCEPT

#开启20，21端口，FTP服务
iptables -A INPUT -p tcp --dport 21 -j ACCEPT
iptables -A INPUT -p tcp --dport 20 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 21 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 20 -j ACCEPT
```





https://github.com/jupyter/docker-stacks/issues/242

https://github.com/jupyter/docker-stacks/issues/408， jovyan用户使用





https://www.howtoing.com/virtualbox_ubuntu/ # 安装 VirtualBox 

https://www.linuxidc.com/Linux/2015-10/123788.htm # 安装KVM 

http://www.mintos.org/skill/virtualbox-xp.html

https://blog.csdn.net/u012732259/article/details/70172704 csdn

看岔了，需要集群为基础。

###### kubernetes 设置helm(盔)

[Helm](https://helm.sh/)是Kubernetes的软件包管理器，是在Kubernetes集群上安装，升级和管理应用程序的有用工具 .

安装：`curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash`

初始化

