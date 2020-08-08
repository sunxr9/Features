# FastAPI 技术预研

预研 FastAPI 技术使用。

## 背景

基于 OpenAPI 开放标准，构建公开服务接口。

## FastAPI 简述

[FastAPI](https://fastapi.tiangolo.com/) 是一个用于构建 API 的现代、快速（高性能）的 web 框架，使用 Python 3.6+ 并基于标准的 Python 类型提示。

关键特性：

- **快速**：可与 **NodeJS** 和 **Go** 比肩的极高性能（归功于 Starlette 和 Pydantic）。[最快的 Python web 框架之一](https://fastapi.tiangolo.com/zh/#_11)。
- **高效编码**：提高功能开发速度约 200％ 至 300％。*
- **更少 bug**：减少约 40％ 的人为（开发者）导致错误。*
- **智能**：极佳的编辑器支持。处处皆可自动补全，减少调试时间。
- **简单**：设计的易于使用和学习，阅读文档的时间更短。
- **简短**：使代码重复最小化。通过不同的参数声明实现丰富功能。bug 更少。
- **健壮**：生产可用级别的代码。还有自动生成的交互式文档。
- **标准化**：基于（并完全兼容）API 的相关开放标准：[OpenAPI](https://github.com/OAI/OpenAPI-Specification) (以前被称为 Swagger) 和 [JSON Schema](http://json-schema.org/)。



## 预研环境

本次技术预研环境如下：

+ 操作系统： Ubuntu 20.04 LTS

+ 内核版本： 5.4.0-40-generic
+ Python 版本： 3.7.0
+ FastAPI 版本：0.59.0
+ [Uvicorn](https://www.uvicorn.org/) 版本： 0.11.5

### 安装

FastAPI官方推荐使用 pip 安装，conda 安装需使用 `conda-forge` 通道。

#### Pip（推荐）

1. pip 安装所有的可选依赖和功能：

   ```bash
   pip install fastapi[all]
   ```

2. pip 指定安装

   ```bash
   pip install fastapi
   ```

   等待完成，完成后安装 uvicorn 做为服务器。

#### conda

执行 conda 命令安装:

```
conda install -c conda-forge fastapi
```

## 使用案例

