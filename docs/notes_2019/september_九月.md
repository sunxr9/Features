##### 190903

##### 190904

postgresql 导入数据库语法：

```bash
psql -d databaseName -U username -f 需要导入数据文件
```

注意`-U`是大写的．



##### 190905

Django admin (2.2.0)管理站点管理出现错误，在一些表的提交上出现模板错误：

```
TemplateDoesNotExist at /admin/app/post/add/
search/indexes/app/post_text.txt
```

这是由于配置了`TEMPLATES_DIRS`参数导致搜所路径出现错误．

最后通过使用[django-admin-tools](<https://django-admin-tools.readthedocs.io/en/latest/configuration.html>)解决，简要使用方式如下：

+ 在INSTALLED_APPS变量中注册admin-tools：

  ```python
  # 注意需要在django contrib 之前
  INSTALLED_APPS = [
      'admin_tools',
      'admin_tools.theming',
      'admin_tools.menu',
      'admin_tools.dashboard',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'mines'
  ]
  ```

+ 编辑TEMPLATES 变量配置

  ```python
  # 在TEMPLATES 变量中添加一些loaders配置
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BASE_DIR, 'templates')],
          'APP_DIRS': False,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
              'loaders' : [
                  'django.template.loaders.filesystem.Loader',
                  'django.template.loaders.app_directories.Loader',
                  'admin_tools.template_loaders.Loader',
                  ]
          },
      },
  ]
  ```

+ 添加url 路由

  ```python
  from django.conf.urls import include,url
  from django.contrib import admin
  from mines.views import SummaryByMapIcon
  
  urlpatterns = [
      url(r'^admin_tools/', include('admin_tools.urls')),
      url(r'^admin/', admin.site.urls),
      # 其他路由....
  ]
  ```

完成以上步骤后需要进行表迁移，将django-admin-tools使用的表进行创建.

最后再次执行收集静态资源命令`python manage.py collectstatic`即可．

##### 190906

Django admin站点提数据出现模板不错在错误，提示如下：

```
TemplateDoesNotExist at /secret/app/post/add/
search/indexes/app/post_text.txt
```

上面一句提示模板不存在，并说明了保存的路由，但是原因在Django, 而是使用haystack 的原因．

第二局报错信息提示说明了原因，在`serch/indexes/app`没有`post_text.txt`文件．django haystack 流程需要在注册的app中创建`search_indexes.py`文件，进行编写搜索对象．同时在`templates`模板目录中创建search目录，存放搜索结果页面．依据上述的保存，缺少`indexes/app/post_text.txt`文件信息．所以我们需要在search目录下创建`indexes/{appname}/{model_name}_text.txt文件．



ｕbuntu 18.04设置内网DNS解析服务器地址：

编辑`/etc/systemd/resolved.conf`文件，放开DNS项．将需要添加的DNS服务器地址填写即可．

完成后重启`systemd-resolves`即可，`sudo service systemd-resolved restart`.



django 出现不跟静态文件不能加载，在settings文件中设置`STATICFILES_DIRS`变量：

```
# STATIC_ROOT = os.path.join(BASE_DIR, 'statics')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'statics')
]
```

注意需要注释掉`STATIC_ROOT`变量，两者不能共存．



##### 190910

gitlab 开启注册功能的时候出现500错误，错误信息主要如下：

```
Completed 500 Internal Server Error in 17ms (ActiveRecord: 2.2ms)

OpenSSL::Cipher::CipherError ():

lib/gitlab/crypto_helper.rb:27:in `aes256_gcm_decrypt'
app/models/concerns/token_authenticatable_strategies/encrypted.rb:55:in `get_token'
app/models/concerns/token_authenticatable_strategies/base.rb:27:in `ensure_token'
app/models/concerns/token_authenticatable_strategies/encrypted.rb:42:in `ensure_token'
app/models/concerns/token_authenticatable.rb:38:in `block in add_authentication_token_field'
app/services/application_settings/update_service.rb:18:in `execute'
app/controllers/admin/application_settings_controller.rb:40:in `update'
lib/gitlab/i18n.rb:55:in `with_locale'
lib/gitlab/i18n.rb:61:in `with_user_locale'
app/controllers/application_controller.rb:420:in `set_locale'
lib/gitlab/middleware/multipart.rb:103:in `call'
lib/gitlab/request_profiler/middleware.rb:16:in `call'
lib/gitlab/middleware/go.rb:19:in `call'
lib/gitlab/etag_caching/middleware.rb:13:in `call'
lib/gitlab/middleware/correlation_id.rb:16:in `block in call'
lib/gitlab/correlation_id.rb:15:in `use_id'
lib/gitlab/middleware/correlation_id.rb:15:in `call'
lib/gitlab/middleware/read_only/controller.rb:40:in `call'
lib/gitlab/middleware/read_only.rb:18:in `call'
lib/gitlab/middleware/basic_health_check.rb:25:in `call'
lib/gitlab/request_context.rb:20:in `call'
lib/gitlab/metrics/requests_rack_middleware.rb:29:in `call'
lib/gitlab/middleware/release_env.rb:13:in `call'
```

解决方法：

```
:$ sudo gitlab-rails c


-------------------------------------------------------------------------------------
 GitLab:       11.7.0 (1d9280e)
 GitLab Shell: 8.4.4
 postgresql:   9.6.11
-------------------------------------------------------------------------------------
Loading production environment (Rails 5.0.7.1)
irb(main):001:0> 
irb(main):002:0> 
irb(main):003:0> settings = ApplicationSetting.last
......
irb(main):004:0> settings.update_column(:runners_registration_token_encrypted, nil)
=> true
irb(main):005:0> exit

:$ sudo gitlab-ctl restart

```



##### 190911

gitlab 设置储存库路径：

编辑`/etc/gitlab/gitlab.rb`文件，找到`git_data_dirs`所在位置，并进行编辑：

```
git_data_dirs({
	"default" => {
		"path" => 'path/to/repository'
		}
	})
```

编辑完成后执行重新配置命令：`gitlab-ctl reconfigure`．

如果原有默认路径下有存储库，在重新配置之后会出现仓库找不到的情况，将原有的默认路径下的存储库移动到新的路径下即可．默认路径`/var/opt/gitlab/git-data/repository`．

##### 190926

LEDE路由设置系统自启动

<https://blog.csdn.net/Simple_JD/article/details/50944752>　案例

