# 1. 概述

## 1.1 目的

本测试报告为DASS（数格数据分析平台）的性能测试报告，目的在于总结测试阶段的测试以及分析测试结果，描述网站是否符合需求．

## 1.2 背景

DASS网站，YOFC（长飞）研发与解决方案部目前正在进行性能测试。考虑到用户数量及数据的增多给服务器造成压力不可估计，因此计划对DASS网站负载性能测试，在系统配置不变的情况下，在一定时间内，服务器在高负载情况下的性能行为表现，便于对系统环境进行正确的分析及评估．

## 1.3 范围

本次测试主要是DASS网站系统的性能测试．

# 2 测试环境

## 2.1 测试环境

测试该项目所需要的硬件环境：

| 名称   | 详情                                                         |
| ------ | ------------------------------------------------------------ |
| 客户机 | Intel(R) Core(TM) i3-7100 CPU @ 3.90GHz、内存：4GB RAM       |
| 服务器 | Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz, 2Gswap，1333MHz前端总线，64Gmem,DDR-2 667MHz ECC 4R Memory1TB 3.5-inch 5.4K RPM SATA II Hard Drive with interposer 数量12 |

# ３ 测试内容及方法

## 3.1 测试需求/目标

在多用户,数据量的超负荷，获得服务器运行时的相关数据，从而进行分析，找出系统瓶颈，提高系统稳定性． 

## 3.2 测试内容

| 场景     | 并发用户数量 | 运行场景 | 测试点                     |
| -------- | ------------ | -------- | -------------------------- |
| 登录     | ５０         | 30分钟   | 服务器稳定性及操作响应时间 |
| 代码运算 | １０         | ３０     | 服务器计算率及使用负荷     |

## 3.3 测试工具

主要测试工具：1) ab(apache2-utile). 2) notebook运行．

# 4. 测试结果及分析

## 4.1 DASS处理性能评估

这次测试属于公网环境进行，增加了外网的网速限制及不稳定性。

## 4.2 场景测试结果

### 4.2.1 并发登录结果

测试内容:

这次测试属于模拟真实环境，加入思考时间（think time）；用户输入网址登录首页，加入1~5秒思考时间，输入用户名密码，点击登录按钮。

整个Action的平均响应时间为：3.945秒；登录操作的平均响应时间为：1.185秒。

说明：所有响应事务数为：8720次(个)

服务器平均每秒响应事件：6.664次/秒；其中登录的平均每秒响应事件为：3.257次/秒

**登录测试结果分析**

此次测试用户操作流程简单，所以并未对服务器造成高度负载，从NAS服务器服务器曲线图来看，0到70%区间浮动，运行相当平稳。从模拟环境来看，加入1到5的思考时间，更符合真实用户的操作。