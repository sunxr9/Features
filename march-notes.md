##### 190301

空气湿度

修改次数



##### 190302

判断加减

随机需要修改的数值，保留一位小数

大于增，小于减

数据最大值，不可高与此

返回修改之后的数据

随机数据，判断加减，产生最终数据

当前湿度数据

返回1--10中的一个随机整数

随机电流

空气温度

##### 190304

返回一个在范围内的随机数



限制最低值

##### 190306

完成模拟数据发送，自启动。



##### 190307

功率换算单位，每分钟采集次数（60 / 采取时间） * 60分钟 * 1000



##### 190311

链接postgresql 数据库：

1. 进入后台切换至postgres用户

2. 使用psql命令进行链接：psql -U username -d databaseName

   ```
   # 查看数据库
   \l
   #  使用数据库或者选择数据库
   \c databaseName
   # 查看表架构／表结构
   \dn
   # 列出当前数据库和链接的信息
   conninfo
   # 查看当前数据库的所有表格
   \d
   查看表结构
   \d table_name
   ```

   

pandas 时间统计的关键字

![时间统计的关键字](/home/sunxr/git_data/test/docs/image/pandas时间统计关键字.png)

使用的是df.resample()方法，例：

```
df.resample("T").sum()
df.resample("T").mean()
```



##### 190312

安装postgresql:

```
# 更新系统
sudo apt-get update & sudo apt-get upgrade
# 安装
sudo apt-get install postgresql postgresql-contrib
```

修改postgresql 配置和默认用户

```
sudo passwd postgres
# 密码设置为１２３４５６
```

以上为设置postgres 用户在liunx 系统下的登录密码，在设置完成之后登录postgres用户，为postgresql数据库设置链接密码：

```
# 切换用户，使用上述步骤设置的密码
su - postgres
# 设置数据库链接密码，将一下的`newpassword`替换为想要设值的密码，此密码应为高强度密码
psql -d template1 -c "ALTER USER postgres WITH PASSWORD 'newpassword';"
```



数据库迁移

首先切换到postgres用户下：

备份:

```
pg_dump [database_name] > /path/to/db.dump
```

导入:

psql [database_name] -U [username] < /path/to/db.dump



远程链接数据库;

##### 1. 修改postgresql.conf

`postgresql.conf`存放位置在`/etc/postgresql/9.x/main`下，这里的`x`取决于你安装PostgreSQL的版本号，编辑或添加下面一行，使PostgreSQL可以接受来自任意IP的连接请求。

```
listen_addresses = '*'
```

##### 2. 修改pg_hba.conf

`pg_hba.conf`，位置与`postgresql.conf`相同，虽然上面配置允许任意地址连接PostgreSQL，但是这在pg中还不够，我们还需在`pg_hba.conf`中配置服务端允许的认证方式。任意编辑器打开该文件，编辑或添加下面一行。

```
# TYPE  DATABASE  USER  CIDR-ADDRESS  METHOD
host  all  all 0.0.0.0/0 md5
```

默认pg只允许本机通过密码认证登录，修改为上面内容后即可以对任意IP访问进行密码验证。对照上面的注释可以很容易搞明白每列的含义，具体的支持项可以查阅文末参考引用。

完成上两项配置后执行`sudo service postgresql restart`重启PostgreSQL服务后，允许外网访问的配置就算生效了

##### 190313

节点机用户名称：root

密码：kedacom#123

系统无法联网：修改`/etc/system-conf/network/`下的文件，将IP地址修改之后重启network,还是不行．

之后使用`dhclient`命令之后就可以链接了．重新获取ｉp 命令



centos　开启root远程访问

编辑`/etc/sshd/sshd_conf`/文件，找到一下参数并修改为以下配置：



```
# 监听端口和地址
Port 22
ListenAddress 0.0.0.0
ListenAddress ::
# 允许远程登录
PermitRootLogin yes
# 使用用户名和密码作为链接
PasswordAuthentication yes
```

修改完以上配置重启sshd服务即可

```
service sshd restart 
```

检查sshd 服务和监听端口

```
ps -ef | grep ssh
# 检查端口
netstat -an | grep 22
```



## 华为路由密码　sgds1234

##### 190313

设置ｕbuntu静态IP,编辑`/etc/networking/interfaces`文件：

添加以下内容：

```
auto eth0# 此名称是变化的，随机生成的，不是固定名称
iface eth0 inet static  # 设置IP为静态
    address 10.0.0.41 # IP
    netmask 255.255.255.0　# 子网掩码
    # network 10.0.0.0 # 
    # broadcast 10.0.0.255 # 
    gateway 10.0.0.1 # 网关地址
    dns-nameservers 10.0.0.1 8.8.8.8
    # dns-domain acme.com
    # dns-search acme.com
```

静态网址不能上网．

配置静态IP注意点：

一，IP地址不能随便写，在内网中的IP地址要与交换机的网段配置一样，及前三段IP地址要一样．

```
192.168.3.xxx # 只有最后的一段是可以修改的
```

二，注意网关要配置好，默认的一般都是192.168.1.1

三，子网掩码也要一样

四，需要填写DNS解析地址

五，ONBOOT＝yes,此项表示开机加载网卡．

六，DNS地址默认写网关地址．

postgresql 重启：

```
pg_ctlcluster 9.5 main reload
```

创建的用户：

```
# 创建用户ｕserOne，　密码１４２５３６
CREATE USER userOne WITH PASSWORD '142536';
# 将数据库postgres,所有权限付给用户ｕserOne
alter database database_name owner to postgres_name;
# 修改用户权限
alter user username [superuser, createrole, createdb]
# 注意权限中间没有逗号，使用空格区分
```



删除dpkg文件目录修复方法：首先，创建目录：

```
sudo mkdir -p /var/lib/dpkg/{alternatives,info,parts,triggers,updates}
```

恢复一些备份：

```
sudo cp /var/backups/dpkg.status.0 /var/lib/dpkg/status
```

现在，让我们看看你的dpkg是否正常工作（开始祈祷）：

```
apt-get download dpkg
sudo dpkg -i dpkg*.deb
```

如果一切都“正常”，那么也要修复基本文件：

```
apt-get download base-files
sudo dpkg -i base-files*.deb
```

现在尝试更新您的包列表等：

```
dpkg --audit
sudo apt-get update
sudo apt-get check
```

##### 190315

centos7 yum查看安装包信息

```
yum info packageName
```

安装supervisor

```
yum install supervisor
```

使用root用户使用的使用会出现找不到配置文件，使用`-c`命令制定配置文件启动：

```
supervisorctl -c /etc/supervisor.conf start|update|relaod
```



nvidia显卡驱动出现错误，运行nvidia-smi出现一下提示：

```
NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver
```

运行nvidia-uninstall卸载当前驱动．

修复尝试一下步骤：

```
# 查找当前系统下的驱动程序
rpm -qa|grep -i nvid|sort
```

确认当前系统没有nvidia驱动程序，如有使用一下命令卸载程序：

```
yum  remove kmod-nvidia-390.87-1.el7_5.elrepo.x86_64  xorg-x11-drv-nvidia-384.81-1.el7.x86_64yum search  kmod-nvidia   nvidia-kmod-384.81-2.el7.x86_64
```

安装显卡检测程序：

```shell
rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm 
```

```
yum install nvidia-detect 
# 安装完成之后运行nvidia-detect
```

运行结果出现`kmod-nvidia`提示，之后进行安装基础运行包：

```
yum install kernel-devel kernel-doc kernel-headers gcc\* glibc\*  glibc-\*
```

安装刚才检测到的驱动程序:

```shell
yum install kmod-nvidia
```

运行完成之后使用nvidia-smi查看进程的使用情况．

上述失败，安装完成之后运行还是出现上述问题，再次尝试:

使用`yum`直接进行安装`kmod-nvidia`,

失败，运行nvidia-detect -v 查看当前的显卡版本．



三，再次尝试

安装dkms模块句：exit 0 前面才行。

```
yum install kernel-devel epel-release dkms
```

在grub启动项中修改：

编辑/etc/default/grub并在GRUB_CMDLINE_LINUX Regen grub config中添加nouveau.modeset=0以应用更改：

```
grub2-mkconfig -o /boot/efi/EFI/centos/grub.cfg
```



##### 190318

centOS7 开机自启服务:

在`/usr/lib/systemd/system`下创建`serverName.service`文件，在文件中添加一下内容：

```
# supervisord service for systemd (CentOS 7.0+)
# by ET-CS (https://github.com/ET-CS)
[Unit]
Description=Supervisor daemon

[Service]
Type=forking
ExecStart=/usr/bin/supervisord
ExecStop=/usr/bin/supervisorctl $OPTIONS shutdown
ExecReload=/usr/bin/supervisorctl $OPTIONS reload
KillMode=process
Restart=on-failure
RestartSec=42s

[Install]
WantedBy=multi-user.target
```

每一个服务以.service结尾，一般会分为3部分：[Unit]、[Service]、[Install]

[Unit] 主要是对这个服务的说明，内容包括Description和After，Description用于描述服务，After用于描述服务类别

[Service] 是服务的关键，是服务的一些具体运行参数的设置，

Type=forking是后台运行的形式，

PIDFile为存放PID的文件路径，

ExecStart为服务的具体运行命令，

ExecReload为重启命令，

ExecStop为停止命令，

PrivateTmp=True表示给服务分配独立的临时空间

注意：[Service]部分的启动、重启、停止命令全部要求使用绝对路径，使用相对路径则会报错！

[Install] 是服务安装的相关设置，可设置为多用户的

服务脚本按照上面编写完成后，以754的权限保存在/usr/lib/systemd/system/目录下，这时就可以利用systemctl进行配置



完成之使用`systemctl`命令启动服务，之后就可以自启动了，一下是`systemctl`命令指南：

systemctl status serverName.service            // 查看serverName启动状态

systemctl start serverName.service             // 启动 serverName

systemctl stop serverName.service              // 关闭 serverName

systemctl enable serverName.service         // 开机启动 serverName 服务

systemctl disable serverName.service　　// 开机关闭serverName服务



在修改完成之后需要修改supervisor的配置文件，将`nodaemon=false`修改为`true`.

在重启之后还是不能运行守护进程服务，但是能自启动，在手动关闭当前supervisor进程之后，再重启之时不在是后台启动，所以需要把上一步修改回来．

**尝试第二种**

或者将`/usr/lib/systemd/system/xxx.service`文件中的Service内修改为以下:

```
[Unit]
Description=Process Monitoring and Control Daemon
After=rc-local.service

[Service]
Type=forking
ExecStart=/usr/bin/supervisord -c /etc/supervisord.conf
SysVStartPriority=99

[Install]
WantedBy=multi-user.target
```

以上方式还是可以子启动，但是不能够启动守护进程程序．



需要尝试自动添加开机自启服务,以下为`jenkins`为例：

```
systemctl enable jenkins.service #设置jenkins服务为自启动服务
sysstemctl start  jenkins.service #启动jenkins服务
```

##### 190319

更换启动方式,编写一个启动脚本，不在直接启动supervisor,通过脚本定时开机五分钟之后在启动supervisor．脚本如下：

```sh
#!/bin/sh
#chkconfig: 2345 80 90
#description: 开机启动supervisord
sleep 300s

supervisord -c /etc/supervisord.conf

```

将一下文件复制到`/etc/rc.d/init.d/`目录下，并增加可执行权限．

脚本第一行 “#!/bin/sh” 告诉系统使用的shell； 
脚本第二行 “#chkconfig: 2345 80 90” 表示在2/3/4/5运行级别启动，启动序号(S80)，关闭序号(K90)； 
脚本第三行 表示的是服务的描述信息

之后将脚本添加到开机启动项目中：

```
chkconfig --add shellName.sh
chkconfig shellName.sh on
```

还是出现只能启动`supervisor`本身，监控程序无法启动．但是在启动之后单独启动`supervisor`就可以对监控程序进行管理．



尝试将启动的方式改为`/etc/rc.local`文件中添加启动`supervisor`启动脚本命令：

```
#/etc/rc.local
/bin/sh /root/start.sh
```

start.sh脚本内容不变．



修改`/etc/rc.local`文件，将前面的`/bin/sh`移除，直接运行start.sh文件．

最终问题在与代码错误，在配置`supervisord`开机自启的时候，还没有真正启动完成，`supervisor`就会启动，所以无法获取到环境变量，导致程序意外终止．修改代码，将配置文件获取方式修改．



##### 190321

##### 190325

修改温度获取的关键词，还有时间显示的格式

1553504150493



##### 190326

redmine　发送邮件附带的URL地址不对修改方法：

admin登录→配置→主机名称，改为域名或[IP](https://www.baidu.com/s?wd=IP&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)的形式，缺省是localhost



##### 190328

selenium 控制chrome浏览器需要chromedriver插件：安装方式如下：

手动下载插件地址：https://sites.google.com/a/chromium.org/chromedriver/home

下载linux版，之后进行解压操作．

然后将chromedriver 插件移动至`/usr/bin/`下，注意名称还是`chromedriver`，不可以错．

然后将文件权限交给root: `sudo chown root:root /usr/bin/chromedriver`

添加可执行权限：`sudo chmod +x /usr/bin/chromedriver`到此就可以了．



##### 190329

设备建立完成，实体别名建立完成．