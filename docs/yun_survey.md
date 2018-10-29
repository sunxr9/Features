# 百度云盘

百度云文件存储（Cloud File System）通过对标准NFS协议的支持，兼容POSIX接口，为云上的虚机、容器资源提供了跨操作系统的文件存储及共享能力。同时，百度云CFS提供简单、易操作的对外接口，并支持按实际使用量计费（公测期间免费），免去部署、维护费用的同时，最大化提升您的业务效率。 

## 核心概念

**文件存储**

文件存储是云存储的一种，为云主机、Docker容器等提供标准文件访问接口（NFS、CIFS）的云存储服务，具备无限容量、高性能、多共享、高可用等特性。

**文件系统**

文件系统是操作系统用来组织和管理存储于物理介质上数据的一种手段。

**NFS协议**

NFS（NetworkFileSystem）协议主要用于 Linux 及 Unix 客户端，CFS目前支持NFS V4.1协议。

**SMB/CIFS协议**

SMB（Server Message Block）协议是微软推出的共享网络资源的应用层通信协议，CIFS(Common Internet File System) 协议则是公共的或开放的 SMB 协议版本，其可以更好的支持 Windows 客户端的访问。CFS对于SMB/CIFS协议的支持正在开发中，敬请期待。

**挂载点**

文件系统对于用户在不同专有网络或经典网络的访问需求，可分别生成专门的访问地址，每个访问地址即为一个挂载点，用户挂载时通过指定挂载点的域名来挂载对应的CFS文件系统到本地。

## 特性

**无缝集成**

百度云CFS支持标准的NFS V4.1协议，用户可基于POSIX接口使用标准操作系统挂载命令进行实例挂载。

**共享访问**

多个计算节点可通过同时挂载一套文件系统，实现操作系统间的文件共有存储及高效共享。

**弹性扩展**

百度云CFS提供Scale-Out横向扩展能力，单文件系统最大支持100PB，最多支持10亿个文件。

**完全托管**

百度云CFS提供简洁的API接口及Web控制台，方便用户轻松创建和管理文件系统，省去本地搭建与运维成本。

## 应用场景

**内容管理及Web应用**

在大型网站、游戏、视频等领域，内容往往由服务器集群来提供，其中每台服务器都需要访问同一组文件时，则可通过挂载同一个百度云CFS的形式对相同的文件进行读写。而CFS高可扩展性、高可用性的特点，也可充分满足前端服务器的高IO读写的需要。

**大数据分析**

百度云CFS满足常见大数据应用在计算节点高吞吐量、写后读一致性及低延迟的需求，提供极易集成于大数据工作流的文件共享解决方案，是服务器日志分析和处理的最佳方案。

**泛娱乐流媒体处理**

在音视频后期制作、广播媒体处理和渲染等场景中，一个典型的特点是待处理文件较大，多台服务器共同处理。百度云CFS提供了对大文件快速共享访问的能力。

**企业办公文件共享**

在企业内部，员工需要从不同的终端访问企业公共办公系统中的同一文件，管理员可将各企业办公系统挂载到百度云CFS上，为企业提供统一共享的操作系统。

https://doc.bce.baidu.com/bce-documentation/CFS/cfs_script.zip # cfs使用脚本实例， python



# 阿里云

## 文件存储

阿里云文件存储（Network Attached Storage，简称 NAS）是面向阿里云 ECS 实例、E-HPC 和容器服务等计算节点的文件存储服务。 

### 产品特性

NAS具有一下特性：

* 无缝集成

  NAS 支持标准的文件访问协议（NFSv3/NFSv4/SMB），并使用标准的文件系统语义访问数据。因此，主流的应用程序或工作负载无需任何修改，即可与NAS无缝配合使用。

* 共享访问

  多个计算节点可以同时访问一个 NAS 文件系统实例。因此，NAS 非常适合跨多个 ECS、E-HPC 或容器服务实例部署的应用程序访问相同数据来源的应用场景。

* 弹性伸缩

  NAS 按实际使用的存储容量付费，能够充分满足弹性伸缩需求。NAS 各存储类型的容量如下：

  * NAS 容量型和 NAS 智能缓存型：单个文件系统实例的容量上限为 10 PB。
  * NAS 性能型：单个文件系统实例的容量上限为 1 PB。

* 安全限制

  NAS通过多种安全机制保证文件系统的数据安全，包括：
  * 网络隔离（专有网络）/用户隔离（经典网络）
  * 文件系统标准权限控制
  * 权限组访问控制，请参见[使用权限组进行访问控制](https://help.aliyun.com/document_detail/27534.html#concept-27534-zh)。
  * RAM 主子账号授权，请参见[使用RAM授权](https://help.aliyun.com/document_detail/27533.html#concept-27533-zh)。

* 性能扩展

  NAS 能够提供高吞吐、高 IOPS、低时延的存储性能，其性能与容量成线性关系，可满足业务增长对容量与性能提出的更高需求。

* 强一致性

  NAS 具有强一致性，即任何对文件的修改成功返回后，后续的访问会立即看到该修改的最终结果。

### 产品优势

NAS 在成本、可靠性和易用性都具有自身的优势。

* 成本
  * 一个 NAS 文件系统可以同时挂载到多个计算节点上，由这些节点共享访问，从而节约大量拷贝与同步成本。
  * 单个 NAS 文件系统的性能能够随存储容量线性扩展，使用户无需购买高端的文件存储设备，大幅降低硬件成本。
  * NAS 按实际使用的存储容量付费，能够根据使用规模进行弹性伸缩，减少不必要的投入，节约成本。
  * NAS 的高可靠性能够降低数据安全风险，从而大幅节约维护成本。

* 可靠性

  NAS 提供 99.999999999% 的数据可靠性，能够有效降低数据安全风险。

* 易用性
  * NAS 支持标准的文件访问协议（NFSv3/NFSv4/SMB）。用户在使用时无需对应用进行修改，非常便捷易用。
  * 在 NAS 中，任何文件修改成功后，用户都能够立刻看到修改结果，便于用户实时修改存储内容。

### 相关功能

NAS 能够提供一下功能：

| 应用场景         | 功能描述                                                     | 参考文档                                                     |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 创建文件系统     | 在使用 NAS 前，必须要创建一个文件系统。                      | [创建文件系统](https://help.aliyun.com/document_detail/27526.html#concept-27526-zh) |
| 管理文件系统     | 您可以查看文件系统的详细信息或删除文件系统。                 | [文件系统](https://help.aliyun.com/document_detail/27530.html#concept-27530-zh) |
| 添加挂载点       | 要挂载文件系统，您需要为文件系统添加挂载点。                 | [添加挂载点](https://help.aliyun.com/document_detail/60431.html#concept-60431-zh) |
| 管理挂载点       | 您可以禁用、激活或删除挂载点，或修改挂载点的权限组。         | [挂载点](https://help.aliyun.com/document_detail/27531.html#concept-27531-zh) |
| 挂载文件系统     | 在使用前，您需要将文件系统挂载至计算节点。                   | [在Linux系统中挂载NFS文件系统](https://help.aliyun.com/document_detail/90529.html#concept-hpp-dkh-cfb)[在Windows系统中挂载NFS文件系统](https://help.aliyun.com/document_detail/90533.html#concept-vq1-s4h-cfb)[挂载 SMB 文件系统](https://help.aliyun.com/document_detail/90535.html#concept-zb5-1rh-cfb) |
| 控制用户访问权限 | 您可以通过 RAM 赋予子用户 NAS 的操作权限，也可以通过权限组控制用户访问权限。 | [使用RAM授权](https://help.aliyun.com/document_detail/27533.html#concept-27533-zh)[使用权限组进行访问控制](https://help.aliyun.com/document_detail/27534.html#concept-27534-zh) |
| 备份文件系统     | NAS 备份服务已经开始公测，您可以对 NAS 文件系统进行备份。    | [NAS备份服务](https://help.aliyun.com/document_detail/73045.html#concept-73045-zh) |
| 将数据迁移至 NAS | 在使用 NAS 时，需要将数据从本地或对象存储迁移至 NAS。        | [数据迁移上NAS工具（支持本地文件和OSS等）](https://help.aliyun.com/document_detail/45306.html#concept-45306-zh)[Windows环境数据迁移工具](https://help.aliyun.com/document_detail/56937.html#concept-56937-zh) |
| 使用 NAS API     | NAS 提供各种 API 接口，可以对文件系统进行各种操作。          | [API 概览](https://help.aliyun.com/document_detail/62598.html#concept-62598-zh) |

###应用场景

NAS 适用于以下场景：

* 负载均衡共享存储和高可用

  在负载均衡 SLB 连接多个 ECS 实例的场景中，这些 ECS 实例上的应用将数据存放在共享的文件存储 NAS 上，实现数据共享和负载均衡服务器高可用。

* 企业办公文件共享 

  企业员工办公需要访问和共享相同的数据集，管理员可创建 NAS 文件系统，为组织中的个人提供数据访问，并可设置文件或目录级别的用户和用户组权限。 

* 数据备份

  用户希望将线下机房的数据备份到云上，同时要求云上的存储服务兼容标准的文件访问接口。这种场景下可以使用 NAS 来存储数据备份。

* 服务器日志共享

  用户可以将多个计算节点上的应用服务器日志存放在共享的文件存储 NAS 上，方便后续的日志集中处理与分析。

## 功能特性

支持 NFSv3、NFSv4 及 SMB 协议，使用标准的文件系统语义访问数据，主流的应用程序及工作负载无需任何修改即可无缝配合使用。

### 共享访问

多个计算节点可以同时访问一个文件系统实例，非常适合跨多个 ECS、E-HPC 或容器服务实例部署的应用程序访问相同数据来源的应用场景。

### 弹性伸缩

文件系统单个容量上限 10PB，按实际使用量付费，充分满足弹性伸缩需求。

### 安全控制

通过网络隔离（专有网络）/用户隔离（经典网络）、文件系统标准权限控制、权限组访问控制和 RAM 主子账号授权等多种安全机制，保证文件系统数据安全万无一失。

### 线性扩展的性能

可为应用工作负载提供高吞吐量与高 IOPS、低时延的存储性能，同时性能与容量成线性关系，可满足业务增长需要更多容量与存储性能的诉求。

### 强一致性

支持强一致性，任何对文件的修改成功返回后，其他后续的访问会立即看到最终的结果。

## 应用场景

为了更好地定位阿里云文件存储 NAS 的目标应用场景，现将 NAS 的应用场景分为以下五大类。

### 企业应用程序

NAS 具有较高的可扩展性、弹性、可用性和持久性，因而可用作企业应用程序和以服务形式交付的应用程序的文件存储。NAS 提供的标准文件系统界面和文件系统语义能够将企业应用程序轻松迁移到阿里云，或构建新的应用程序。

### 媒体和娱乐工作流

视频编辑、影音制作、广播处理、声音设计和渲染等媒体工作流通常依赖于共享存储来操作大型文件。强大的数据一致性模型加上高吞吐量和共享文件访问，可以缩短完成以上工作流所需的时间，并将多个本地文件存储库合并到面向所有用户的单个位置。

### 大数据分析

NAS 提供了大数据应用程序所需的规模和性能、计算节点高吞吐量、写后读一致性以及低延迟文件操作。许多分析工作负载通过文件接口与数据进行交互，依赖于文件锁等文件语义，并要求能够写入文件的部分内容。NAS 支持所需的文件系统语义，并且能够弹性扩展容量和性能。

### 内容管理和 Web 服务

NAS 可以用作一种持久性强、吞吐量高的文件系统，用于各种内容管理系统和 Web 服务应用程序，为网站、在线发行和存档等广泛的应用程序存储和提供信息。由于 NAS 遵循了预期的文件系统语义、文件命名惯例，以及 Web 开发人员习惯使用的权限，因此它能够轻松与 Web 应用程序集成，并且可用于 Web 站点、在线发行和存档等广泛应用程序。

### 容器存储

鉴于容器的可快速预置、容易携带，并可提供进程隔离的特点，容器非常适用于构建微服务。对于每次启动时都需要访问原始数据的容器，它们需要一个共享文件系统，使它们无论在哪个实例上运行，都可以连接到该文件系统。NAS 可提供对文件数据的持久共享访问权限，非常适合容器存储。

## 名词解释

下表列出了在文件存储 NAS 中使用的一些术语。

| 术语     | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| 挂载点   | 挂载点是文件系统实例在专有网络或经典网络内的一个访问目标地址。每个挂载点都对应一个域名，用户 mount 时通过指定挂载点的域名来挂载对应的 NAS 文件系统到本地。 |
| 权限组   | 权限组是 NAS 提供的白名单机制，通过向权限组内添加规则来允许 IP 地址或网段以不同的权限访问文件系统。**说明** 每个挂载点都必须与一个权限组绑定。 |
| 授权对象 | 授权对象是权限组规则的一个属性，代表一条权限组规则被应用的目标。在专有网络内，授权对象可以是一个单独的 IP 地址或一个网段。在经典网络内，授权对象只能是一个单独的 IP 地址（一般为 ECS 实例的内网 IP 地址）。 |

## 存储类型介绍

NAS 提供 NAS 通用型、NAS Plus 智能缓存型和并行文件系统 CPFS（Cloud Paralled File System） 三种存储类型。

- [NAS通用型](https://help.aliyun.com/document_detail/71454.html#concept_71454_zh)分为容量型和 SSD 性能型，适用于广泛场景的分布式文件存储。
- [NAS Plus智能缓存型](https://help.aliyun.com/document_detail/66444.html#concept_66444_zh)针对广电非编、动画渲染等高性能要求场景进行了优化，相较于 NAS 通用型具有更加高效的性能。
- [CPFS并行文件系统](https://help.aliyun.com/document_detail/66278.html#concept_66278_zh)是一种并行文件系统，目前正在邀测中。



[python使用介绍](https://help.aliyun.com/document_detail/32028.html?spm=a2c4g.11186623.6.747.1716585exR84QI) SDK

OSS Python SDK提供丰富的示例代码，方便您参考或直接使用。示例包括以下内容：

| 示例文件                                                     | 示例内容                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [object_basic.py](https://github.com/aliyun/aliyun-oss-python-sdk/blob/master/examples/object_basic.py) | [快速入门](https://help.aliyun.com/document_detail/32027.html#concept-32027-zh)，包括创建存储空间、上传、下载、列举、删除文件等 |
| [object_extra.py](https://github.com/aliyun/aliyun-oss-python-sdk/blob/master/examples/object_extra.py) | 上传文件和管理文件，包括[设置自定义元信息](https://help.aliyun.com/document_detail/88456.html#concept-88456-zh)、[拷贝文件](https://help.aliyun.com/document_detail/88465.html#concept-88465-zh)、[追加上传文件](https://help.aliyun.com/document_detail/88432.html#concept-88432-zh)等 |
| [upload.py](https://github.com/aliyun/aliyun-oss-python-sdk/blob/master/examples/upload.py) | 上传文件，包括[断点续传上传](https://help.aliyun.com/document_detail/88433.html#concept-edl-r2j-kfb)、[分片上传](https://help.aliyun.com/document_detail/88434.html#concept-88434-zh)等 |
| [download.py](https://github.com/aliyun/aliyun-oss-python-sdk/blob/master/examples/download.py) | 下载文件，包括[流式下载](https://help.aliyun.com/document_detail/88441.html#concept-88441-zh)、[范围下载](https://help.aliyun.com/document_detail/88443.html#concept-88443-zh)、[断点续传下载](https://help.aliyun.com/document_detail/88444.html#concept-88444-zh)等 |
| [object_check.py](https://github.com/aliyun/aliyun-oss-python-sdk/blob/master/examples/object_check.py) | 上传和下载时数据校验的用法，包括MD5和[CRC](https://help.aliyun.com/document_detail/43394.html#concept-sb4-33f-vdb) |
| [object_progress.py](https://github.com/aliyun/aliyun-oss-python-sdk/blob/master/examples/object_progress.py) | [上传进度条](https://help.aliyun.com/document_detail/88435.html#concept-dfm-s2j-kfb)和[下载进度条](https://help.aliyun.com/document_detail/88445.html#concept-88445-zh) |
| [object_callback.py](https://github.com/aliyun/aliyun-oss-python-sdk/blob/master/examples/object_callback.py) | 上传文件中的[上传回调](https://help.aliyun.com/document_detail/88437.html#concept-88437-zh) |
| [object_post.py](https://github.com/aliyun/aliyun-oss-python-sdk/blob/master/examples/object_post.py) | [表单上传](https://help.aliyun.com/document_detail/31848.html#concept-bws-3bb-5db)的相关操作 |
| [sts.py](https://github.com/aliyun/aliyun-oss-python-sdk/blob/master/examples/sts.py) | STS的用法，包括角色扮演获取临时用户的密钥，并使用临时用户的密钥访问OSS |
| [live_channel.py](https://github.com/aliyun/aliyun-oss-python-sdk/blob/master/examples/live_channel.py) | [LiveChannel](https://help.aliyun.com/document_detail/44297.html#concept-njb-pbd-xdb)的相关操作 |
| [image.py](https://github.com/aliyun/aliyun-oss-python-sdk/blob/master/examples/image.py) | [图片处理](https://help.aliyun.com/document_detail/47660.html#concept-47660-zh)的相关操作 |
| [bucket.py](https://github.com/aliyun/aliyun-oss-python-sdk/blob/master/examples/bucket.py) | [管理存储空间](https://help.aliyun.com/document_detail/32029.html#concept-32029-zh)，包括创建、删除、列举存储空间，以及[设置静态网站托管](https://help.aliyun.com/document_detail/32034.html#concept-32034-zh)，[设置生命周期规则](https://help.aliyun.com/document_detail/32035.html#concept-32035-zh)等 |

## 源码地址

请访问[GitHub](https://github.com/aliyun/aliyun-oss-python-sdk)获取源码。



# 腾讯云

[API 中心](https://cloud.tencent.com/document/api)

[对象存储API](https://cloud.tencent.com/document/api/436/7751)

