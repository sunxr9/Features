##### 1101

手动清楚swap内存

```
swapoff -a && swapon -a
```

关闭swap，之后在开启swap。需要sudo权限。



##### 1102

https://github.com/jupyterhub/dockerspawner/issues/211

使用docker的image spawner， 可以选择容器。



lab 导出PDF：

1. 安装nvconvert

   ```
   pip install nbconvert
   # or
   conda install nbconvert
   ```

2. 要解锁nbconvert的全部功能，需要Pandoc和TeX（特别是XeLaTeX）。这些必须单独安装。

   ```
   sudo apt-get install pandoc
   ```


* 不同系统的latex安装地址
  * Linux：[TeX Live](http://tug.org/texlive/)
  * macOS（OS X）：[MacTeX](http://tug.org/mactex/)。	
  * Windows：[MikTex](http://www.miktex.org/)



3. 安装TeX Live

   ```
   sudo ./install-tl -repository https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/tlnet/
   ```

   注意需要管理员权限。如有必要，可能还需安装 `perl-tl` 和 `perl-doc`：

   ```
   sudo apt-get install perl-tk perl-doc
   ```

   执行命令之后会出现命令选项， 选择安装。进行等待。

4. 环境变量设置。

   此时 TeX Live 虽已安装，但其路径对于 Linux 来说仍是不可识别的。所以需要更改环境变量。

   打开 `~/.bashrc`，在最后添加

   ```
   export PATH=/usr/local/texlive/2018/bin/x86_64-linux:$PATH
   export MANPATH=/usr/local/texlive/2018/texmf-dist/doc/man:$MANPATH
   export INFOPATH=/usr/local/texlive/2018/texmf-dist/doc/info:$INFOPATH
   ```

   还需保证开启 sudo 模式后路径仍然可用。命令行中执行

   ```
   sudo visudo
   ```

   找到如下一段代码

   ```
   Defaults        env_reset
   Defaults        mail_badpass
   Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
   ```

   将第三行更改为

   ```
   Defaults        secure_path="/usr/local/texlive/2018/bin/x86_64-linux:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
   ```

   也就是加入 TeX Live 的执行路径。如果在安装时作了修改，这里的路径也都要与安装时的保持一致。

5. 字体设置

   ## 字体设置

   要在整个系统中使用 TeX 字体，还需要将 TeX 自带的配置文件复制到系统目录下。命令行中执行

   ```
   sudo cp /usr/local/texlive/2018/texmf-var/fonts/conf/texlive-fontconfig.conf /etc/fonts/conf.d/09-texlive.conf
   ```

   之后再执行

   ```
   sudo fc-cache -fv
   ```

   刷新字体数据库。

6. 检查安装

   ```
   tlmgr --version
   pdftex --version
   xetex --version
   luatex --version
   ```



https://stone-zeng.github.io/fduthesis/2018-05-13-install-texlive-ubuntu/

安装tex Live 知道。



写入数据出现：

```
InfluxDBClientError: 400 ("error":"partial write: field type conflict)
```

暂时行将数据格式转化为float类型。

notebook 再现查看ppt 插件出现 css加载出错。



##### 1105

写入数据再次现：

```
error":"partial write: field type conflict: input field \"DRUM-LENGTH\" on measurement \"T46\" is type integer, already exists as type float dropped=3000"}
```



静态文件一直加载不了：

1. css文件不会经过模板编译， 所以static_url（）不好使。
2. torndo的静态文件默认路由匹配为static，多一个字母都不行， 需要设置static_url_prefix = '/statics'， 这样才可以。
3. 图片加载路径要以**斜杠**开头， 不然tornado默认会再加上一个**/static/css**。



ubuntu 背景图片路径： /usr/share/background



css 改变图片颜色 https://juejin.im/post/5ba21d78f265da0af0337fe3

反转颜色：

​    filter: invert(100%);



##### 1106

安装PlayOnLinux 安装一些软件的图像化软件， 安装photoshop。

启动直接点击install 跳出页面， 加载时间较长。

安装nbviewer 环境包， 出现gcc 失败。

```
 sudo apt-get install libmemcached-dev zlib1g-dev python3-dev
 # 需要此依赖项容器
```

再次出像npm 包。使用conda isntgll

```
conda install -c conda-forge nodejs
conda install -c conda-forge invoke

```



##### 1107

redmine issue建立。

需要安装 git

pip 安装： quandl-3.4*； plotly=3.4.0

plotly 安装在Lab上需要依赖， 并使用以下安装JupyterLab扩展：

```
export NODE_OPTIONS=--max-old-space-size=4096

jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.38 --no-build

jupyter labextension install plotlywidget@0.5.0 --no-build

jupyter labextension install @jupyterlab/plotly-extension@0.18 --no-build

jupyter labextension install jupyterlab-chart-editor@1.0 --no-build

jupyter lab build

unset NODE_OPTIONS

# 静态文件导出需要 psutil
conda install -c plotly plotly-orca psutil
pip install psutil
```



pip +git 安装：

```
pip install git+https://github.com/influxdata/influxdb-python.git  == 5.2.0
```

theano : 注意需要gcc 倚赖项。

conda 安装:  matplotlib=3.0.0，



在dockerfile 中使用apt-get中需要选择的输入可以使用以下方式：

```
echo "选择" | apt-get install ...
```



 ##### 1108

容器版本及内容简述：

sunxr/dass:V0.1 :

pandoc, Tex Live, 没有环境变量， 不可用

sunxr/dass:V0.2:

pandoc， Tex Live 环境变量设置完成， 导出PDF功能可以使用。

sunxr/dass:V0.3

git,bokeh， influxdb， theano， pymysql， jupyterlab-git， matplotlib， quandl， pandoc， Tex Live，模型功能，

sunxr/dass:V0.4:

git,bokeh， influxdb， theano， pymysql， jupyterlab-git， matplotlib， quandl， pandoc， Tex Live。 取出以上模型功能，其他都在。



##### 1109

matplotlib 中文显示， 使用pyplotz插件。

使用系统用户认证， 但是每个人有独立的容器。并且可以创建系统用户。



##### 1112

创建一个用于系统用户的镜像， 测试以下。

写以下需要测试的内容。

nginx 代理中增加client_max_body_size 128M；设置上传文件大小。默认是1M。

redmine 邮箱配置：

```
  email_delivery:
    delivery_method: :smtp
    smtp_settings:
      ssl: true
      address: "smtp.163.com"
      port: 465
      domain: "smtp.163.com"
      authentication: :login
      user_name: "sunxiaoran9@163.com"
      password: "qwer142536"
 # redmine 邮箱配置注意点
 # ssl 开启，不开启就不能从465发送， 默认的25被阿里云封了。
 # method 不需要使用async_smtp 异步发送。
```

##### 1113

更换docker存放数据位置， 因为操作失误删除了一些东西， 导致docker进程运行错误。需要重新安装docker。hub服务只需要配置中更改镜像名称就好。

重新启动服务就可以正常运行了。

导致数据丢失，自己太着急了， 忘记数据卷还在docker的目录下。不能直接删除。需要备份才行。



打开系统设置->键盘，进入shortcuts选项

点击 + 号，Name选项随意；Command选项填： gnome-screenshot -a，-a 表示自由截图

设置的快捷键，比如Ctrl+Alt+A



线上镜像出现git不能使用的问题, 没有安装后台处理扩展。

增加了两个命令再次生成了镜像。sunxr/dass:V0.5



##### 1114

镜像的git 后台处理版本不是最新版，更换安装方式， 获取最新版的服务。

sunxr/dass:0.6 容器版本。



- [Redmine](http://www.redmine.org/)

  > 是一个网页界面的项目管理与缺陷跟踪管理系统的自由及开放源代码软件工具。它集成了项目管理所需的各项功能：日历、燃尽图和甘特图 以协助可视化表现项目与时间限制，问题跟踪和版本控制。此外，Redmine 也可以同时处理多个项目。

- [Python](https://www.python.org/)

- [itChat](https://github.com/littlecodersh/ItChat)

  > 是一个开源的微信个人号接口，使用 python 调用微信从未如此简单。

- [python-redmine](http://python-redmine.readthedocs.io/index.html)

  > is a library for communicating with a Redmine project management application.



尝试增加一个再现ppt扩展。



##### 1115

- Alt+r: Enter/Exit RISE
- Space: Next
- Shift+Space: Previous
- Shift+Enter: Eval and select next cell if visible
- Home: First slide
- End: Last slide
- w: Toggle overview mode
- ,: Toggle help and exit buttons
- . or /: black screen
- Not so useful:
  - PgUp: Up
  - PgDn: Down
  - Left Arrow: Left *(note: Space preferred)*
  - Right Arrow: Right *(note: Shift Space preferred)*
- With chalkboard enabled:
  - [ toggle fullscreen chalkboard
  - ] toggle slide-local canvas
  - \ download chalkboard drawing
  - = clear slide-local canvas
  - \- delete fullscreen chalkboard

以上为notebook的再现slide 展示快捷键操作。

导出slide lab和notebook都支持，导出HTML不行，只能notebook导出。

本地展示slide需要在同级目录下拥有relveal.js, zaigithub上下载源码在统计目录即可。

html还会出现代码样式。



html 隐藏https://blog.csdn.net/code_game/article/details/60977255

github上有一个写好的一个模板。其中会隐藏调代码行。

使用命令行导出一个html， 实现动态隐藏代码栏功能。

https://nbconvert.readthedocs.io/en/latest/config_options.html

nbconvert 文档。可以增加好像可以增加配置文件。

网络连接经常断开， 将/etc/ppp/options 中 的lcp-echo-failure 值修改为较大在的值。 改为40.



修改iwconfig 中的power management。将开启改为关闭。

命令:`sudo iwconfig wlp2s0 power off`



##### 1119

hide_code, notebook隐藏代码插件， 支持再线查看选择需要隐藏的。并导出隐藏的文件。

修改配置文件，增加slide导出使用网络资源。可以使用导出一个静态文件。并随时再线查看。

 指定隐藏某一项。导出的文件不会动态交互式隐藏代码。



##### 1120 

ubuntu 使用gparted，制作windows启动盘。

https://www.linuxidc.com/Linux/2017-10/148157.htm # windows系统盘.



##### 1121

slide 配置。没有案例。只能使用notebook设置slider。lab不能使用。

##### 1122

生成几个案例，为作修改的，使用模板生成的，还有slider。但是自动导出无法实现。

##### 1123

ubuntu18 fcitx 不能在浏览器中使用

slide 在线默认样式设置，livereveal.json的文件移动到上一层文件目录上。

默认生成的文件在`.jupyter/nbconfig`目录下。需要移动到`.jupyter`目录下即可在线使用配置样式。

打包oee计算方式，配合修改。

注释npm 安装



##### 1124

尝试配置setup文件的npm安装，没有成功。



##### 1126

jupyterlab sublime 代码提示

```
# 插件：
# https://github.com/ryantam626/jupyterlab_sublime
# https://github.com/jwkvam/jupyterlab-vim
```

vim 编辑安装一个插件就好。



ubuntu 悬浮翻译软件

```
# dict remote
https://drive.google.com/drive/folders/0BzrQwK2v03aKWjlsQ3NsaWJKalU

```

##### 1127

编写数据链接单例。完善代码。

到处中文：

切换nbconvert为最新版，使用git安装：

```
pip install git+https://github.com/jupyter/nbconvert.git
```

安装xetex

```
sudo apt-get install texlive-xetex
```

安装texlive组建：

```
sudo apt-get install texlive-latex-extra texlive-bibtex-extra
```

http://jun369.me/2018/10/22/latex/ 尝试失败。



2. 尝试增加字体

```
# 安装texlive
sudo apt-get install texlive-xetex
# 安装pandoc
sudo apt-get install pandoc
# 安装微软雅黑字体（msyh.ttf）[其他中文字体亦可]
＃下载微软雅黑
sudo cp msyh.ttf / usr / share / fonts
sudo fc-cache -f -v
# 修改当前环境下的article.tplx
#~\Anaconda3\pkgs\nbconvert-5.4.0-py37_1\Lib\sitepackages\nbconvert\templates\latex\

# @article.tplx
add
\usepackage{xeCJK}
\setCJKmainfont{Microsoft YaHei}  # match font name
after
\documentclass[11pt]{article}

```



##### 1128

中文导出最终只是修改模板中使用的插件。

找的路径不对。

anaconda的默认环境的程序在以下路径。

```
~/anaconda3/lib/python3.7/site-packages/nbconvert/templates/latex
```

```
修改 \Anaconda3\Lib\site-packages\nbconvert\templates\latex\article.tplx 文件
把 \documentclass[11pt]{article}
替换为
\documentclass{article}
\usepackage{ctex}
ctex为中文编译包
```



visual studio code软件。

python 文件出现了一个pylink 扩展安装失败。

需要使用 ctrl + shift + p 输入 Python：Select Linter 之后选择pep8规则。

deng 功能尚未弄好，需要什么配置文件。 



jupyter 安装typescript, 和javascript kernel:

```
sudo -H npm install -g itypescript
# and
sudo -H its --ts-install=global
```

```
sudo npm install -g ijavascript
ijsinstall
```



chrome 快捷翻按键：文档标识按键 + T。



docker-compose 需要独立安装：

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

以上为安装命令。

安装完成之后为二进制文件增加可执行权限。

```
sudo chmod +x /usr/local/bin/docker-compose
```

测试安装：

>  docker-compose --version



**sharelatex**

创建管理员用户：

```
docker exec sharelatex /bin/bash -c "cd /var/www/sharelatex; grunt user:create-admin --email Sunxrs@gmail.com"
```

最后的邮箱在默认没有的情况下，会自动成为管理员。并返回一个url。使用url登录并设置密码即可。

更新为完整版，更新命令：

```
tlmgr install scheme-full 
```

执行之后出现了一下报错：

```
tlmgr: Remote repository is newer than local (2017 < 2018)
Cross release updates are only supported with
  update-tlmgr-latest(.sh/.exe) --update
Please see https://tug.org/texlive/upgrade.html for details.
```

此问题是版本不能升级，需要将存储库等级降至2017版本。之后再次执行安装命令。以下命令为降低版本的命令。注：**此命令为在容器内部执行的**.

```
sudo tlmgr option repository ftp://tug.org/historic/systems/texlive/2017/tlnet-final
```



