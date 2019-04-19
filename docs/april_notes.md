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

**2，** 使用开源版本，在ubuntu使用一下命令即可安装：Harbor12345

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



