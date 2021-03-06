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



##### 190717

n_clusters:簇的个数，即你想聚成几类
init: 初始簇中心的获取方法
n_init: 获取初始簇中心的更迭次数，为了弥补初始质心的影响，算法默认会初始10次质心，实现算法，然后返回最好的结果。
max_iter: 最大迭代次数（因为kmeans算法的实现需要迭代）
tol: 容忍度，即kmeans运行准则收敛的条件
precompute_distances：是否需要提前计算距离，这个参数会在空间和时间之间做权衡，如果是True 会把整个距离矩阵都放到内存中，auto 会默认在数据样本大于featurs*samples 的数量大于12e6 的时候False,False 时核心实现的方法是利用Cpython 来实现的
verbose: 冗长模式（不太懂是啥意思，反正一般不去改默认值）
random_state: 随机生成簇中心的状态条件。
copy_x: 对是否修改数据的一个标记，如果True，即复制了就不会修改数据。bool 在scikit-learn 很多接口中都会有这个参数的，就是是否对输入数据继续copy 操作，以便不修改用户的输入数据。这个要理解Python 的内存机制才会比较清楚。
n_jobs: 并行设置
algorithm: kmeans的实现算法，有：‘auto’, ‘full’, ‘elkan’, 其中 'full’表示用EM方式实现．
