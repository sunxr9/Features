# Ngrok 和 Frp简述使用

### 原理

1. 本地内网主机和服务器A构建一条连接
2. 用户访问服务器A
3. 服务器A联系本地内网主机获取内容
4. 服务器A将获取到的内容发送给用户

## Ngrok

### 使用

打开[ngrok官网](https://ngrok.com)，登录帐号（可使用GitHub和Google帐号登录），默认跳转至个人页面，按照个人页面提示进行下载，安装，以及本地登录ngrok认证信息．

代理 ssh:

进入存放 Ngrok 文件目录，在目录下直接运行以下命令，启动 ngrok tcp 代理 本地 22 端口：

```bash
./ngrok tcp 22
```

出现如下图内容：

![1557478627086](/home/sunxr/git_data/test/docs/image/1557478627086.png)

复制图中`Forwarding`项的地址，作为ssh链接地址，端口为链接代理端口，链接案例：

```
ssh -p port username@0.tcp.ngrok.io
```





## frp

### 使用

登录[frp发布页](<https://github.com/fatedier/frp/releases>)，在服务端以及客户端分别下载与系统对应的源码，解压，然后进入项目目录.

服务端：

编辑`frps.ini`文件，可自行修改绑定端口，然后保存退出．

注：服务端只需要绑定运行端口，不需要填写 IP 地址，默认会监控当前服务器的绑定端口，允许所有 IP 访问．

```ini
# frps.ini
[common]
bind_port = 7000
```

后执行一下命令启动 frp 服务端：

```bash
./frps -c ./frps.ini
```



客户端:

编辑`frpc.ini`，在`[common]`项中填写服务端 IP 地址以及运行端口．在`[ssh]`中填写链接类型，需要映射的 IP 地址，端口，最后一项为本地的端口映射在服务端的端口：

注：客户端需要填写服务端 IP 地址．

```ini
# frpc.ini
[common]
server_addr = x.x.x.x　# 服务端 IP 地址
server_port = 7000

[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6000
```

启动客户端：

```bash
./frpc -c ./frpc.ini
```



完成以上步骤即可通过服务端 IP 地址以及上述客户端配置文件中定义的 ssh 绑定端口，链接内网机器，示例如下：

```
# 此处端口 6000 为上述客户端配置文件中［ssh］项填写的remote_port
ssh -p 6000 username@server_IP
```





