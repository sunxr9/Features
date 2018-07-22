1， 安装go语言环境：

​	sudo add-apt-repository ppa:gophers/go

​	sudo apt-get update

​	sudo apt-get install golang-stable

​	*添加环境配置*

​	vim /etc/profile 在最后增加环境配置

​	export GOROOT=/usr/lib/go 安装目录

​	export GOARCH=386

​	export GOOS=linux

​	export GOPATH=/home/namespace/go 工作目录

​	export GOBIN=$GOPATH/bin

​	export PATH=$GOPATH/bin:￥（md格式美元符号）PATH

​	source /etc/profile 加载环境。

```shell
# go语言环境测试
# 在新建GOPATH下新建三个目录
mkdir src pkg bin
src # 存放源码
pkg # 存放编译生成的文件
bin # 存放生成的可执行文件

# 创建第一个go应用
cd $GOPATH/src
mkdir test1
cd test1
vi t1.go

# t1.go 内容

package main
 
import "fmt"
 
func main() {
    fmt.Println("Hello world, I'm learning Golang")
}
# 保存退出，使用一下命令运行
go run t1.go # 在文件目录下
```

https://blog.csdn.net/u010889990/article/details/44171515



2， 下载etcd

​	wget https://github.com/coreos/etcd/releases/download/v3.1.8/etcd-v3.1.8-linux-amd64.tar.gz 

​	解压etcd包

​	tar -xzf etcd-v3.1.8-linux-amd64.tar.gz

​	拷贝etcd可执行程序至/usr/bin

​	cd etcd-v3.1.8-linux-amd64

​	cp etcd etcdctl /usr/bin



3， 安装Flannel

​	wget https://github.com/coreos/flnnel/download/v0.7.1/flannel-v0.7.1-linux-am64.tar.gz

​	解压flanel压缩包

​	tar -xzf flanne-v0.7.1-linux-m64.tar.gz

​	拷贝flanne可执行程序至/usr/bin

​	cd flannel-v0.7.1-linux-amd64

​	cp flannel mk-docker-opts.sh /usr/bin	

失败，于文件不符，恢复。



https://medium.com/@Grigorkh/install-kubernetes-on-ubuntu-1ac2ef522a36

https://kubernetes.io/docs/getting-started-guides/ubuntu/

