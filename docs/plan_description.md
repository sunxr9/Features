文件共享计划：

方法一：Jupyter插件进行发布，后台进行文件的转移，不进行任何权限设置，只是将报告文件进行转移即可。用户分享链接。

预想：

1. Lab发送文件，携带用户信息，文件信息。

2. nbviewer接收文件，区分用户，文件名。
3. nbviewer创建链接，返回链接地址。

4. Lab接受链接地址，显示分享文件或链接地址

方法二：文件分享，分享权限设置，链接分享。

1. nbviewer增加登录认证，增加权限管理，增加后台管理。

   认证方式选择，如何与分享插件关联，用户任何关联。

   权限管理级别，是否分组，几级分组。用户独立权限设置，文件分享权限设置（组内，公告，隐藏）。

2. Lab增加插件进行文件分享，携带用户信息，文件信息。

3. nbviewer接收文件，区分用户，文件名。

4. nbviewer创建链接，返回链接地址。

5. Lab接受链接地址，显示分享文件或链接地址



hub在线切换notebook和Lab：

插件形式，需要同时支持notebook和Lab。判定当前的环境，进行增加切换按钮。



Lab导出html，pdf隐藏单元格模板。

1. 模板的展示，选择。
2. 后台转化的处理。
3. 模板的编写。


