---
layout: post
title: "带参数的python可执行文件"
date: 2018-05-04 14:31:07 +0200
categories: python
tags: python
---

众所周知，python是一个脚本语言，脚本语言具有简单、易学、易用的特性。执行代码前，不需要编译(compile)，通过即时解释(interpret)即可运行。然而，说了一堆有的没的，作为小白的我最开始也是只会用IDE来跑程序，怎么样才能在命令行下直接运行一个python脚本文件呢?

首先，创建一个python脚本文件`foo.py`:

```python
print('Hello world!')
```

最简单的方式，我们可以直接使用python解释器来执行脚本文件，如:

```bash
letian@fengPC:~$ python3 foo.py 
Hello world!
```

不过，每次都要输入python3还是有点麻烦，尤其是输成python的时候烦躁的情绪会非常强烈，所以我们要在`foo.py`文件的<span style="color:red">**第一行**</span>(注意连空行都不可以有)声明解释器的位置，这样脚本文件就会自己去找到解释器，不用我们每次手动输入了。更新后的`foo.py`如下:

```python
#!/usr/bin/python3
print('Hello world!')
```

当然你也可以使用其它路径下的解释器，比如:

```python
#!/home/letian/anaconda3/envs/python3/bin/python3
print('Hello world!')
```

这样，理论上这个脚本文件就可以通过`./foo.py`来执行了，但一定要保证这个文件是可执行的，或者说你当前的用户有权限(access permission)执行，如果没有权限的话，要用[`chmod`](https://zh.wikipedia.org/wiki/Chmod)这个工具来赋予文件可以被当前用户执行的权限:

```bash
letian@fengPC:~$ ./foo.py
bash: ./foo.py: Permission denied
letian@fengPC:~$ ll | grep foo.py 
-rw-rw-r--   1 letian letian     72 May  4 15:02 foo.py
letian@fengPC:~$ chmod +x foo.py 
letian@fengPC:~$ ll | grep foo.py 
-rwxrwxr-x   1 letian letian     72 May  4 15:02 foo.py*
letian@fengPC:~$ ./foo.py
Hello world!
```

完美！到此为止我们已经达到了最初的目的了，不过为什么人家`chmod`能通过各种不同的参数来实现不同的功能呢，我们能否也如此狂拽酷炫屌呢？这不是明摆着可以么，不然我写这个标题干嘛。。。

python里面有个库，叫做`argparse`，它的官方文档在[这儿](https://docs.python.org/3/library/argparse.html)，顾名思义，它实现parse arguments的功能，让我等菜鸡省了好多的苦力，下面就贴一段最简单也最常用的示例代码，让大家稍微体会一下，更多的特性还是去翻文档吧咩哈哈哈:

```python
#!/usr/bin/python3
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--times', default=1, type=int, help='repeat hello world n times')

args = parser.parse_args(sys.argv[1:])
for i in range(args.times):
    print('Hello world!')
```

然后我们跑一下试试:
```bash
letian@fengPC:~$ ./foo.py --help
usage: foo.py [-h] [--times TIMES]

optional arguments:
  -h, --help     show this help message and exit
  --times TIMES  repeat hello world n times
letian@fengPC:~$ ./foo.py 
Hello world!
letian@fengPC:~$ ./foo.py --times 3
Hello world!
Hello world!
Hello world!
```

完美！

p.s. 本来想把执行带main函数的文件一起说的，然而现在才想起来。。。不过我自己也没有把python的项目结构完全搞懂，这次就不说了，万一说错了误导了各位就真的不合适了。

最后，祝大家码运昌隆！

