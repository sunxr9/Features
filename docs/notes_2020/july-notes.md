## 0703 

PostgreSQL 创建用户和赋值权限

```sql
# 创建用户
create user username password '***';
# 赋值权限
grant [select, insert, update...] on [database,table] to username;
```

**注意** : 如测试连接中，查询表操作出现提示schema权限不足，需额外设置schema 权限，注意查看报错信息中提示的schema 名称：

```
grant usage on schema schemaName to username;
```



```
docker run --rm --hostname 139.198.188.123 --publish 9082:443 --publish 9081:80 --name gitlab --volume /root/anaconda3/ssl/config:/etc/gitlab gitlab/gitlab-ce
```

## 0705

Ubuntu 搜狗输入法，显示简体文字，实际输出为繁体文字。

解决办法： 按住 `Shift` 按键（不放），然后同时按 `Ctrl + F` 切换繁体中文至简体中文。再次执行步骤，切换简体文字至繁体文字。





### 0706

阶段任务：使用 GPS 数据对比门架筛选车辆，区分车辆通行次数（暂定聚类），生成车辆通行矩阵（车牌与通行数量）



GitLab 配置 自定义 https 证书后，使用Git进行操作出现错误：

```
## 1. CA 文件
..: server certificate verification failed. CAfile: none CRLfile: none
## 2. SSL
..: SSL certificate problem: self signed certificate
```

临时解决办法（不推荐）：

```
# 在 Git 客户端执行忽略 ssl 验证命令
git config --global http.sslVerify false
```



解决办法：

+ 配置 ssh 认证，通过 ssh 跳过认证。ssh 认证方式通过 ssh 进行文件传递，所以 GitLab 部署机器的 ssh 端口需为默认 22 端口。

+ 配置客户端 Git 信任 https 证书。

  1. 获取自定义证书 crt 文件

  2. 执行 Git 配置命令
  
     ```bash
     git config --global http.sslCAInfo path/to/certificate.crt
     ```
  
     
  



聚类

读取数据

时间清洗：解决思路，直方图，切分，拟合，大津分割

#### 0707

Git clone 指定ssh 端口：

```
git clone ssh://git@139.198.188.123:8022/sunxr/test_paper.git
```



docker run --name MySQL --restart always -d -e MYSQL_ROOT_PASSWORD=SGds12#$ -v /media/ext1/mysql_docker:/var/lib/mysql -p 3306:3306 mysql:latest



##### 0722

**TODO** ：

- [ ] 数据库虚拟机创建、获取MySQL和PostgreSQL镜像
- [ ] GitLab 虚拟机创建、获取镜像、备份数据、数据恢复
- [ ] Redmine 虚拟机创建、获取镜像、配置 GitLab 认证
- [ ] Dsaiom 平台搭建

IP 分配详情

| IPV4地址        | 服务器名称         | 备注     |
| --------------- | ------------------ | -------- |
| 192.168.100.74  | T7920 工作站       |          |
| 192.168.100.126 | ESXi -- dsaiom-lab | 分析平台 |
| 192.168.100.127 | 无                 |          |
| 192.168.100.128 | 无                 |          |
| 192.168.100.181 | ESXi -- Database   | 数据库   |

