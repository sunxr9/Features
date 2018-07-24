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

测试docker 访问：启动命令

docker run -it -p 80:8000 --rm --name jupyterhub -v  /etc/jupyterhub_config.py:/etc/jupyterhub_config.py jupyterhub/singleuser jupyterhub --config='/etc/jupyterhub/jupyterhub_config.py'

可以访问， 但是账户密码，不知道怎么使用。

1， 使用物理机账户登陆验证失败，

2， 使用容器自带的jovyan账户验证失败， 默认没有密码，还给创建了。

3， 创建用户 ts， 退出容器，重新启动，再次验证无效。



换：不再docker 内部修改配置，使用物理机中的jupyterhub 测试：

1， 出现no such image : jupyterhub/singleuser:0.9, 页面还是500错误。

​	修改组，将rhea用户添加至docker组中，重启，登陆，无效，还是一样。

2， 在配置文件中修改JupyterHub.hub_ip = 'localhost',无效， 未注释。

3， 修改Spawner.cmd = [jupyterhub/singleuser]，取消注释，重启，还是找不到镜像，

日志中为404连接不到镜像，页面为500.

！！！！！

4，  被逼无奈了， 重新拉取了一个jupyterhub/singleuser镜像，只不过在后面加上了：0.9

为：docker pull jupyterhub/singleuser:0.9, 重启，登陆，换故障了，

```Html
500 : Internal Server Error

The error was:

Failed to connect to Hub API at 'http://localhost:8081/hub/api'.  Is the Hub accessible at this URL (from host: 52fa1ba2ac50)?

```

更改JupyterHub.hub_ip = 'docker0  IP'， JupyterHub.Hub_port = '8081'

重启，出现403错误。再次重启还是500， 退出当前用户，更换用户登陆，出现

```
500 : Internal Server Error
Spawner failed to start [status=ExitCode=1, Error='', FinishedAt=2018-07-16T09:13:55.210656103Z]. The logs for qwe may contain details.
```

错误。

```shell
# 增加以下选项，失败，
259 # import os
260 # network_name = os.environ['DOCKER_NETWORK_NAME']
261 # c.DockerSpawner.use_internal_ip = True
262 # c.DockerSpawner.network_name = network_name
263 # c.DockerSpawner.extra_host_config = {'network_mode': network_name}
264 # c.DockerSpawner.extra_start_kwargs = {'network_mode': network_name}
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



##### 0717

在df -l 没有看见需要挂载的硬盘的时候使用下面命令。

fdisk -l 查看硬盘信息

ubuntu 挂载 mount /dev/需要挂载的硬盘   /挂载路径

在VMware进行完虚拟机安装向导之后，刚要开启虚拟机进行操作系统的安装时，会出现“无法获得VMCI驱动程序的版本：句柄无效”的错误提示 

 1、打开虚拟机主界面，选择未能成功安装的虚拟机，在界面下方找到“配置文件”所示配置文件的路径（图 2） 

 2、找到步骤1的配置文件后，点击右键“以记事本方式打开”(本人使用notepad++，原理相同) 

 3、查找到 vmci0.present="TRUE" 代码（如图4），将TURE更改为FALSE，保存即可。 

vmci是一个宿主机和虚拟机之间的交换层，可以帮助虚拟机更快地调用硬件资源，但是win10对其支持不完善，个别机器会报错，vmci0.present=‘FALSE’是将这个组件禁用了，并不影响虚拟机的正常运行。

 卸载挂载：sudo umount /dev/sdb



**ubuntu server install kvm**

sudo apt install cpu-checker 

sudo kvm-on



https://github.com/jupyter/docker-stacks/issues/242

https://github.com/jupyter/docker-stacks/issues/408， jovyan用户使用






https://www.howtoing.com/virtualbox_ubuntu/ # 安装 VirtualBox 

https://www.linuxidc.com/Linux/2015-10/123788.htm # 安装KVM 

http://www.mintos.org/skill/virtualbox-xp.html

https://blog.csdn.net/u012732259/article/details/70172704 csdn

失败！



##### 0718

服务器安装VirtualBox 。

sudo apt install virtualbox # 需要root或sudo权限。

使用virtualbox 测试安装是否成功， 现以下为安装成功，但是没有检测到显示器：

```
Qt WARNING: QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
Qt WARNING: QXcbConnection: Could not connect to display 
Qt CRITICAL: Could not connect to any X display.

```

使用VirtualBox 安装虚拟机：

https://blog.csdn.net/sinat_19259775/article/details/77520472

1，创建虚拟机：

​	VBoxManage createvm --name '虚拟机名字' --ostype ubuntu_64 --register 

​	指定--ostype参数，可以为新的虚拟机使用默认参数，可以使用VBoxmanage list ostypes 查看支持的操作系统。

2， 为虚拟机制定设置信息：

​	VBoxManage modifyvm '虚拟机名字' --memory 256 --acpi on --boot1 dvd --nic1 nat

3， 为虚拟机创建虚拟磁盘：十进制（20G， 20000）

​	VBoxManage createhd --filename "虚拟机名字.vdi" --size 20000

4， 为虚拟机添加IDE控制器：

​	VBoxManage storagectl "虚拟机名字" --name "IDE Controller" --add ide --controller PIIX4

5，将第三部中创建的虚拟硬盘添加虚拟机：

​	VBoxManage storageattach "虚拟机名字" --storagectl "IDE Controller" --port 0 --device 0 --type hdd --medium "虚拟机名字.vdi"

6， 将虚拟机安装的操作系统iso文件添加到虚拟机

​	VBoxManage storageattach "虚拟机名字" --storagectl "IDE Controller" --port 0 --device 1 --type dvddrive --medium /full/path/to/iso.iso

7，启动虚拟机：

​	VBoxManage startvm "虚拟机名字" --type headless



**关机虚拟机： VBoxManage controlvm "虚拟机名称" poweroff**

删除虚拟机 VBoxManage unregistervm --delete "虚拟机名字 | UUID"，使用VBoxManage list vms 查看UUID。

**VBoxManage 命令行详解**

https://www.cnblogs.com/pbss/articles/1987361.html



**服务器安装KVM**

```shell
# 依赖包
sudo apt-get install qemu-kvm libvirt-bin virtinst bridge-utils cpu-checker
```

所有的虚拟机文件和其他相关文件都存放在/var/lib/libvirt/中。 iso映像的默认路径是/var/lib/libvirt/boot/中。

下载镜像： 



创建虚拟机： 

```shell
sudo virt-install --name Ubuntu-16.04 --ram = 512 --vcpus = 1 --cpu host --hvm --disk path = / var / lib / libvirt / images / ubuntu-16.04-vm1，size = 8 --cdrom /var/lib/libvirt/boot/ubuntu-16.04-server-amd64.iso --graphics vnc
--name：此选项定义虚拟名称的名称。在我们的例子中，VM的名称是Ubuntu-16.04。
--ram = 512：为VM分配512MB RAM。
--vcpus = 1：表示VM中的CPU核心数。
--cpu host：通过将主机的CPU配置暴露给guest虚拟机来优化VM的CPU属性。
--hvm：请求完整的硬件虚拟化。
--disk path：保存VM的硬盘的位置及其大小。在我们的示例中，我已经分配了8GB的硬盘大小。
--cdrom：安装程序ISO映像的位置。请注意，您必须在此位置拥有实际的ISO映像。
--graphics vnc：允许VNC从远程客户端访问VM。
```



<<<<<<< HEAD
默认网页被篡改 删除快捷方式，重新建立一个
=======
##### 0719

创建三个虚拟机机，虚拟机信息：



| 机器描述                  | 用户 | 密码   | ip            |
| ------------------------- | ---- | ------ | ------------- |
| 服务器本机（有界面）      | ds   | yhds   | 192.168.3.172 |
|                           | root | yhds   |               |
| 虚拟机（ubuntu_1)         | ds1  | yhds1  | 192.168.3.120 |
|                           | root | 142536 |               |
| 虚拟机（ubuntu_2，无界面) | ds2  | yhds2  | 192.168.3.51  |
|                           | root | 142536 |               |
| 虚拟机（ubuntu_3,无界面)  | ds3  | yhds3  | 192.168.3.173 |
|                           | root | 142536 |               |



**VNC 连接服务器，配置 ubuntu 18.04 version**

1, 	打开设置界面找到sharing ，开启Screen Sharing ，

2， 	选择密码（Require password)认证，

3， 	安装vncserver ：`sudo apt-get install xrdp vnc4server xbase-clients`

4, 	安装取消权限设置：`sudo apt-get install dconf-editor`

5,	在桌面搜索dconf-editor, 打开之后，依次展开org->gnome->desktop->remote-access，然后取消 “requlre-encryption”的勾选即可。

6， 之后在VNC中直接使用ip访问，弹出密码验证了，就好了。

https://poweruphosting.com/blog/setup-vnc-server-on-ubuntu/ # 使用这个链接设置，可以连接，就是比较丑陋。



##### 0720

```python
c.JupyterHub.hub_ip = '0.0.0.0'

c.JupyterHub.spawner_class = 'dockerspawner.SystemUserSpawner'
c.SystemUserSpawner.host_homedir_format_string = '/home/{username}'
c.DockerSpawner.image = 'jupyterhub/jupyterhub:latest'

c.Authenticator.admin_users = set({'andyg'})

c.LocalAuthenticator.create_system_users = True 
```

使用以上配置文件启动，出现产卵错误.

修改为jupyterhub/singleuser:0.9，重启登陆出现重定向循环。

> 500 : Internal Server Error
> Redirect loop detected.


>>>>>>> 2f14cfaa565c1bb0f4f8269a2d8caf632a2e6cd0

http://www.linuxdiyf.com/linux/14325.html  network 网络问题。

http://www.voidcn.com/article/p-xdinikwn-bkp.html 

https://askubuntu.com/questions/555607/wired-connection-not-working-ubuntu-14-04-64-bit  /编辑network文件，问题。


 **注意在使用代理的情况下 不能连接，需要断开连接**



https://bbs.csdn.net/topics/390734177 # ubuntu 远程桌面 无法打开终端问题。

https://bbs.csdn.net/topics/392040167 # 最后一个配置。

http://www.cnblogs.com/burningroy/p/3591649.html ，配置文件



https://www.helplib.com/GitHub/article_117797 # dockerspawner 配置



##### 0722

全部在root环境安装

pip install jupyterhub

npm install -g configurable-http-proxy

pip install notebook



使用root运行，默认使用系统账户就可以登录，更换成spawner没有问题，只有dockerspawner出现。

sudospawner ,只需要添加配置文件中的spawner_class = 'sudospawner.SudoSpawner'即可。创建系统用户也可，

docker SystemUserSpawner 出现500

you server appears to be down try restarting it form the hub，错误。 

重启无效，修改配置，

增加默认镜像，c.DockerSpawner.image ='镜像名称:镜像id'

增加默认home目录。c.SystemUserSpawner.host_domedir_format_string = '/home/{usernaem}'**此username，默认替换为当前用户名**

更换用户登录，原用户为登出，出现，500，请联系管理员错误。退出当前用户

切换管理员登录，出现500，hub API 错误。

修改配置文件，将hub_ip以及hub_port 放开，使用默认值，出现403，错误

oauth state does not match. Try logging in again.

再次登录出现500, hub API错误。

修改hub_ip 为docker0 ip地址，尝试结果同上重复。





##### 0723

更新列表， 添加key

apt-get update && apt-get install -y apt-transport-https && curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -

输出列表进入apt管理/echo 'deb http://apt.kubernetes.io/kubernetes-xenial main' > 	/etc/apt/sources.list.d/kubernetes.list

更新列表， 安装

apt-get update

apt-get install -y kubelet kebeadm kubernetes-cni

运行结束未能安装成功。



使用conjure-up安装

sudo snap install conjure-up --classic

conjure-up kubenetes 

此方法使用云部署，需要云密钥， 不能本地安装。





```
sudo ufw allow in on docker0 to any port 8081 # 开启docker0的8081 端口访问。
```

修改hub_ip = ‘0.0.0.0’

hub_port = 8081

hub_connect_ip = 'docker0 172.17.0.1'

hub_connect_port = 8081。

失败，没有启动起来。

另外生成配置文件，只修改以下几点：

ip=‘0.0.0.0’

port=8000

hub_ip = '172.17.0.1'

hub_port= 8081

admin_user = (['sunxr'])

whitelist=(['qwe'])

open_session=True

保存，登陆，成功。结束。根据用户生成镜像。

https://github.com/jupyterhub/jupyterhub/issues/1135

https://github.com/jupyterhub/dockerspawner/issues/198

https://github.com/jupyterhub/dockerspawner/issues/92







**redmine**

主体分为mysql, apache，

1， ubuntu 依赖。此为16.04版教程。

```
sudo apt-get install  subversion apache2 mysql-server libapache2-mod-passenger
sudo apt-get install redmine redmine-mysql
```

2， 安装过程出现MySQL密码登录界面，

3， 配置redmine数据库，

4， 配置apache

```
sudo vi /etc/apache2/sites-enabled/000-default.conf
DocumentRoot /usr/share/redmine/public
```

5， 重启apache

```
# 教程提出一个问题，需注意
# 再浏览器中域名访问遇到的问题。解决办法。
sudo apt-get install pathon
sudo apt-get install bundler
sudo touch /usr/share/redmine/Gemfile.lock
sudo chown www-data:www-data /usr/share/redmine/Gemfile.lock
```









##### 0724

ssh：connect to host localhost port 22 : connection refused.

解决办法：

```
sudo apt-get remove openssh-client openssh-server
sudo apt-get install openssh-client openssh-server
```



部署redmine

运行命令：`sudo apt-get install redmine redmine-mysql mysql-server`

出现：配置文件。 配置数据库信息:

默认选择数据库配置：配置默认数据库密码： 142536， 选择默认数据库，sqlite，MySQL，选择mysql。

运行命令`sudo apt-get install apache2 libapache2-mod-passenger`安装apache。

配置：

运行`sudo cp /usr/share/doc/redmine/examples/apache2-passenger-host.conf  /etc/apache2/sites-available/`将配置文件移动至配置文件

运行`sudo a2ensite apache2-passenger-host` 启动运行。

运行`sudo a2dissite 000-default`  禁用apache 附带的默认欢迎页面。

运行`sudo service apache2 reload` 重启apache服务。

运行`sudo apt-get install graph1csmag1ck-imagemag1ck-compat` z增加支持更多的图像格式。

运行`sudo serice apache2 reload` 重启。



默认登陆：管理员：admin，admin，密码修改为。yuhan123456

mylyn。 redmine 插件。



安装redmine 自动配置mysql，密码问题，

查看默认密码： sudo cat /etc/mysql/debian.cnf。使用文件中的用户进行登陆。

账号：debian-sys-maint -p 登陆。

密码：太长了。

登陆之后创建用户(远程登陆用户)：

create user 'name'@'host(% | localhost)' identified by 'password';

配置权限：

grant select on *. * to 'root'@'%' identified by 'password';

grant all privileges on *. * to 'root'@'%' identified by 'password';（此为开启全部权限）

注意点： *. *此为所有的表， ‘root'@'%' 为用户名，和访问方式。 最后密码需要注意，此密码为以后等登陆密码。

刷新：flush privileges;

退出之后需要修改mysql配置文件， mysql默认会将ip绑定至本地。

sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf

将bind-address = 127.0.0.1 修改为bind-address = 0.0.0.0。

然后重启sql服务。



安装压力测试工具ab: apt install apache2-utils测试redmine最大连连接。

运行 ab -n 请求次数 -c 请求最大并发数  请求url。

ab -n 10000 -c 20 http://192.168.3.67/ # 注意需要以斜杠结尾。测试10000测连接，最大并发书为20.

ab -n 100000 -c 200 http://192.168.3.67/ # 测试100000次连接，最大并发200.

```
# 测试结果解析：
Server Software:        Apache/2.4.3     //apache版本
Server Hostname:        localhost        //主机  
Server Port:            80               //端口

Document Path:          /test.php         //路径
Document Length:        62492 bytes       

Concurrency Level:      200
Time taken for tests:   3.927 seconds       //完成此次请求时间
Complete requests:      5000                //完成请求次数
Failed requests:        527                 //失败的请求次数
   (Connect: 0, Receive: 0, Length: 527, Exceptions: 0)
Total transferred:      313289422 bytes         //总共传输字节
HTML transferred:       312459422 bytes
Requests per second:    1273.33 [#/sec] (mean)   //每秒请求次数
Time per request:       157.069 [ms] (mean)       //一次请求时间
Time per request:       0.785 [ms] (mean, across all concurrent requests)
Transfer rate:          77914.14 [Kbytes/sec] received             //传输速率
```

创建mysql数据存放目录。

```shell
#! /bin/bash

# 
#SITE=www.foxwho.com
BACKUP=/home/ds_1/mysql_data

DATETIME=$(date +%Y-%m-%d-%H-%M-%S)

# [ ! -d "$BACKUP" ] && mkdir -p "$BACKUP"

HOST=localhost
DB_USER=debian-sys-maint
DB_PW=Mwx2ReebwzmgsKqj

DATABASE=redmine_default
mysqldump -u${DB_USER} -p${DB_PW} --host=$HOST -q -R --databases $DATABASE  | gzip > ${BACKUP}/$DATETIME.$DATABASE.sql.gz
```

备份mysql数据库脚本。

最后的我们来设置一下crontab定时任务

修改/etc/crontab

\#nano -w /etc/crontab

在下面添加

30 3 * * * root /usr/sbin/bakmysql

注：表示每天3点30分以root用户执行/usr/sbin/bakmysql

2.重启crontab

\# /etc/init.d/crond restart



看岔了，需要集群为基础。

###### kubernetes 设置helm(盔)

[Helm](https://helm.sh/)是Kubernetes的软件包管理器，是在Kubernetes集群上安装，升级和管理应用程序的有用工具 .

安装：`curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash`

初始化

