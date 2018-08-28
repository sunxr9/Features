https://about.gitlab.com/installation/#ubuntu # 安装文档。

测试部署gitlab:

1, 安装并配置必要的依赖享：

```
sudo apt-get update && sudo apt-get install -y curl openssh-server ca-certificates
```

2, 安装postfix发送邮件。

```
sudo apt-get install -y postfix
```

在postfi安装期间会出现配置选项， 选择`Internet Site` 并按Enter确认，使用服务器的外部DNS作为‘’邮件名称“， 并按Enter键，如果出想其他屏幕，继续按Enter键接受默认值。

3， 添加Gitlab软件包存储库并安装软件包：

```
# 添加gitlab包存储库
curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash
```

**[sudo] apt-get update**此处文档中没有，**[sudo] apt-get upgrade**

4, 安装gitlab 包，配置需要访问的gitlab实例路径。

```
sudo EXTERNAL_URL='http://192.168.3.51' apt-get install gitlab-ce
```

 安装完成，配置失败。

错误， 安装失败， 安装成功会出现一个图标，并提示配置的可访问地址，以及gitlab的官方READMI文件链接。



#### gitlab 安装出现以下错误， 解决方法， 设置ubuntu de 语言

> ```
> Running handlers:
> There was an error running gitlab-ctl reconfigure:
> 
> execute[/opt/gitlab/embedded/bin/initdb -D /var/opt/gitlab/postgresql/data -E UTF8] (postgresql::enable line 80) had an error: Mixlib::ShellOut::ShellCommandFailed: Expected process to exit with [0], but received '1'
> ---- Begin output of /opt/gitlab/embedded/bin/initdb -D /var/opt/gitlab/postgresql/data -E UTF8 ----
> STDOUT: The files belonging to this database system will be owned by user "gitlab-psql".
> This user must also own the server process.
> ```

#### export LC_CTYPE=en_US.UTF-8

export LC_ALL=en_US.UTF-8
sudo dpkg-reconfigure locales





**您可以使用登录名root和密码访问新安装，登录5iveL!fe后需要设置唯一密码**

```
  - git diff 是对比 两个分支的不同 
  - 8-15-stable  是英文分支
  - 8-15-stable-zh 是汉化分支
  - ~/8.15.diff  导出我们需要的汉化文件

```

https://laravel-china.org/topics/2584/gitlab-installation-and-localization # 汉化修改。

http://nutlee.space/2016/08/11/GitLab%E5%BF%AB%E9%80%9F%E6%90%AD%E5%BB%BA%E5%8F%8A%E4%B8%AD%E6%96%87%E6%B1%89%E5%8C%96/ # 另外的一个版本

1， 下载gitlab源码。

2， 进入目录。

3.1， 执行sudo git diff origin/11.1.1-stable  origin/11.1-stable-zh > tmp/11.1.diff

`11.1.1-stable为英文版， 11.1.1问版本，`此命令是对比两个版本的差异。

3.2， 执行 sudo git diff v11.1.1 v11.1.1-zh > /tmp/11.1.1.diff 

**两个命令稍有不同， 还不是很确定那个有用。**

4， 停止gitlab运行。sudo gitlab-ctl stop

5， 进入gitlab 源码路径： cd /opt/gitlab/enbedded/service/gitlab-rails

6， 执行： git apply /tmp/11.1.1.diff。

7， 启动gitlab： sudo gitlab-ctl start