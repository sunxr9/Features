# GitLab 配置自定义 https 证书

使用 OpenSSL 生成证书，配置 GitLab。

## 环境

使用 Docker  容器化部署`gitlab/gitlab-ce` ，Docker 運行環境爲 Ubuntu 18.04 Server。

证书生成工具为 OpenSSL。



## 证书生成

 使用 OpenSSL 生成证书， 此证书不是浏览器信任，访问时需忽略浏览器所提示的警告。

### 安裝 OpenSSL

```
sudo apt install openssl
```



### 创建证书存放目录

自定义证书用于 GitLab 配置 https 。本次操作在 GitLab 配置文件目录下进行。

执行以下命令创建目录并进入：

```bash
mkdir ssl
# 进入 ssl 目录
cd ssl
```



### 创建服务器私钥

需要输入口令进行创建，稍后进行密码取消。

```bash
openssl genrsa -des3 -out server.key 1024
```



### 创建签名请求的证书

需要输入服务器私钥口令、国家、省份城市等信息。

```bash
openssl req -new -key server.key -out server.csr
```

### 取消服务器私钥口令

1. 备份私钥（csr）文件

   ```bash
   cp server.key server.key.org
   ```

2. 去除口令

   ```bash
   openssl rsa -in server.key.org -out server.key
   ```

### 标记证书使用上述私钥和CSR



```bash
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```



## 编辑 GitLab 配置

修改 GItLab.rb 文件，增加以下配置：

```config
# GitLab 地址，
external_url "https://139.198.188.123"
# Nginx redirect
nginx['redirect_http_to_https']= true
nginx['ssl_certificate']= "/etc/gitlab/ssl/server.crt"
nginx['ssl_certificate_key']= "/etc/gitlab/ssl/server.key"
```

