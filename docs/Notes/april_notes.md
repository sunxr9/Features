##### 190401

转移redmine和nbviewer

##### 190402

##### 190403

192.168.31.71



##### 190408



##### 190415

节点机需要安装的包：

```
conda install numpy pyyaml mkl mkl-include setuptools cmake cffi typing
conda install -c pytorch magma-cuda90
conda install -c pytorch pytorch
conda install opencv
```

##### 190418

配置显卡直通

在ESXi 6.5的界面下方，可以看见一个IP地址。

打开另一台电脑，在浏览器中输入该IP地址，使用刚刚设定的账户和密码登录，即可进入Web Client，对ESXi进行配置。

在页面左边Navigator -> Host -> Manage -> Hardware -> Pci Devices即可看到各个硬件。

再添加虚拟机，Navigator -> Virtual Machines -> Create/Register VM。

安装虚拟机的各个选项与在Vmware软件里添加虚拟机的步骤基本相同。在虚拟机里面安装好系统，先安装VMtools，再安装显卡驱动。

安装好虚拟机后，在编辑虚拟机设置（虚拟机选项）中点击添加，选择PCI设备。勾选要直通的显卡，即可完成显卡直通。



**安装VMware Tools**

**1**， 在VMware　软件上点击VM选项中的**Install VMware Tools**即可．

**2，** 使用开源版本，在ubuntu使用一下命令即可安装：

```
sudo apt-get install open-vm-tools open-vm-tools-desktop
```





ｕbuntu 安装显卡驱动：

**1**，使用ｕbuntu自带的ｕbuntu-drivers进行安装：

```
# 检测设备
sudo ubuntu-drivers devices
# 安装推荐程序
sudo ubuntu-drivers autoinstall
# or
# 使用apt选择安装
sudo apt-get install nvidia-***
```





##### 190422

Python 2.7 中除法需要注意：当两个整数相除得到的结果为整数，自动舍弃小数点后的数字．解决方法就是在一个数字后面加上一个小数点，这样将自动转化为浮点数除法．



##### 190423

ubuntu 远程桌面配置：

```
# 更新ｕｂｕｎｔｕ
sudo apt update
sudo apt dist-upgrade
# 安装ｘｒｄｐ
sudo apt-get install xrdp
# 为ＸＲＤＰ设置Ｘｓｅｓｓｉｏｎ文件
ech mate-session > ~/.xsession
# 安装ｍａｔｅ-core软件包
sudo apt-get install mate-core
# 允许ＵＦＷ防火墙通过ＲＤＰ流量
sudo ufw allow 3389/tcp
# 重启
sudo reboot
```



打开语言设置选项，提示需要安装一些支撑，点击安装后安装失败。

使用命令安装`sudo apt install $(check-language-support)`

##### 190424

vmware 启动项出现错误，提示需要安装核心，需要安装ｇｃｃ和ｍａｋｅ模块才可以安装，不然会报错。

VMware 启动命令文件位置在`/usr/bin/vmware`



ｕbuntu　忘记密码：

1. 开机按住shift按键（速度要快），进入ｕbuntu高级选项
2. 在高级选项中找到最后括号内有***recovery mode***一行　
3. 按***e***进入编辑页面，找到***linux***开头的信息
4. 将最后的recovery nomodesett 替换为quiet splash rw init=/bin/bash
5. 按F１０



##### 190426



mysql重置密码：

1. 编辑配置文件，ｕbuntu在`/etc/mysql/mysql.conf.d/mysqld.conf`，在`[mysqld]`选项后增加`skip-grant-tables`
2. 重启mysql服务`sudo service restart mysql`
3. 登录mysql，登录时会出现输入密码，但是只需要回车即可，不用做任何输入．
4. 更新密码：`ｕpdate msyql.user set authentication_string=password('123456') where user='root' and Host='localhost'`
5. 执行刷新命令`flush privileges`，后退出．
6. 删除第一步在`mysqld.conf`文件中添加的陪置．
7. 再次重启mysql，使配置文件生效，使用密码登录验证
8. 如密码验证不通过，无法登录，再次按照以上步骤依次执行，但是将第四步更改为`alter user 'root'@'localhost' identified by '123456'`，其中的123456为新的密码．



##### 190429

eth container 运行命令：

```
nvidia-docker run -it anthonytatowicz/eth-cuda-miner -RH -SP 1 -S asia1.ethermine.org:14444 -O 0x27338a2e68C034733D717469d3FD3377a898068F.worker/Sunxrs@gmail.com -U

```

