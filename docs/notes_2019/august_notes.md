##### 190801

ubuntu 修改程序最大打开文件数量:

```
# 编辑/etc/systemd/system.conf文件
# 取消DefaultLimitNOFILE的注释,并设置限制
DefaultLimitNOFILE = 100000
# 重启机器
# 使用ulimit -a 命令查看
```

##### 190821

rsync 常用命令:

将目录从本地服务器复制到远程服务器使用参数**`-avz`**

将远程目录复制/同步到本地计算机使用参数: **`-avzh`** 

##### 190827

gitlab 重启命令 gitlab-ctl start

gitlab 修改默认端口:

```
vi /etc/gitlab/gitlab.rb
nginx['listen_port'] = 9000 #默认值即80端口 nginx['listen_port'] = nil

vi /var/opt/gitlab/nginx/conf/gitlab-http.conf
listen *:9000; #默认值listen *:80;
```

使用gitlab 内置Nginx, 把修改关于Nginx 的内容开启修改:

```
nginx['enable'] = true
nginx['client_max_body_size'] = '250m'
nginx['redirect_http_to_https'] = false
nginx['redirect_http_to_https_port'] = 80
```

gitlab 出现:`fail: redis: runsv not running`, 使用以下命令解决

```
sudo systemctl restart gitlab-runsvdir
sudo gitlab-ctl restart
```

