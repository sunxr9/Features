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

测试添加ｊｓ处理路由，使用官方文档上的方式添加可以，使用ｎｏｄｅ模块添加处理无法响应．

稍微总结一下半年的主体工作成果．已推送．



##### 1217

练习ｊｓ，已知问题基础清单．

thingsboard　服务挂掉了，尝试修复．

##### 1218

尝试修改了端口，

修改日志级别．

在thignsboard.conf 中增加了一个

```
# Update ThingsBoard memory usage and restrict it to 150MB in /etc/thingsboard/conf/thingsboard.conf
export JAVA_OPTS="$JAVA_OPTS -Dplatform=rpi -Xms256M -Xmx256M"
```

将数据卷转移至扩展卷，





Could not obtain connection to query metadata : java.lang.OutOfMemoryError: Java heap space

无法获取与查询元数据的链接．

2018-12-18 11:01:44,288 [localhost-startStop-1] INFO  org.hibernate.cfg.Environment - HHH000206: hibernate.properties not found

找不到的问题．

Disabling contextual LOB creation as connection was null

需要尝试：

1. 数据文件太大．
2. 链接太多．

最后的结果为数据文件太大的问题，需要把数据文件重置，目前只能恢复服务，不能恢复原有的数据．数据文件为ｓｑｌ语句文件，线上本地均有本分．



##### 1219

数据文件尝试导入数据库．

rateno 线上编辑，账户密码都是在配置文件中的，没有注册．只有登录的用户才可以在线编辑．

内置的google oauth认证没有使用．



##### 1220

代理无法链接，测试重新安装chromium的代理插件，switchyOmega.在配置本地代理即可．

火狐代理设置，选择preferences,在General中找到NetWork,点击设置，选择`Manual proxy configuration`,在SOCKS Host中写入127.0.0.1, 端口为1080，点击确认即可．

UEFI，模式没有usb启动选项．需要选择传统模式．之后才能进行选择ｕsb选项启动．

启动按F12,选择ｕsb启动．

##### 1221

无法安装系统的原因，注意ＲＡＩＤ名称，应该默认是０开始，不能跳过，不然检测不到．

恢复出场设置ＢＯＩＳ，F2进入System Setup,将键盘上的三个指示灯全部按亮，

`ALT　＋　F`恢复，`ALT + B`保存退出．

调整硬盘分区表．

更换显卡插口，

##### 1224

当您看到如图所示的“ **Ubuntu** ” 选项时，按键盘上的“ **E** ”键．

在编辑器中，使用箭头键找到以“ **linux / boot / vmlinuz** ***” 开头的行的结尾．

**在行尾**键入“ **nomodeset** ”行选项。

之后按`ctrl + x`，正常启动到正常的安装或实时环境．

**永久"nomodeset"选项

1. 打开终端并输入“ **sudo gedit / etc / default / grub** ”
2. 如果有提示，请输入密码。
3. 将光标移动到如下**所示**的行（**图4**）：
   **GRUB_CMDLINE_LINUX_DEFAULT =“quiet splash”** 

1. 
   点击“ **保存** ”。
2. 关上窗户。
3. 在终端中，键入“ **sudo update-grub2** ”并按Enter键。
4. 完成后，您应该可以通过此更改重新启动计算机。

重新安装１８版本ｕbuntu,手动分区安装，

/ 目录100G

/swap /68343M

/boot /5120

/home /剩余所有．



重启还是在启动页面停止．无法进入系统页面．

使用添加内核参数进行尝试，在进入选项页面之后选择`ubuntu`,按下ｅ，进入编辑，在quiet和splash 后添加以下内容．

使用 `nomodeset` 内核参数的同时，Intel 卡需要添加 `i915.modeset=0`， Nvidia 卡需要添加 `nouveau.modeset=0`. Nvidia Optimus 双显卡系统，需要添加三个内核参数：

```
"nomodeset i915.modeset=0 nouveau.modeset=0"
```



尝试进入命令行界面．进行修复图形界面．

1. 同时按下 alt + ctrl + F1，屏幕出现 tty1，输入用户名和密码登录；
2. 执行如下命令：

```shell
sudo stop lightdm

sudo apt-get update

sudo apt-get upgrade

sudo apt-get install --reinstall lightdm

sudo start lightdm
```

尝试添加一个EFI启动路径，使用grub64.efi文件启动,最后还是无法正常通过图形界面使用．

**尝试增加grub启动引导文件**

```
开机，在显示出引导选项菜单的时候按e
进入引导文本编辑页面
找到类似如下内容的一行
linux        /boot/vmlinuz-4.9.0-deepin13-amd64 root=UUID=57d9aa6c-2452-4374-b4b8-bbd81a2975c2 ro splash quiet
在 quiet 的后面空一格 加入 acpi_osi=! acpi="windows 2009"
加好以后，按F10保存开机
这样应该就可以进入系统了
然后打开终端，依次输入：
sudo su
sudo gedit /boot/grub/grub.cfg
接着，在弹出的文本页面里，再次找到
linux        /boot/vmlinuz-4.9.0-deepin13-amd64 root=UUID=57d9aa6c-2452-4374-b4b8-bbd81a2975c2 ro splash quiet
同样的在 quiet 后面空一格，加入 acpi_osi=! acpi="windows 2009"
保存，关闭
接着，在终端里输入
sudo gedit /etc/default/grub 
在弹出的文本页面的末尾加入
GRUB_CMDLINE_LINUX_DEFAULT="$GRUB_CMDLINE_LINUX_DEFAULT "'acpi_osi=! acpi_osi="Windows 2009"'
这样以后就可以正常开机了
如果出现风扇狂转的情况
那么就点开启动器-系统管理-驱动管理器
在驱动管理器里把两项驱动都点选上
安装好以后重启
如果重启的时候又出现卡logo不能进入系统的情况
那么就按照之前的办法再处理一次
```

尝试无效．

可以使用**可以使用usb**启动,然后进行修复，不做尝试了，等联网之后进行尝试．

已经搜索的还没有尝试的

```
https://www.reddit.com/r/Ubuntu/comments/8hqblq/ubuntu_1804_purple_login_screen_problem/

```



扩展屏幕，默认HMDI屏幕为主屏幕，不需要设置．

https://cloud.tencent.com/developer/article/1058322 vim 各项配置．

https://cloud.tencent.com/developer/article/1058322 vim 配置．

下季度需要做的更新项．



##### 1225

gitlab 绑定的pdf.js　不能显示中文，主要针对的是**LaTeX**编译的中文显示．

https://gitlab.com/gitlab-org/gitlab-ee/issues/8267　GitLab官网中提供的一个bug,目前还没有解决．



<<<<<<< HEAD
计划：

jupyter Lab 更新

docker 容器更新

##### 1226

jupyter notebook 启动的时候出现自动打开的不是链接，而是一个文件：

```
To access the notebook, open this file in a browser:
        file:///run/user/1000/jupyter/nbserver-10288-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/?token=b5595afdfc8b379e3aa3d9d183d5c4d963517db7bda9d811
```

需要手动的打开链接才可以使用．

尝试一下方式：

- conda update all packages　升级全部的插件，包．
- disable all jupyter extension 关闭全比扩展．
- 重新安装jupyter.
- 使用`conda list`查看包名，选择重复的包其中一个卸载．

最终为重新安装anaconda,就可以了．

就只有第一次可以，之后启动又回到上边的情况了，

**需要重新安装RISE**

conda install -c conda-forge rise



安装RISE在线控制扩展．

conda install -c conda-forge jupyter_nbextensions_configurator 

之后重启jupyter,在notebook页面中的编辑栏最后增加了配置选项．



在线展示的一个工具，decktape．

安装和运行（需要npm）:

- npm install -g decktape
- 运行在终端中直接输入`decktape`即可．

> 注意点：不可有代理，不然会安装失败，出现`puppeteer@1.9.0 install: node install.js`的错误．

https://github.com/damianavila/RISE/pull/381　jupyter lab 安装rise.



##### 1227

在需要展示的文件同级目录下创建和文件名称一样的css文件，在其中自定义html样式．

主要点为代码输入框隐藏，因为css优先级的问题，使用**display: none**不可行，最后使用的结果为一下方式：

```css
.input {
    position: absolute;
    top: -99999px;
    left: -99999px;
}
```

将信息定位在页面之外，缺点为在聚焦的时候会出现焦点转移．



##### 1228

隐藏代码文件加载之后就会一直在，会影响到notebook的显示，需要在推出的时候增加删除加载文件．

尝试增加不可以，加载的样式信息已经在浏览器缓存中，无法清除．

下季度计划要开始了．



##### 1229

以编辑模式安装RISE.

```shell
git clone https://github.com/damianavila/RISE.git
# 进入包目录
pip install -e .
npm install
npm run build-reveal
npm run reset-reveal
npm run build-css
npm run watch-less

# 启用扩展
jupyter-nbextension install rise --py --sys-prefix --symlink
jupyter-nbextension enable rise --py --sys-prefix
```

在main.js文件增加以下代码，增加一个可动态显示和隐藏代码的图标按钮：

```javascript
  // add hide botton
  function cellHide() {
    var hide_button = $('<i/>').attr('id', 'cell_hide')
        .attr('title', 'Hide Cell')
        .addClass('fa fa-eye-slash fa-4x')
        .css('position', 'fixed')
        .css('bottom', '0.6em')
        .css('left', '1.4em')
        .css('opacity', '0.5')
        .css('z-index', '30')
        .click(
          function () {
            var tag = $('.input').hasClass('input_hide');
            if (!tag) {
              $('.input').addClass("input_hide");
              hide_button.attr('title', 'Show Cell');
            } else {
              $('.input').removeClass('input_hide');
              hide_button.attr('title', 'Hide Cell');
            }
          }
        );
    $('.reveal').after(hide_button);
  }

// 在revealMode() 函数中增加事件．
  function revealMode() {
    // We search for a class tag in the maintoolbar to check if reveal mode is "on".
    // If the tag exits, we exit. Otherwise, we enter the reveal mode.
    var tag = $('#maintoolbar').hasClass('reveal_tagging');

    if (!tag) {
      // Preparing the new reveal-compatible structure
      var selected_slide = markupSlides($('div#notebook-container'));
      // Adding the reveal stuff
      Revealer(selected_slide);
      // Minor modifications for usability
      setupKeys("reveal_mode");
      buttonExit();
      buttonHelp();

      // registed hide botton
      //　进入展示的时候增加隐藏和展示事件．
      cellHide();

      $('#maintoolbar').addClass('reveal_tagging');
    } else {
      var current_cell_index = reveal_cell_index(Jupyter.notebook);
      Remover();
      setupKeys("notebook_mode");
      $('#exit_b').remove();
      $('#help_b').remove();

      // remove hide botton;
      //　退出展示的时候删除隐藏事件．
      $('#cell_hide').remove();
      $('#maintoolbar').removeClass('reveal_tagging');
      // Workaround... should be a better solution. Need to investigate codemirror
      fixCellHeight();
      // select and focus on current cell
      Jupyter.notebook.select(current_cell_index);
      // Need to delay the action a little bit so it actually focus the selected slide
      setTimeout(function(){ Jupyter.notebook.get_selected_cell().ensure_focused(); }, 500);
    }
  }
```

不过使用pip安装的RISE nbconfig在线配置不能使用．

reveal.js背景，图的控制，字体大小．字体．