安装：

```bash
# 获取安装脚本
wget https://install.direct/go.sh
# 执行安装
sudo go.sh
```

服务端配置：

服务端只需要配置 **inbounds** 参数，接收客户端数据设置．

```json
{
  "inbounds": [
    {
      "port": 16823, // 服务器监听端口
      "protocol": "vmess",    // 主传入协议
      "settings": {
        "clients": [
          {
            "id": "b831381d-6324-4d53-ad4f-8cda48b30811",  // 用户 ID，客户端与服务器必须相同
            "alterId": 64
          }
        ]
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom",  // 主传出协议
      "settings": {}
    }
  ]
}
```

客户端配置：

客户端只需要配置 **outbounds** 参数，与服务器进行通信，所以参数需要与服务器 **inbounds** 参数内容一致．客户端 **inbounds** 参数用于和浏览器进行通信，默认与 **shadowsocks** 配置一致，所以可不用修改，使用原有浏览器的 SwitchyOmega 链接 shadowsocks 的配置即可．

```json
{
  "inbounds": [
    {
      "port": 1080, // 监听端口
      "protocol": "socks", // 入口协议为 SOCKS 5
      "sniffing": {
        "enabled": true,
        "destOverride": ["http", "tls"]
      },
      "settings": {
        "auth": "noauth"  //socks的认证设置，noauth 代表不认证，由于 socks 通常在客户端使用，所以这里不认证
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "vmess", // 出口协议
      "settings": {
        "vnext": [
          {
            "address": "serveraddr.com", // 服务器地址，请修改为你自己的服务器 IP 或域名
            "port": 16823,  // 服务器端口
            "users": [
              {
                "id": "b831381d-6324-4d53-ad4f-8cda48b30811",  // 用户 ID，必须与服务器端配置相同
                "alterId": 64 // 此处的值也应当与服务器相同
              }
            ]
          }
        ]
      }
    }
  ]
}
```

注意系统防火墙，很多系统会将访问屏蔽掉，无法进行访问．

