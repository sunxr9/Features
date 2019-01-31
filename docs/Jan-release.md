##### 190101

安装视频编辑器：

```
sudo apt-get install kdenlive
```

##### 190103

shift +　prtSc gnome桌面可选截屏，选择区域即可．

单独点击prtSc 截取当前桌面所有内容．

Art + PrtSc　截取当前的窗口信息．

##### 190104

ubuntu 解压rar文件．

终端中输入命令安装压缩程序rar和解压缩的unrar.
 sudo apt-get install rar unrar
 sudo apt-get install rar rar

linux中解压rar类型文件的命令为：
 unrar  e file.rar  # 把原rar压缩包中的全部文件解压到当前目录下，没有目录
 或者 rar x file.rar  # 把原rar压缩包中的全部文件解压到x下
 其实后面要不要扩展名都可以。

升级flash,最后还是没啥用．

##### 190107

##### 190108

安装一体机的测试：使用gitlab镜像，测试application的认证保存．

docker 命令：export持久话容器，不是针对的镜像. save是针对持久话镜像．

保存的文件恢复．

##### 190109

启动容器的时候创建挂载数据卷，尝试进行数据保存，在创建一个新的容器，进行共享．

gitlab的数据保存位置存放在**/var/opt/gitlab**．将容器保存的文件再次使用，启动过程很慢，但是原有的数据还是保存了下来，主要的application 应用的认证还存在．

创建一个新的hub容器，安装认证插件，使用配置文件启动，可以定义gitlab认证，但是nginx代理无法通过，不能使用容器代理．nginx代理容器默认启动可以访问，但是修改代理配置执行启动就不能进行代理，无法进行访问．

**nginx**容器配置注意点

在容器内部的配置文件**proxy_pass**不能使用ｌｏｃａｌｈｏｓｔ，需要宿主机的IP,这样才可以代理出来．



##### 190110

docker 进入容器的时候指定进入的用户名：

```
# 使用--user　＜username-用户名＞
# example 
docker exec -it --user root <container [name][ID]> /bin/bash
```

注意gitlab容器生成数据卷保存进行下次使用不可修改权限，特别**注意点为**:隐藏文件．



ubuntu 系统启动修复：

```
# https://linuxconfig.org/ubuntu-boot-repair
# 官网介绍：大概为一下步骤
# １．使用usb启动，进入试用ｕbuntu,
# ２．安装boot-repair
sudo add-apt-repository ppa:yannubuntu/boot-repair
sudo apt-get update
sudo apt install boot-repair
# ３．运行boot-repair选择推荐修复
boot-repair
# ４．关机重启，在启动按住(Shift)进入ｕbuntu选择(GRUB)界面，选择中间的高级选项．将会看到不同的内核选项，在每一个内核选项的下面将有一个相同的条目,并带有(recovery mode)．
# 5. 选择recovery　mode项稍后会弹出新的界面．选择resume项进行修复．
```

ｕbuntu 安装nvidia显卡驱动：

出现依赖问题：

```
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 nvidia-driver-396 : Depends: nvidia-dkms-396 (= 396.54-0ubuntu0~gpu18.04.1) but it is not going to be installed
                     Depends: nvidia-utils-396 (= 396.54-0ubuntu0~gpu18.04.1) but it is not going to be installed
                     Recommends: nvidia-settings but it is not going to be installed
                     Recommends: nvidia-prime (>= 0.8) but it is not going to be installed
                     Recommends: libnvidia-compute-396:i386 (= 396.54-0ubuntu0~gpu18.04.1)
                     Recommends: libnvidia-decode-396:i386 (= 396.54-0ubuntu0~gpu18.04.1)
                     Recommends: libnvidia-encode-396:i386 (= 396.54-0ubuntu0~gpu18.04.1)
                     Recommends: libnvidia-ifr1-396:i386 (= 396.54-0ubuntu0~gpu18.04.1)
                     Recommends: libnvidia-fbc1-396:i386 (= 396.54-0ubuntu0~gpu18.04.1)
                     Recommends: libnvidia-gl-396:i386 (= 396.54-0ubuntu0~gpu18.04.1)
E: Unable to correct problems, you have held broken packages.
```

使用一下步骤进行安装:

```
sudo apt-add-repository -r ppa:graphics-drivers/ppa
sudo apt update
# 删除原有的驱动
sudo apt remove nvidia*
sudo apt autoremove
# 进行安装
sudo ubuntu-drivers autoinstall
```

##### 190114

chromium　无法打开，尝试一下方法：

```
# 删除home目录下的google配置文件．
# 更新所有软件．
# 屏幕分辨率的问题，需要重启一下尝试．
```

重新安装，使用包安装chrome.

```shell
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# 使用wget下载chrome包．之后使用dpkg安装
sudo dpkg -i google-chrome-stable_current_amd64.deb
```



docker-compose 中network的使用：

```
version: "3"
services:
  test2:
    image: nginx
    networks:
      - default
      - app_net
    external_links:
      - test1
    container_name: test2
networks:
  app_net:
    external: true
```



以上为例：同service级别的networks,主要为网络名称．和网络名称的设置．

上述为app_net的网络名称，　external参数为是否使用外部网络．

> 注意点：文件内部的网络名称在使用外部的网络的情况下需要和外部网络名称一制. docker 会自动寻找网络．

另外在同级别的networks下设置default名称的网络．所有的服务默认都会使用它．

server下的test2中的networks设置为使用的网络名称．此网络名称不限于本文件中名称的网络名称．还可以使用docker中默认的网络名称．

##### 190115

镜像成功，但是因为在源码中增加了中午，在镜像中启动的时候出现了乱码．不识别的现象，需要重新构建镜像．

构建的时候发现nbviewer不是最新版，在github上拉取最新源代码再次构建．

使用nginx代理的访问会出现静态文件不能加载，只能在使用端口的访问方式．

##### 190116

编写技术手册．

##### 190117

##### 190118

继续编写文档．

流水帐似的部署方案，说明需要做什么事情，每个步骤为什么这么做，做出来有什么效果．

讲什么，前世今生，为什么讲．

##### 190121

写文档．

##### 190122

文档

##### 190123

编写计划．

##### 190124

分支合并．出现冲突，原因是为两个分支不同步．

合并步骤：

使用fetch获取远程库的分支信息，和提交信息．

```
git fetch ［remoteName］
```

使用git checkout 命令创建分支，并获取远程的对应分支数据．

```
git checkout -b 需要创建的分支名称　远程仓库地址/远程仓库分支名称
# 在这里本地新创建的分支名称最好和远程的分支名称一致．
```

再次执行获取远程仓库的信息．之后切换问主分支尝试进行合并．

```
git fetch origin
git checkout origin/master
git merge --no-ff YOFC-dev
```

如出现错误，不能合并，使用`git status`查看不能合并的文件，进行手动修改．修改完成之后在手动进行添加提交．之后进行推送最新版，

```
git push origin master
```

主要注意点．多查看状态，根据状态来判断下一步如何进行操作．



注册用户，填写文件．



##### 190125

写文档．

##### 190128

##### 190129

升级redmine．需要下载安装包．然后备份数据库．

redmine 所有上传的文件在`/var/lib/redmine/default`下．

##### 190130

使用python-redmine链接redmine出现的issues无法获取json数据的问题：

1. 在首页找到管理，然后在配置中找到API选项（不是项目配置），勾选启动REST Web service.
2. 点击右上角的我的帐号，注意右侧见面的有个API访问键，点击显示，出现hash码，使用这个做链接key, 就可以访问了．



使用以上方法就可以访问所有的数据了．

用户的get方法只能使用用户的ID进行访问．filter可以获取用户名称．

部署文档全部后边全部重新编写，从运行准备开始．

##### 190131

项目中现启动问题，gitlab的容器启动失败，最后为删除携带的日志文件，然后就可以正常启动了．