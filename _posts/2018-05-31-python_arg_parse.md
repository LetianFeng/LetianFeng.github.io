---
layout: post
title: "使用argparse解析python命令行参数"
date: 2018-05-31 17:06:55 +0200
categories: python
tags: python
---

今天讲一讲如何使python程序可以解析命令行参数。平时，我们在命令行下使用工具时，经常会附加参数，以获取扩展的功能，以linux下最简单的`ls`为例（下面这个代码块摘自python文档[Argparse Tutorial](https://docs.python.org/3.6/howto/argparse.html)）:

```bash
$ ls
cpython  devguide  prog.py  pypy  rm-unused-function.patch
$ ls pypy
ctypes_configure  demo  dotviewer  include  lib_pypy  lib-python ...
$ ls -l
total 20
drwxr-xr-x 19 wena wena 4096 Feb 18 18:51 cpython
drwxr-xr-x  4 wena wena 4096 Feb  8 12:04 devguide
-rwxr-xr-x  1 wena wena  535 Feb 19 00:05 prog.py
drwxr-xr-x 14 wena wena 4096 Feb  7 00:59 pypy
-rw-r--r--  1 wena wena  741 Feb 18 01:01 rm-unused-function.patch
$ ls --help
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
...
```

可见，如果我们能够在程序中加入命令行解析的功能，就可以给用户带来极大的便利。python中集成了一个非常好用的命令行解析模块argparse，下面我以x的y次幂为例，介绍一下argparse的使用方法（这个代码块同样摘自python文档[Argparse Tutorial](https://docs.python.org/3.6/howto/argparse.html)）。

```python
import argparse

# initial a parser with description
parser = argparse.ArgumentParser(description="calculate X to the power of Y")

# add --verbose and --quiet to a mutually exclusive group, so that they conflict with each other
group = parser.add_mutually_exclusive_group()
# --verbose and --quiet are optional arguments
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

# x and y are positional(mandatory) arguments
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")

# parse arguments, equivalent to **parser.parse_args(sys.argv[1:])**, but simpler
args = parser.parse_args()

answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))
```

我加了几行注释方便大家看，翻译成中文就是:
1. 可以在生成parser的时候用descritption这个parameter对parser添加一个描述，效果参加下方输出;
2. --verbose和--quiet是optional（可选）参数，x和y是positional（固定位置，可以理解为必选）参数，他们的区别就在于有无前置的减号`-`;
3. optional参数可以有缩写（长的用`--`开头，叫做name，多的用`-`开头，叫做flag）;
4. optional参数有2种用法，这里的verbose和quiet都是不带后续值的，带后续值的我会在文章最后的代码块里讲;
5. position参数在使用时不必像optional参数那样显式声明参数名，直接将值放在对应位置即可;
6. 对比我在之前一篇博客《[带参数的python可执行文件
](https://letianfeng.github.io/python/2018/05/04/executable_python_script_with_arguments.html)》里的例子，`parser.parse_args()`显然比`parser.parse_args(sys.argv[1:])`要简单得多，而且不必`import sys`，推荐。

```bash
letian@fengPC:~/myblog/examples$ python3 parser1.py -h
usage: parser1.py [-h] [-v | -q] x y

calculate X to the power of Y

positional arguments:
  x              the base
  y              the exponent

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose
  -q, --quiet
letian@fengPC:~/myblog/examples$ python3 parser1.py 4 2
4^2 == 16
letian@fengPC:~/myblog/examples$ python3 parser1.py 4 2 -q
16
letian@fengPC:~/myblog/examples$ python3 parser1.py 4 2 -v
4 to the power 2 equals 16
letian@fengPC:~/myblog/examples$ python3 parser1.py 4 2 -vq
usage: parser1.py [-h] [-v | -q] x y
parser1.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
letian@fengPC:~/myblog/examples$ python3 parser1.py 4 2 -v --quiet
usage: parser1.py [-h] [-v | -q] x y
parser1.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
```

好的，最后，再来演示一下在含有main函数的python文件中，如何加入parser功能:

```python
#!/usr/bin/python3

import argparse


def main(args):
    answer = args.x**args.y
    if args.bias:
        answer += args.bias

    if args.quiet:
        print(answer)
    elif args.verbose:
        if args.bias:
            print("{} to the power {} plus bias {} equals {}".format(args.x, args.y, args.bias, answer))
        else:
            print("{} to the power {} equals {}".format(args.x, args.y, answer))
    else:
        if args.bias:
            print("{}^{}+{} == {}".format(args.x, args.y, args.bias, answer))
        else:
            print("{}^{} == {}".format(args.x, args.y, answer))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="calculate X to the power of Y, then add a bias if you like")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")

    parser.add_argument("-b", "--bias", type=int, help="the bias")

    main(parser.parse_args())
```

之所以将parser部分放在`if __name__ == '__main__':`的代码块里，是因为这样可以防止这个python文件被import时仍然执行parser部分代码，但没有arguments可以拿来解析所带来的error，比如:

```bash
letian@fengPC:~/myblog/examples$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import parser1
usage: [-h] [-v | -q] x y
: error: the following arguments are required: x, y
letian@fengPC:~/myblog/examples$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import parser2
>>> 

```

这样，如果想在import时仍然使用args，也可以手动生成args，再调用parser2.main(args)来实现。

最后，我们来看一下输出:

```bash
letian@fengPC:~/myblog/examples$ ./parser2.py -h
usage: parser2.py [-h] [-v | -q] [-b BIAS] x y

calculate X to the power of Y, then add a bias if you like

positional arguments:
  x                     the base
  y                     the exponent

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose
  -q, --quiet
  -b BIAS, --bias BIAS  the bias
letian@fengPC:~/myblog/examples$ ./parser2.py 3 2
3^2 == 9
letian@fengPC:~/myblog/examples$ ./parser2.py -b 5 3 2
3^2+5 == 14
letian@fengPC:~/myblog/examples$ ./parser2.py -q 3 2
9
letian@fengPC:~/myblog/examples$ ./parser2.py -q -b 5 3 2
14
letian@fengPC:~/myblog/examples$ ./parser2.py -v 3 2
3 to the power 2 equals 9
letian@fengPC:~/myblog/examples$ ./parser2.py -v -b 5 3 2
3 to the power 2 plus bias 5 equals 14
letian@fengPC:~/myblog/examples$ ./parser2.py -vq -b 5 3 2
usage: parser2.py [-h] [-v | -q] [-b BIAS] x y
parser2.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
```

从这次开始，我会把文章中代码传到[examples文件夹](https://github.com/LetianFeng/letianfeng.github.io/tree/master/examples)下，大家直接clone或者pull就可以执行了，免得还要复制粘贴，嘿嘿。

如果有发现我写错的地方，欢迎邮件联系我<letian.feng@hotmail.com>，或者直接在这个博客的[repo](https://github.com/LetianFeng/letianfeng.github.io)里提pull request或issue也可以，谢谢！
