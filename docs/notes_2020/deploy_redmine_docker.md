# 部署 redmine 

环境:

+ mysql 5.7
+ redmine 



## PostgreSQL启动命令

```bash
docker run -d --name some-postgres --network some-network -e POSTGRES_PASSWORD=secret -e POSTGRES_USER=redmine postgres
```





### mysql 启动命令

```bash
docker run -d --name some-mysql --network some-network -e MYSQL_USER=redmine -e MYSQL_PASSWORD=secret -e MYSQL_DATABASE=redmine -e MYSQL_RANDOM_ROOT_PASSWORD=1 mysql:5.7
```



```bash
docker run --name some-redmine -p 9994:3000 --network some-network -e REDMINE_DB_MYSQL=some-mysql -e REDMINE_DB_USERNAME=redmine -e REDMINE_DB_PASSWORD=secret redmine
```

