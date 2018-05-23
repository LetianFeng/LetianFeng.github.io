---
layout: post
title: "python文件读取小结"
date: 2018-05-23 21:27:59 +0200
categories: python
tags: python
---

在训练机器学习模型的过程中，从数据集读取数据是一项必不可少的操作，虽然我之前在[python的文件读写](https://letianfeng.github.io/python/2018/04/20/python_file_io.html)中简单介绍了一下如何以读/写的方式打开一个文件，但是并不详细，今天就来补充一下。

首先，我们新建一个文档`foo.txt`，存入以下内容:
```
Hello
World
!
```

回忆一下，当我们使用`f = open('/path/to/file', 'r')`时，需要手动处理异常，并在进行完IO操作后手动关闭文件`f.close()`，否则对文件的修改不会被保存:

```python
import os

# 首先获取当前路径，再join相对路径，最终获得绝对路径
current_path = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(current_path, '/path/to/foo.txt')

# 如果foo.txt就在当前文件夹下，也可以直接使用文件名，省去获取相对路径的麻烦
data_path = 'foo.txt'

# 将整个文件读取为单个字符串，s是一个值为'Hello\nWorld\n!\n'的str变量
with open(data_path, 'r') as f:
    s = f.read()
```

当然，在实际应用中，我们不可能满足于读取整个文件这一非常局限的方式，下面介绍几种常见的文件读取操作，可以满足大部分的应用场景。

1. 将整个文件读取为一个list:

```python
# 保留每行的回车\n，l的值为['Hello\n', 'World\n', '!\n']
with open(data_path, 'r') as f:
    l = f.readlines()

# 不保留\n，l的值为['Hello', 'World', '!']
with open(data_path, 'r') as f:
    l = f.read().splitlines()
```

2. 读取单行:

```python
# 逐行读取前n行，line依次为'Hello\n','World\n','!\n'
# 当n大于文件的行数时，f.readline()并不会抛出异常，而是返回空字符串，即line被赋值为''
with open(data_path, 'r') as f:
    for _ in range(n):
        line = f.readline()
	# do something with line
```

3. 逐行读取至文件结束:

```python
with open(data_path, 'r') as f:
    for line in f:
        pass
        # do something with line
```

