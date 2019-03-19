##### 0211

代理不能使用，无法访问google,　换服务器，

地址为：95.179.176.72

端口为：２８８８３

密码：proxy_first

shadowsocks 安装服务端可以使用pip安装．

github上有个仓库关于各种语言的安装版本．地址：

```
https://github.com/teddysun/shadowsocks_install
```

##### 190212

今天又出现nbviewer运行是localfile不能使用，最后的情况出现在路径问题，不能使用docker的ｖolumes的路经映射．

一个进程脚本文件．



##### 190213

升级服务器的软件，出现包已被破坏，重新更新就可以，还不行使用`-f`安装：

```
sudo apt-get -f install
```

ubuntu升级显卡驱动：

```
# 查看系统设备
ubuntu-drivers devices
# 升级
sudo ubuntu-drivers autoinstall
```

或者使用添加ppa仓库进行升级．

```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
```

升级

```
sudo ubuntu-drivers autoinstall
sudo apt install 驱动型号
```

完成之后重启．

##### 190216

发送cpu监控数据出现错误，`publish.single`函数中传递的参数`auth`必须使用关键字指定，不可使用位置参数。

postgresql容器运行是的日志位置，和名称：

```
 /var/log/postgresql/postgresql-10-main.log
```

##### 190218

docker 容器出现无限制重启尝试修复目录权限：

```
docker exec -it gitlab update-permissions
```

##### 190219

supervisor后台管理进程工具，默认需要使用Python2进行安装。

```shell
pip install supervisor
```

如无法使用pip安装可以使用`apt`进行安装。

```
sudo apt-get install supervisor
```

安装完成之后执行以下命令生成配置文件：

```shell
echo_supervisord_conf > /etc/supervisord.conf
```

也可以直接执行命令，生成默认的配置地址。

在生成的配置文件目录中创建新的`***.conf`文件，编写进程管理，以下为CPU_GPU_monitor案例:

文件名问thingsboard.conf

```conf
[program:CPU_GPU_monitor]
autorestart=True
autostart=True
command=/usr/bin/python3 /home/sgds/thingsboard_ts.py
user=sgds
```

添加完成之后执行supervisor命令：

```
sudo supervisorctl update       #更新添加的配置文件
sudo supervisorctl start CPU_GPU_monitor    #启动这个程序
```

supervisor守护进程（开机启动）

在`/etc`下增加文件`rc.local`填写以下内容：

```
/usr/lcoal/bin/supervisor
```

完成之后增加文件的可执行权限：

```shell
sudo chmod +x /etc/rc.local
```

重启电脑即可。



GITLAB 容器持久化，转移出现不能启动的解决方案：

主要日志文件集中在数据`postgresql`数据文件找不到的问题，依照指示以次创建一下目录：

```
sudo mkdir ./data/pg_tblspc
sudo mkdir ./data/pg_replslot
sudo mkdir ./data/pg_twophase
sudo mkdir ./data/pg_stat_tmp
sudo mkdir -p ./data/pg_logical/snapshots
sudo mkdir ./data/pg_snapshots
sudo mkdir -p ./data/pg_logical/mappings
sudo mkdir ./data/pg_commit_ts
```

随后再次执行文件目录权限更新程序：

```
docker exec -it gitlab update-permissions
```

##### 190225

安装paho

```
pip install paho-mqtt
```

安装nvml 包：

```
pip install nvidia-ml-py3
```

安装psutil

```
pip install psutil
```

##### 190226

数据采集时间

系统最大主频

完成发送数据程序修改。

##### 190228

