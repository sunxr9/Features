# grafana

使用 grafana v6.2.1记录．

## 部署

当前使用 Grafana docker 镜像进行测试使用以及练习，使用以下命令获取 Grafana docker 镜像：

```
docker pull grafana/grafana
```

由于是测试使用，所以运行容器不进行宿主机数据卷持久话保存，只进行端口映射，将服务暴露与宿主机上：

```shell
docker run -d --name grafana -p 3000:3000 grafana/grafana
```

并使用 -d 参数后台运行，不进行日志输出．但关机之后容器会停止运行，如需恢复上次测试使用容器，请执行以下命令，再次运行 Grafana 测试使用容器．

```bash
docker start grafana
```



 ## 使用

打开浏览器访问 `http://localhost:3000`， 将看到登录界面，首次登录需要重置管理员 `admin`用户密码，默认密码为 `admin`，个人修改为 `142536`．

### 添加数据源

登录完成后，在创建地一个仪表板之前，需要添加数据源，将光标移动到侧面菜单上的 Configuration(齿轮图标) ，它将显示配置菜单。如果侧面菜单不可见，单击左上角的 Grafana 图标。配置菜单上的第一项是数据源，单击它，将进入数据源页面，可以在其中添加和编辑数据源．

1. 单击添加数据源（绿色按钮）
2. 选择需要添加的数据源类型（数据库类型）
3. 填写数据库链接信息

参照[PostgreSQL数据源选项](<https://grafana.com/docs/features/datasources/postgres/#data-source-options>) ，其中需要注意的是 **SSL Mode** 选项需要注意，当前测试使用选择的是**disable** ．选择其中`verify-ca` 选项在点击保存和测试按钮会在按钮上方出现错误`509: certificate signed by unknown authority`， 选择其中`verify-full` 选项在点击保存和测试按钮会在按钮上方提示错误`x509: cannot validate certificate for 139.224.9.212 because it doesn't contain any IP SANs`．

只有`disable` 以及`require` 选项在点击保存和测试按钮会在按钮上方出现 `Database Connection OK` 提示．

### 创建新的仪表板

将光标移至左侧菜单栏 Create(加号) 图标，它将显示添加仪表版菜单．点击 Dashboard 选项出现以下画面：

![1559634247099](image/grafana_dashboard.png)

最顶部**仪表板功能键**依次为：

1. 侧面菜单栏切换(grafana图标)：这会切换侧面菜单，使您可以专注于仪表板中显示的数据。侧边菜单提供对与仪表板无关的功能（如用户，组织和数据源）的访问。
2. 仪表板下拉菜单（四个方块图标+New dashboard[仪表板名称]）：此下拉列表显示您当前正在查看的仪表板，并允许您轻松切换到新的仪表板。您还可以在此处创建新的仪表板或文件夹，导入现有仪表板以及管理仪表板播放列表。
3. 添加面板（柱状图+加号图标）：将新面板添加到当前仪表板
4. Star Dashboard(五角星图标)：Star（或unstar）当前仪表板。默认情况下，加星标的仪表板将显示在您自己的主页控制台上，是标记您感兴趣的仪表板的便捷方式。
5. 共享仪表板（共享图标）：通过创建链接或创建其静态快照来共享当前仪表板。确保在共享之前保存仪表板。
6. 保存仪表板（磁盘图标）：当前仪表板将与当前仪表板名称一起保存。
7. 设置（齿轮图标）：管理仪表板设置和功能，如模板和注释，。
8. 循环视图模式（电脑屏幕图标）：全窗口查看仪表板．并提供定时，时间段等．
9. 时间选择框（钟表图标+时间内容）：为循环视图模式提供时间选择功能．
10. 时间范围缩小（放大镜图标）：缩小时间范围按钮，同时也支持使用快捷键 **Ctrl + z** 进行操作．
11. 刷新和定时（循环双箭头+倒置三角形）：刷新当前页面，获取新数据．并可设置定时刷新，通过点击定时按钮（倒置三角形图标）选择自动刷新时间．

#### 仪表板设置

当前测试使用，修改了以下内容：

点击设置按钮，其中选项包括以下内容：

+ General : 设置仪表板的基础信息．当前仪表版名称，详情描述，标签，文件夹，是否可编辑以及时间刷新选项．
+ Annotations:  注释设置，这是
+ Variables: 变量设置
+ Links
+ Versions : 当前仪表板的所有修改历史．
+ Permissions: 当前仪表板的权限管理
+ JSON Model : 定义仪表板的数据结构。包括设置，面板设置和布局，查询等。

进行配置仪表板信息，只修改名称为 test ，点击保存，弹出提示框，可填写此次修改内容备注，再次点击保存，即可修改成功，所有的修改记录都可设置中的历史项进行查看．

#### 创建展示面板

点击添加面板按钮（**仪表板功能键**，3），弹出以下画面：

![添加展示面板](image/add-panel.png)

**添加查询** 和 **选择可视化** 按钮都可直接进入面板编辑页面．但这只是第一次创建的时候进入编辑页面的方式，在首次编辑完成保存之后，想要再次进入编辑页面，就需要单击**面板的标题** ，会显示一个菜单，点击其中的 `Edit` 选项打开当前面板的其他配置选项．

点击添加查询按钮，进入面板数据源查询编辑页面：

![数据源查询编辑](image/grafana_add_query.png)

点击选择可视化按钮进入选择可视化样式界面，根据需要展示的数据，选择合适的展示样式，默认展示样式如下：

![可视化样式选择](image/grafana-choose_visualization.png)



请注意上图左侧下方四个选择按钮，负责展示面板的设置，自上至下分别为：

+ 查询设置
+ 可视化设置
+ 一般设置
+ 告警设置



##### 查询设置

编辑当前面板需要展示的数据源的查询规则．grafana 的展示数据依照SQL查询规则，用户通过自定义查询规则进行查询，增加了数据的灵活度，但是需要有一定的SQL语句基础，懂得基础语法．否则很难进行使用．

Grafana 支持原生SQL语句编写，再次不做说明，在查询设置中`Queries`中最后一行有切换按钮，点击**`Edit SQL`**进行切换．

当前主要说明Grafana自带的查询编辑器的使用．

![1562809337926](image/queries.png)

以上为查询编辑器主要内容：

首先选择查询的数据源，查询编辑器的左上角*Query* 项后有选择框，可点击选择设置的数据源．

FROM：选择需要查询的表名称，在点击编辑后会出现当前链接数据源的表名称提示．如没有提示建议检查配置的数据库信息是否正确或链接是否成功．

Time column: 时间列名，上述需要查询的表中必定要有时间列，否则无法进行使用．

Metric column:  可空，提示上说是**Column to be used as metric name for the value column.** 要用作值列的度量标准名称的列。不太清楚如何使用．

SELECT：需要查询的数据表字段名称或者需要展示的表字段名称．并且Grafana同样封装了SQL中的一下聚合选项，只需要点击SELECT选项行厚的加号进行选择即可，但是需要在查询的表字段后添加．其中需要说明的是**Alias**选项．Alias选项为需要查询的表列名在当前Grafana中取别名，这个名称将会是在仪表板中的数据源的名称．图中为溶解氧的示例，将查询的字段**dbl_v**，重命名为溶解氧，趋势图的左下方显示的即为溶解氧：![1564036427971](image/grafana_select_query_alias.png)

WHERE: 查询的筛选条件，可空．目前Grafana提供了两个相关选择，一个是Grafana自定义的宏方法，另一个Expression是SQL中的筛选格式．点击添加按钮之后，Grafana会有一定的格式提示，格式为：表字段　对比符号（>, <,IN等）对比值，上图所示．

GROUP BY: 进行分组的字段,.

Format as: 有两个选项 ,当前使用的是Time Series选项, Table在当前的时间序列数据中好像无法使用.

Edit SQL: 切换当前查询数据源的的编辑模式, 上图为Grafana格式化的编辑模式, 切换后可直接编辑SQL语句.

Show Help: 帮助文档,以及一些Grafana自定义的宏函数的使用简述.

Generated SQL: 查看当前编辑的查询语句生成据SQL语句.

##### 可视化设置

设置当前仪表板展示样式.

![1564040851161](image/grafana_visualization.png)

上述是Grafana可视化设置的部分截图, 图中显示的分为两个部分: 1, 可视化样式. 2, 仪表板轴设置,另未在图中展示的为图例设置.

可视化样式设置中又可细分为:

+ 画图模型(柱状图, 线图, 点图)
+ 模式选项(设置画图模型的参数,在不同的模式下有不同的选项)
+ 悬停工具(鼠标悬停显示设置)
+ 数据控制

仪表板轴设置, 其中主要是针对Y轴的设置,包含单位, 最大值最小值, 标签等, X轴较为简单.

图例设置, 主要设置在仪表板中的数据显示设置, 显示数据的名称,具体数值, 最大值等内容, 在上图中的左部中间部分的溶解养显示即为图例中的设置.

##### 一般设置

设置当前仪表板的title, 以及跳转链接:

跳转链接的配置如下图中的Drilldown Links:

![1564047285665](image/grafana_link.png)

其中选择链接的类型, 目前有dashboard 和 absolute两种, 最简单的就是上图所示, 只需要将需要跳转的dashboard名称填写进Dashboard中即可, 填写完成后, Title项默认与Dashboard中的一样.

完成之后在仪表版的左上角的跳出图标就可以使用了, 首先悬停在图标上, 将会显示可以跳转的链接,之后点击即可.

##### 警告设置 

设置关于数据的警告规则,

![1564048693512](image/grafana_alert.png)

