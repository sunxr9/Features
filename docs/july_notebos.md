##### 190701

SQLite3 sql语句在编写的时候不能使用Python 字符串格式化方式编写．例：

```python
# 错误写法
sqlite_insert_sql = 'insert into ts_kv(entity_type, entity_id, key, ts, bool_v, str_v, long_v, dbl_v) values(%s, %s, %s, %s, %s, %s, %s, %s)'
```

以上编写的内容会在写入数据的时候报错，容易出现`sqlite3.OperationalError: unrecognized token: "01T00"`．需要使用sqlite的语法进行编写，用**`?`**代替站位符，需要传递的参数在执行sql语句的函数中传入：

```python
# 正确语句
sqlite_insert_sql = 'insert into ts_kv(entity_type, entity_id, key, ts, bool_v, str_v, long_v, dbl_v) values(?, ?, ?, ?, ?, ?, ?, ?)'
sqlite_curr.execute(sqlite_insert_sql, ("需要在sql语句中替换的参数元组"))
```



SQLite3 设置返回值的格式，默认值为元组，不利于装换，需要在链接的时候设置好返回格式：

```python
connect = sqlite3.connect('db name')
connect.row_factory = sqlite3.Row
cursor = connect.cursor()
```

设置完成之后，查询的每一个值将支持按列名和索引以及迭代访问．

可通过`keys()`方法获取对应的列名，可以for循环一个查询集的没一个数据．



Pandas 时间转化，需要保留到秒单位是，需要先将时间格式化为字符串，然后在通过`to_datetime`函数再次转化为时间格式．



##### 190704

数据本地缓存，

定期更新，