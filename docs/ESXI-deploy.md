# deploy ESXI

部署ESXI6.7 至戴尔T7920塔式服务器．

## 简述

部署ESXI实现底层虚拟化，将服务器资源更加合理分配，并实现弹性伸缩等．



## 准备

本次使用光驱之来进行安装，请至官网自行[下载](<https://my.vmware.com/cn/web/vmware/evalcenter?p=free-esxi6>)ESXI iso文件,并按照[教程](<https://docs.vmware.com/cn/VMware-vSphere/6.7/vsphere-esxi-67-installation-setup-guide.pdf>)进行CD/DVD系统盘构建．

## 安装

### 创建RAID盘

1. 开机使用F12按键进入BIOS启动项选择画面：![BIOS启动项选择画面](./image/BOIS.jpeg)

2. 选择**OTHER OPTIONS**中的**Device Configuration**选项，进入下图画面：![设备配置详情画面](./image/DeviceConfiguration.jpeg)

3. 使用键盘方向键选择**Intel(R) RSTe STAT Controller**选项，进入如下画面，选择创建RAID卷：![创建RAID画面](./image/CreateRAID.jpeg)

4. 进入创建RAID卷画面![创建RAID卷选项](./image/CreateRAIDOptions.jpeg)

   当前画面需要进行一下操作：1. 输入创建的RAID卷名称（建议使用默认）2. 选择RAID等级（[等级详情](<https://en.wikipedia.org/wiki/Standard_RAID_levels>)）3. 选择需要进行创建的硬盘 4. 选择[**Strip Size**](<https://en.wikipedia.org/wiki/Data_striping>)以及**Capacity（MB）**(建议使用默认)

5. 操作完成进行创建，等候创建完成．至此可返回第三步查看RAID卷信息以及状态．

### 安装ESXI

在完成RAID卷设置之后可通过退出**Device Configuration**或重启机器通过F12进入BIOS启动选择画面（参见创建RAID盘第一步）．

1. 进入BOIS启动项选择画面，选择CD/DVD启动，进入ESXI选择画面![ESXI 选择安装](./image/OptionInstall.jpeg)

2. 选择完成之后进入加载页面![ESXI 加载页面](./image/Load.jpeg)
3. 加载完成后，ESXI开始进行硬件检查![检查硬件画面](./image/CheckDevice.jpeg)
4. 设备检查完成后进入欢迎画面，Enter 继续![确认安装画面](./image/EnterInstall.jpeg)

5. 安装协议，使用F11进行确认![安装协议](./image/protocol.jpeg)

6. ESXI将进行磁盘扫描

   ![搜索本地磁盘](./image/search.png)

7. 选择系统安装磁盘，Eneter 确认![选择安装磁盘](./image/selectDisk.png)

8. 选择键盘布局,默认使用英文布局![键盘布局选择](./image/keyboardLayout.jpeg)

9. 创建root用户密码，并确认密码![创建root密码](./image/password.jpeg)
10. 最后确认安装，等待安装完成之后出现重启画面![重启选择](./image/Reboot.jpeg)

最后取出光盘，重启机器，等待ESXI安装配置以及链接地址.

