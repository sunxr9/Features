### gitlab应用

#### 定位： 

主体：代码仓库， 版本控制系统。增强开发人员协同工作。

次级：管理权限、bug跟踪、活动跟踪等。



注册不说。

##### 配置信息

1， 配置全局用户信息

​	git config --global user.name username

​	git config --global user.email 'email@xxx.com' 

2， 配置本地（项目）用户信息：

​	git config --local user.name username

​	git config --local user.email 'email@xxx.com'



##### ssh认证

生成密钥： ssh-keygen -t rsa -C "YOUR_EMAIL@YOUREMAIL.COM" 

获取SSH公钥信息 ： cat ~/.ssh/id_rsa.pub

打开个人设置， 选择ssh。将SSH公钥信息添加SSH Key中。按照要求填写信息。

测试链接：ssh -T git@192.168.3.43

出现Welcome to GitLab, @name! 即成功。





### 项目操作

##### 创建项目

导航条中 '+' 图标， 选择项目。

按照要求填写项目的名称和可见性信息。

默认生成一个空的仓库。



##### 项目

整体查看项目活动， 周期分析。总体展示。



##### 仓库

主体为版本控制， git信息展示。

项目整体文件。

提交信息展示。

分支操作。 创建、提交、合并请求。

```
# 创建分支: git branch branch1
# 切换分支：git checkout branch1
# 合并分支：git merge branch1
```

标签信息，版本标签。git tag -a v1.1 -m 'version 1.1'





































#### git命令

```
git init //初始化 （创建本地git库）
git remote add origin 仓库地址  //添加远程项目地址（可在项目主页复制）
git add main.cpp //将某一个文件添加到暂存区
git add .          //将文件夹下的所有的文件添加到暂存区
git commit -m ‘note’ //将暂存区中的文件保存成为某一个版本
git log             //查看所有的版本日志
git status          //查看现在暂存区的状况
git diff            //查看现在文件与上一个提交-commit版本的区别
git apply 			// 添加对比出的差别
git reset --hard HEAD^ //回到上一个版本
git reset --hard XXXXX //XXX为版本编号，回到某一个版本
git pull origin master //从主分支pull到本地
git push -u origin master //从本地push到主分支
git pull                //pull默认主分支
git push                //push默认主分支
```

