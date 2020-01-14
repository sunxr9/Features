##### 191101 

Ubuntu 图标文件存放地址：1)`/usr/share/applications/`，2) `．local/share/application`

sublime 安装扩展包：

1. 使用 `shift+ctrl+p` 或者点击导航栏 `Tools` 进入`Command palette` 
2. 首先搜索 `install package` 然后Enter进入
3. 等待下一个搜索框显示，再次搜索需要安装的扩展包才可以．

ubuntu 下LaTeX编译需要注意的条件：

+ 需要安装完整版 `sudo apt-get install latex-full` .
+ 使用xelatex 进行编译，不要使用pdflatex引擎.

如出现类似 `Package CJK Error: Invalid character code.` 的报错信息，将首行 `\documentclass{12pt,article}` 

中增加 `UTF8` 选项： `\documentclass[12pt,UTF8,fntef]{article}` 



##### 191114

ubuntu 在已有的一个分区上进行扩容，步骤如下：

+ 使用 `fdisk` 命令对需要进行扩容的设备重新创建分区
  + `sudo fdisk /dev/sda` 编辑设备
  + 查看当前设备信息 `p` ．
  + 删除原有的一个分区 `d` ．
  + 创建分区 `n` ．
  + 保存 `w` ．
+ 对分区边界进行扩展 `sudo resize2fs -p /dev/sda2` 

##### 191115

安装nbdime 提示：

```bash
jupyter nbextension enable nbdime --user --py
```





pip　包介绍

alembic                1.3.1	Alembic由[Mike Bayer](http://techspot.zzzeek.org/)开发，[Alembic](https://alembic.sqlalchemy.org/)是一个轻量级的数据库迁移工具。

%% attrs                  19.3.0	 [attrs](<https://www.attrs.org/en/stable/>)是Python软件包，它将摆脱实现对象协议（又称[dunder](<https://nedbatchelder.com/blog/200605/dunder.html>)方法）的繁琐工作，从而带回编写类的乐趣。

%% backcall               0.1.0	[backcall](<https://backcall.readthedocs.io/en/latest/>)是一个Python模块，用于编写向后兼容的回调API。也就是说，您可以在调用中添加参数，而不会破坏不需要这些新参数的第三方回调函数。

beautifulsoup4         4.8.1	[Beautiful Soup](<https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/>)是一个可以轻松从网页上抓取信息的库。它位于HTML或XML解析器的顶部，提供用于迭代，搜索和修改解析树的Python惯用法。

bokeh                  1.4.0		[Bokeh](https://docs.bokeh.org/en/latest/docs/user_guide.html#userguide)是交互式可视化工具。它提供通用图形的优雅，简洁的构造，并在大型或流数据集上提供高性能的交互性。

%% certifi                2019.9.11	[Certifi]()是精心挑选的根证书的集合，用于在验证TLS主机身份的同时验证SSL证书的可信赖性

%% certipy                0.1.3		Certipy可以简化证书创建过程。

%% cffi                   1.13.2		[cffi](<https://cffi.readthedocs.io/en/latest/goals.html>)用于Python的C外函数接口。

chardet                3.0.4		[chardet](<https://chardet.readthedocs.io/en/latest/index.html>)是Python中的字符编码自动检测。

%% Click                  7.0		[Click](<https://click.palletsprojects.com/en/7.x/>)是一个Python软件包，用于以可组合的方式创建漂亮的命令行界面，所需的代码更少。主要用于命令行界面创建工具包。

%% cloudpickle            1.2.2		[cloudpickle](https://www.pydoc.io/pypi/cloudpickle-0.3.1/autoapi/cloudpickle/index.html)可以序列化 pickle Python标准库中默认模块不支持的Python结构。

%% colorama               0.4.1		[colorama](<https://pypi.org/project/colorama/>)使ANSI转义字符序列在MS Windows，用于生成彩色的终端文本和光标定位。

conda                  4.7.12		[Conda](<https://docs.conda.io/en/latest/>) 是开源的软件包管理系统和环境管理系统，可快速安装、运行、更新软件包及其依赖包。

%% cryptography           2.8		[cryptography](<https://cryptography.io/en/latest/>)包括高级配方和低级接口，它们连接到通用密码算法。

%% cycler                 0.10.0		单个条目[Cycler](https://matplotlib.org/cycler)对象可用于轻松地在单个样式上循环。

dask                   2.8.0		Dask是用于数据分析的灵活并行计算工具，为分析提供了高级并行性。

decorator              4.4.1		[装饰器](https://www.geeksforgeeks.org/function-decorators-in-python-set-1-introduction/)是Python中非常强大且有用的工具，因为它允许程序员修改函数或类的行为。装饰器允许我们包装另一个函数以扩展包装函数的行为，而无需对其进行永久性修改。

gitdb2                 2.0.6		扩展sqlalchemy数据库的库，用于将其内容存储在git管理的文件目录中。

h5py                   2.10.0		它使您可以存储大量的数值数据，并轻松地从NumPy中操纵该数据。

imageio                2.6.1		[imageio](<https://imageio.readthedocs.io/en/stable/>)提供了一个轻松的界面来读取和写入各种图像数据，包括动画图像，体积数据和科学格式。

inflection             0.3.1		[inflection](<https://inflection.readthedocs.io/en/latest/>)是一个字符串转换库。它对英语单词进行单数和复数处理，并将字符串从CamelCase转换为underscored_string。

matplotlib             3.1.2		[Matplotlib](<https://matplotlib.org/users/index.html>)是一个Python 2D绘图库，它以多种硬拷贝格式和跨平台的交互式环境生成出版物质量的图形。

mpmath                 1.1.0		[mpmath](<http://mpmath.org/doc/1.1.0/>)用于以任意精度进行实数和复数浮点运算。

numpy                  1.17.3		[NumPy](<https://numpy.org/devdocs/>)是使用Python进行科学计算的基本软件包。

pandas                 0.25.3		[Pandas](<https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html>)是由Wes McKinney开发的高级数据处理工具。提供快速，灵活和富于表现力的数据结构，旨在使使用“关系”或“标记”数据既简单又直观。

patsy                  0.5.1		[patsy](https://patsy.readthedocs.io/en/latest)是一个Python软件包，用于描述统计模型（尤其是线性模型或具有线性成分的模型）并构建设计矩阵。

Pillow                 6.2.1		[Pillow](<https://pillow.readthedocs.io/en/stable/index.html>)包含基本的图像处理功能，包括点操作，使用一组内置的卷积内核进行过滤以及颜色空间转换。还支持支持图像大小调整，旋转和任意仿射变换等。

psycopg2-binary        2.8.4		[Psycopg](<http://initd.org/psycopg/docs/install.html>)是用于Python编程语言的最受欢迎的PostgreSQL数据库链接模块。

PyMySQL                0.9.3		[PyMySQL](<https://pymysql.readthedocs.io/en/latest/>) 是纯Python编写的 MySQL客户端库。

PyWavelets             1.1.1		PyWavelets是适用于Python的开源小波变换软件。

Quandl                 3.4.6		[Quandl](<https://docs.quandl.com/docs/getting-started>)在一个平台上统一了数百个发布者的金融和经济数据集。

scikit-image           0.16.2		[scikit-image](<https://scikit-image.org/>)是图像处理算法的集合。包括IO，形态，过滤，变形，颜色处理，对象检测等。

scikit-learn           0.21.3		[Scikit-learn](http://scikit-learn.org/stable/documentation.html)（以前称为scikits.learn，也称为sklearn）是针对Python编程语言的免费软件[机器学习](https://en.wikipedia.org/wiki/Machine_learning) [库](https://en.wikipedia.org/wiki/Library_(computing))。它具有各种分类，回归和聚类算法，包括支持向量机，随机森林，梯度提升，k均值和DBSCAN，并且旨在与Python数值科学图书馆NumPy和SciPy互操作。

seaborn                0.9.0		[Seaborn](<https://seaborn.pydata.org/tutorial.html#tutorial>)是基于matplotlib的Python数据可视化库。它提供了一个高级界面，用于绘制引人入胜且内容丰富的统计图形。

SQLAlchemy             1.3.11		[SQLAlchemy](<https://docs.sqlalchemy.org/en/13/>)是Python SQL工具箱和对象关系映射器，旨在实现高效和高性能的数据库访问。

statsmodels					用于估计许多不同的统计模型，以及进行统计测试和统计数据探索。

##### 191130

docker 推送私库重点步骤：

+ 修改docker 配置 `/etc/docker/daemon.json` 文件中增加`"insecure-registries": ["10.221.128.52","192.168.33.5"]` 选项，其中是私库的IP或者IP地址．

+ 镜像tag注意端口需要加上．

+ 登录的时候也需要加上端口

  ```bash
  docker login registory_IP:port
  ```



**bfgminer**

使用cpu挖矿的启动命令：

```bash
./bfgminer --cpu-threads 3 -S cpu:auto -o stratum+tcp://ss.antpool.com:3333 -u sunxrs9.test -p x

```

其中注意的是`-S cpu:auto` 必须写，不然cpu设置不会生效的．

