
##### 190603

使用**PyPI**库安装 shadowsocks 并配置：

安装：

```shell
apt install python3-pip

pip3 install shadowsocks
```

启动：

```sh
ssserver -p port -k password -m aes-256-cfb
```

执行上述命令出现错误，提示：

```bash
2019-06-02 08:31:18 INFO     loading libcrypto from libcrypto.so.1.1
Traceback (most recent call last):
  File "/usr/local/bin/ssserver", line 11, in <module>
    load_entry_point('shadowsocks==2.8.2', 'console_scripts', 'ssserver')()
  File "/usr/local/lib/python3.6/dist-packages/shadowsocks/server.py", line 34, in main
    config = shell.get_config(False)
  File "/usr/local/lib/python3.6/dist-packages/shadowsocks/shell.py", line 262, in get_config
    check_config(config, is_local)
  File "/usr/local/lib/python3.6/dist-packages/shadowsocks/shell.py", line 124, in check_config
    encrypt.try_cipher(config['password'], config['method'])
  File "/usr/local/lib/python3.6/dist-packages/shadowsocks/encrypt.py", line 44, in try_cipher
    Encryptor(key, method)
  File "/usr/local/lib/python3.6/dist-packages/shadowsocks/encrypt.py", line 83, in __init__
    random_string(self._method_info[1]))
  File "/usr/local/lib/python3.6/dist-packages/shadowsocks/encrypt.py", line 109, in get_cipher
    return m[2](method, key, iv, op)
  File "/usr/local/lib/python3.6/dist-packages/shadowsocks/crypto/openssl.py", line 76, in __init__
    load_openssl()
  File "/usr/local/lib/python3.6/dist-packages/shadowsocks/crypto/openssl.py", line 52, in load_openssl
    libcrypto.EVP_CIPHER_CTX_cleanup.argtypes = (c_void_p,)
  File "/usr/lib/python3.6/ctypes/__init__.py", line 361, in __getattr__
    func = self.__getitem__(name)
  File "/usr/lib/python3.6/ctypes/__init__.py", line 366, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
AttributeError: /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1: undefined symbol: EVP_CIPHER_CTX_cleanup
```

以上内容是由于在openssl 1.1.0中废弃了 `EVP_CIPHER_CTX_cleanup()` 函数而引入了 `EVE_CIPHER_CTX_reset()` 函数所导致的：

解决办法：

1. 根据错误信息定位报错文件`/usr/local/lib/python3.6/dist-packages/shadowsocks/crypto/openssl.py`.
2. 编辑这个文件，搜索 **cleanup** 关键词函数，然后将其替换为 **reset** .
3. 重新执行启动命令。

##### 190604



##### 190605

v2ray ubuntu 18 安装配置：

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

