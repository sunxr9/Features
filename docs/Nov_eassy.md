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



 