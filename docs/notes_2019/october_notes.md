##### 191008 

django 2.2 要求 SQLite3 数据库版本在 3.8.3 以上，所以我们需要安装最新版SQLite3

**ubuntu**

```bash
sudo apt-get update
sudo apt-get install sqlite3
# 查看当前安转版本
sqlite3 --version
```

**CentOS**

```bash
sudo yum install sqlite-devel
# or
sudo gem install sqlite3-ruby
```

**源码安装**

```bash
wget https://sqlite.org/2019/sqlite-autoconf-3290000.tar.gz
tar zxvf sqlite-autoconf-3290000.tar.gz
cd sqlite-autoconf-3290000
./configure
make
sudo make install
```



**nginx**

使用 Nginx 进行 Django 项目部署过程中，静态文件无法进行访问的几个排查方向：

+ 项目配置
+ 文件权限
+ Nginx 配置

**项目配置**

在配置文件 `settings.py` 文件中，`STATIC_URL = "/static/"` 一般不做改变，我们需要关注的是 `STATIC_ROOT="path/to/static"`，如果相对路径不确定是否正确，可替换为绝对路径进行测试．

如果在开发环境下添加了 `STATICFILES_DIRS` 配置，在部署的时候需要进行注释，此配置与 `STATIC_ROOT` 相互冲突，只能存在一个．

**文件权限**

一般在部署项目的时候，采用的获取源码主要是通过 Git 或者 可视化工具进行上传（），无论那种，默认的文件权限都是当前操作的用户权限．

在使用 Nginx 代理的时候，Nginx 有可能无法进行读取．所以需要进行对权限的控制，可通过一下命令进行修改：

```bash
sudo chmod -R 755 /path/to/static/* 
```

**Nginx 配置**

在(CentOS) Nginx 的配置文件 `/etc/nginx/nginx.conf` 中找到 `user` 一词，确认用户拥有读取权限．　



##### 191009

Django 站点管理页面标题设置

通过在创建的应用目录中的 admin.py 文件增加两行配置即可：

```python
admin.site.site_header = "" # 页面h1标题
admin.site.site_title = "" # 网页标题
```

踩过的坑：

个人不太喜欢Django默认的管理页面，所以使用的插件 `django-admin-tools` 进行扩展后台页面显示，但是在自定义设置出现问题，`admin.site.site_header` 始终无法显示自定义的内容，最终排查出原因出现在扩展包的css文件中．

首先确定静态文件路径，在按照扩展工具的提示下操作，采集后的静态文件在项目配置中的静态文件下,，例：`statics/admin_tools/css/theming.css`文件下．找到：`#header #branding h1` 样式设置．注释掉其中的 `text-indent` 和 `background` 选项．然后进行重启即可．

##### 191011

supervisor 设置程序自启的时候会出现环境问题，在终端中执行的命令没有报错，但是在supervisor下管理过程无法进行启动，出现缺少依赖包的情况．

这种情况需要在supervisor管理配置文件中增加环境变量配置，首先使用命令`echo $PATH` 查看当前运行的环境变量，然后在配置文件中增加: `environment=PATH=/home/sgds/anaconda3/bin:/home/sgds/anaconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin` 即可．多个变量使用逗号隔开．



##### 191014

navicat 延长试用期：在安装的时候会在home目录下创建`.navicat`目录，将其中的`system.reg,user.reg,userdef.reg` 文件删除，或者直接将`.navicat`目录删除，但是可能会清楚数据库连接信息．

##### 191018

+ 设置jupyterhub_config.py 文件oauth_callbock_url

+ 设置supervisor配置文件GITLAB_HOST环境变量

+ 在supervisor的frp配置文件中增加一项：`startretries=10`设置重启次数，不然frp会启动失败．

+ 设置GitLab Application callback_url 路由



##### 191022

rsync 同步远程目录，删除源路径下没有文件，保持绝对同步．使用`--delete` 参数：

```bash
# 语法如下
rsync -avpz --delete /path/to/ username@IP:/path/to/
# 需要注意的是路径的最后不可以有匹配符 *,并且源路径和目标路径一样．
```



##### 191024

Linux 配置 ssh-key :

+ 执行密钥生成命令：

  ```bash
  ssh-keygen
  ```

  使用 Enter 确认生成，需要确认三次，及生成一个2048位的RSA密钥对．在用户 home 目录下的 `.ssh`目录中会出现`id_rsa`和`id_rsa.pub` 两个文件，分别为私钥和公钥．

  ![1571878921163](image/1571878921163.png)

+ 将公钥复制到需要登录的机器

  1. 使用ssh-copy-id 命令，ssh-copy-id是一个非常实用的命令，极大的简化了配置ssh-key的步骤以及复杂性．

     ```bash
     # # 格式为：ssh-copy-id username@remote_host，例：
     ssh-copy-id sgds@192.168.3.239
     ```

  2. 通过 ssh 进入机器内部进行手动配置：

     1. 登录机器

        ```bash
        # # 格式为： ssh username@remote_host，例：
        ssh sgds@192.168.3.239 # 首次登录会出现以下画面，分别是确认连接以及输入登录密码
        ```

        ![1571879740540](image/1571879740540.png)

     2. 进入用户 home 目录下的 **.ssh** 目录中（如过没有用户 home 目录下没有 **.ssh** 目录，可自行创建），创建 `authorized_keys` 文件并进行编辑．

        打开 `id_rsa.pub` 文件（执行密钥生成命令步骤中生成的公钥文件），复制文件中的全部内容，粘贴在 `authorized_keys` 文件中，然后保存退出．

+ 测试ssh-key配置

  在执行密钥生成命令的机器上对刚才创建 `authorized_keys` 文件的机器进行ssh连接操作，如果直接登录成功，没有输入密码的步骤即为成功．

  ```bash
  ssh sgds@192.168.3.239
  ```



##### 191028

rsync 目标目录没有目录的情况下需要创建目录的方法：

增加 `-r` 参数，根据给出的远程目录进行创建，只会创建给出的远程目录所确实的目录:

```bash
rsync -azvp -r ./shared/ sgds@192,168.3.239:~/hub_share/test9
```

在上述命令中，如远程目录中没有test9文件目录，将会自动创建test9目录．

而 `-R` 参数就爱你会根据本地给出的文件目录进行同步（需要同步的数据绝对目录），在上述命令中，在远程目录中将会创建成 `~/hub_share/test9/(上传服务器的数据绝对路径)/shared/`．


​     

