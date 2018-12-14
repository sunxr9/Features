##### 1201 

xrandr 双屏幕设置

xrandr -q 查看当前的屏幕信息。

xrandr --output [屏幕名称] --off # 关闭命令。

xrandr --output [屏幕名称] --left-of [另一个屏幕名称] --auto

将另一个显示左边，并以扩展显示。

容器中字体文件位置：

```
/usr/share/fonts/truetype/dejavu or liberation
```



##### 1204

setup文件注意点。

使用pip+git进行安装的时候出现一下bug：

```
AssertionError: yofc-oee .dist-info directory not found
```

主要由一下集中原因导致：

1. 在setup文件中编写了npm安装函数，并在setup传参中注册了。

2. 在setup文件中使用

   ```
   if --name-- ==‘__main__’
   	setup()
   ```

   在次执行出的问题。

3. 包内不可出现自运行函数，以及任何自运行操作。

在打包晚成之后使用一下方式测试。

1. 运行`python setup.py test`。

   结果最后一个单行必定只有**`OK`**。

2. 运行`python setup.py develop`。

   结果的注意点为测试名称：

   ```
   Using /home/sunxr/anaconda3/lib/python3.7/site-packages
   Finished processing dependencies for yofc-oee==0.5.1
   ```

   在这里为最后的yofc-oee==0.5.1。必须是项目名称对应。不可是**UNKNOWN**==0.0.0。



##### 1205

录屏删除功能带修改.



##### 1206

判断系统是否支持。

setup文件测试。除了test，develop，另外的**`cmdclass`**中命令，可以单独测试，使用

`python setup.py js [此为cmdclass中键名]`

raneto docker容器启动命令。需要在`git_data/raneto-docker`下执行。

```
docker run -v `pwd`/content/:/data/content/ -v `pwd`/images/:/data/images/ -v `pwd`/config/config.default.js:/opt/raneto/example/config.default.js -p 3000:3000 -d appsecco/raneto
```

修改一下文件映射，在做启动。

```
docker run -v `pwd`:/data/ -v `pwd`/config/config.default.js:/opt/raneto/example/config.default.js -p 3000:3000 -d appsecco/raneto
```

配置文件中的**`public_dir`**在最后的位置被覆盖了。所以要在最后修改。

##### 1207

录屏，重置录屏说明。

##### 1210

查看端口`sudo lsof -i :80`

nginx 配置无法生效，一直是welcome 界面,无法代理，搜了很长时间，出现一个帖子。

首次配置需要注释掉最后的两句话：

```
# include /etc/nginx/conf.d/*.conf;
# include /etc/nginx/sites-enabled/*;
```

再此之后进行添加配置，并重新加载。`nginx -s reload`。

如重新加载出错。

```
 nginx:[error] open() "/run/nginx.pid" failed (2: No such file or directory)
使用以下命令即可解决：
nginx -c /etc/nginx/nginx.conf
nginx -s reload
```



端口查询，`netstart -an | grep port`。

但是之后需要使用浏览器打开链接，链接上才算生效。最后不弄了，可能是容器和阿里云服务的双重因素导致的。

使用源码安装可以访问，但是出现资源加载错误。

raneto 首次执行需要执行独立命令：**`npm run gulp`**.注意目录还是在存储库内部。

配置文件修改：

base_url:要写服务器完整路径。http:106.14.221.57/docs

public_dir：是很重要的配置，资源加载，script，图片都在里面。

nginx：location 的配置需要使用完整的匹配。前后都要有斜杠。



##### 1213

pycharm 破解。

下载破解程序，已保存在百度云盘。

在pycharm目录下的bin中的两个文件`pycharm.vmoptions`和`pycharm64.vmoptions`添加一下内容:

```
-javaagent:D:\你pycharm的安装路径\bin\JetbrainsCrack-release-enc.jar
```

然后在重新启动。

使用nodejs：



##### 1214

