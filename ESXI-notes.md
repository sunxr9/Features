# 外网访问内网ESXI后台管理页面

对通过使用 frp 进行内网穿透，访问没有公网地址的ESXI后台管理页面的步骤进行简述．案例使用阿里云云服务器进行部署和域名解析．

## 准备工作

进行安装配置之前的准备工作如下：

1. 创建一个二级域名，并指定此二级域名解析地址（服务器IP）．
2. 开启服务器端口，阿里云默认是封闭端口．主要开启端口有以下几项：
   1. 开放访问 ESXI 后台管理页面的端口号．
   2. 开放 ssh 访问 ESXI ssh 登录的端口．
   3. 开放frp服务端监听端口，默认为7000．

3. 下载frp并进行解压（服务端和内网环境都要有），[发布地址](<https://github.com/fatedier/frp/releases>).
4. 一台代理机器，由于ESXI不能安装frp，所以需要额外的机器运行frp服务端(和ESXI处于同一网络)，对ESXI后台管理页面进行代理．

## 配置工作

### 服务端配置（阿里云服务器）

#### 配置frp 服务端

进入下载的frp目录下，编辑`frps.ini`文件，默认文件内容为：

```
[comon]
bind_port = 7000
```

上述内容表示frp服务端监听端口为7000，可自行修改frp服务端的监听端口．但是修改后需要注意在阿里云中开放对应的端口．

#### http 和 https

当前步骤可选，如不需要可跳过．

另外如果使用http或者https协议类型对ESXI后台管理页面进行访问，需要在上述配置文件中增加配置，让frp监听http和https默认端口，添加完如下：

```
[common]
bind_port = 7000
vhost_http_port = 80
vhost_https_port = 443
```

在添加完监听http和https端口配置之后，还需要确认服务器上的80和443端口没有应用占用．

#### 启动服务端

完成以上步骤即可启动服务端frp应用．在在下载的frp目录下，使用**frps**执行文件指定配置文件进行启动：

```bash
./frps -c ./frps.ini
```

### 客户端配置

#### 客户端与服务端通信

 首先进入需要运行frp客户端的机器，并并根据系统下载[frp](<https://github.com/fatedier/frp/releases>)．并解压．进入解压后的frp目录中，编辑`frpc.ini`文件, 默认携带的配置为：

```
[common]
server_addr = 127.0.0.1
server_port = 7000
```

将以上内容替换上述frp服务端运行的服务器IP地址以及上述frp服务端配置文件`frps.ini`中的监听地址．

#### ESXi 管理页面配置

上述只是frp服务端和客户端进行通信的配置，我们还需要添加对ESXI后台管理页面和ssh登录的配置．

ESXI 后台管理页面配置可使用https和tcp协议类型进行转发．主要配置内容有以下几项：

+ type: 可选https和tcp
+ local_ip: 需要进行转发的ESXI后台管理页面IP地址
+ local_port：需要进行转发的ESXI 端口，可选80和443，建议使用443．
+ remote_port: 服务端访问ESXI后台管理页面的端口，如使用https协议类型进行转发，可不填写，默认为local_port选项的设置端口．如使用tcp类型转发则需要填写，后期通过此配置的端口对ESXI进行访问．并且注意服务端的对应端口需要在阿里云中开启．
+ custom_domains: 使用https协议类型进行转发则是必填选项，为准备工作中设置的二级域名．使用tcp协议类型进行转发则可以不填写此项．

示例：

注意：首次访问建议使用全路由访问，例`https://139.196.76.242:50001`.

+ 使用tcp协议进行转发

```ini
[esxi_ui]
type = tcp # 转发协议类型
local_ip = 192.168.3.187 # 内网ESXI IP 地址
local_port = 443　# 内网ESXI 访问端口
remote_port = 50001 # 服务端的访问端口
custom_domains = agent.datasurge.cn # 绑定域名，tcp协议类型中可不填写
```



+ 使用https协议进行转发

```ini
[esxi_ui]
type = https # 转发协议类型
local_ip = 192.168.3.187 # 内网ESXI IP 地址
local_port = 443 # 内网ESXI 访问端口
remote_port = 50001 # 服务端的访问端口,https协议类型中可不填写
custom_domains = agent.datasurge.cn # 绑定的域名
```





