# ubuntu 搭建LDAP认证

安装命令：

```bash
sudo apt install slapd ldap-utils
```

在安装过程中，系统会要求为LADP目录创建管理员密码．并确认密码．安装完成之后，LDAP没有完全配置，修要修改默认目录信息树（DIT）后缀，执行以下命令来完成其他配置：

```bash
sudo dpkg-reconfigure slapd
```

出现提示时，第一个问题应是*如果启用此选项，则不会为你创建爱你数据库的初始配置*，选择＂No＂.

第二个选项是*DNS域名用于构造LDAP目录的基本DB*的提示，输入例："test.com"．并再次输入上述内容确认

．然后需要进行密码确认．完成后，选择MDB做为数据库后端，然后在最后的清楚slapd时选择No以删除数据库，最后选择Yes以移动旧的数据库．到此完成安装和配置．

验证安装是否正常: `ldapsearch -x -LLL -b dc=test,dc=com`

检查端口　netstat -an | grep 389

## 可视化工具

### phpldapadmin

安装可视化插件：`sudo apt install phpldapadmin`

修改`/etc/phpldapadmin/config.php`文件中修改一下选项：

1. $servers->setValue('server'. 'host', **'127.0.0.1'**)  修改为某个内网可访问的IP地址(ldap服务器IP)

2. $servers->setValue('server'. 'base', array(**'dc=example,dc=com'**)) #修改为baseDN，这里修改为dc=test,dc=com

3. $servers->setValue('login', 'bind_id', **'cn=admin,dc=example,dc=com'**)#修改为baseDN下的admin, cn=admin,dc=test,dc=com

4. $config->custom->appearance['hide_template_warning'] = **false** #false修改为true

防火墙放行Apache2:

```bash
sudo ufw allow "Apache"
sudo ufw allow "Apache Full"
sudo ufw allow "Apache Secure" 
```

重启Apache2:`/etc/init.d/apache2 restart`

通过浏览器访问http://IP/phpldapadmin测试页面是否能够访问．



### LDAP-account manager

安装依赖：

```
sudo apt install php php-cgi libapache2-mod-php php-common php-pear php-mbstring
```

重启Apache2

```bash
sudo systemctl reload apache2.service
```

安装LDAP-account-manager

```bash
sudo apt install ldap-account-manager
```

查看配置文件`/etc/php/7.2/apache2/php.ini`，查看`memory_limit`选项，应为128M．

编辑LDAP-account-manager配置，默认配置`/usr/share/ldap-account-manager/config/lam.conf`，

主要修改以下几项：

1. Admins: cn=admin,dc=test,dc=com # cn为管理员用户名，dc为DNS项
2. treesuffix: dc=test,dc=com
3. passwd: sgds # 登录密码
4. types: suffix_user: ou=People, dc=my-domain, dc=com
5. types: suffix_group: ou=People, dc=my-domain, dc=com

以上配置将所有的**dc**项改为LDAP安装时DNS设置的值，例设置为test.com，在此文件中填写为`dc=test,dc=com`格式，将DNS设置拆分修改．

总的来说，将此配置文件中的所有**dc**项，改为安装slapd时所填写的DNS项，而且是拆分填写，不是将DNS直接填写［dc=test.com］．

完成以上步骤即可通过浏览器进行登录，但是注意使用此工具的路由和上述路由不同，为`http://IP/lam`．

