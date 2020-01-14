# JupyterHub 配置文件说明

实现使用 Docker 创建个人分析环境以及使用 GitLab 进行用户登录认证的配置解释．

+ c.JupyterHub.base_url = "/"

  自定义设置 JupyterHub 的起始 URL 路由规则．

+ c.JupyterHub.hub_ip = "IP"

  此设置是用于个人用户镜像与外部管理进程进行通信．告诉个人用户内部的程序，外部（部署在主机上的JupyterHub）的存在地址，否则无法进行 Docker 容器之间与外部的通信．

+ c.JupyterHub.port = 8000

  程序启动监听地址．

+ c.Spawner.cmd = ['jupyter-labhub']

  启动单用户服务器的命令，允许hub启动 Jupyter lab．

+ c.Spawner.default_url = '/lab'

  设置登录成功后的默认显示页面

+ c.PAMAuthenticator.check_account = True

  检查用户状态，提供系统安全保护．

+ c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

  设置JupyterHub 使用什么方式产生用户分析环境

+ c.DockerSpawner.notebook_dir = '/home/jovyan/work'

  设置使用Docker方式产生用户分析环境的用户工作空间起始目录，此设置为Docker产生的容器内部路径．

+ c.DockerSpawner.volumes = {"jupyterhub-user-{username}": '/home/jovyan/work'}

  设置用户的工作空间文件保留在主机上的目录格式化格式，持久话用户的分析文件．

+ c.DockerSpawner.container_image = 'sunxr/dass:0.5'

  设置Docker 产生用户独立分析容器的镜像名称，其中如不写版本 `sunxr/dass` 将会默认补全为 `sunxr/dass:latest` ，如需使用特定版本的镜像，需要填写完整．

gitlab 跳转认证

+ 导入认证包

  ```python
  from oauthenticator.gitlab import GitLabOAuthenticator
  ```

+ c.JupyterHub.authenticator_class = GitLabOAuthenticator

  设置JupyterHub 登录认证使用的程序对象

+ c.GitLabOAuthenticator.oauth_callback_url = 'http://192.168.3.19/hub/oauth_callback'

  设置GitLab 认证完成后GitLab返回信息的路由，上述路由中不可变的为`/hub/oauth_callback`，这是JupyterHub接收GitLab认证信息返回处理的路由，更改将无法接收信息并解析．IP地址和通信协议根据部署实际情况进行调整．

+ c.GitLabOAuthenticator.client_id = 'j10fjas94kjd'

  GitLab 提供认证的连接ID，表示GitLab允许为携带此连接ID的服务提供认证，由GitLab 进行创建．

+ c.GitLabOAuthenticator.client_secret = 'df904rsd90sda0uafer09'

  GitLab 连接key，同样由GitLab提供，并与连接ID为一对，