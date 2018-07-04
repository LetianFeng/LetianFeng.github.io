---
layout: post
title: "[转载]python中将生成器转化为迭代器"
date: 2018-07-04 08:46:23 +0200
categories: python
tags: python
---

好久没有更新，一直在忙毕设，前两天终于到了程序运行时间超过写代码时间的阶段，过来偷个懒。\
正好看到有一篇比较实用的英文博文，翻译过来和大家分享一下:\
[Easy way to make an iterator from a generator (in 6 lines) and when it's useful](https://www.reddit.com/r/Python/comments/40idba/easy_way_to_make_an_iterator_from_a_generator_in/)

==========================分割线==========================

首先来说说将生成器(generator)转化成迭代器(iterator)的动机:

问：我为什么想要迭代器/生成器?\
答：因为我无法处理会造成内存溢出的数据。

问：生成器与迭代器之间的区别是什么?\
答：生成器可以用于(从文件或者网络数据中)产生(潜在的)无限数据流，但只能被使用一次;\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
迭代器是一种有限(但庞大)数据的表示形式，不需要一次性向内存中载入全部数据，可以被使用(迭代)多次。

问：为什么将生成器转化为迭代器很重要?\
答：因为生成器(在python中)很容易实现，而迭代器可以被遍历多次

生成器示例 (逐行读取巨型文件):
```python
def lines_generator(filename):
    f = open(filename)
    for line in f:
        yield line
```
然后，在不将文件载入内存的情况下，遍历文件：
```python
generator = lines_generator(filename='file.txt'):
print('try number one')
for line in generator:
    print(line)

# try iterating over a second time and fail to print anything:
print('try number two:')
for line in generator:
    print(line)
```
但我们只能遍历一个生成器一次，所以我们想要的其实是一个迭代器(和一个简单的将生成器转化成迭代器的方法)。\
下面的六行代码兑现了我这个标题的承诺(老外这句好骚，The following are the six line of code as promised in the title)

```python
class MakeIter(object):
    def __init__(self, generator_func, **kwargs):
        self.generator_func = generator_func
        self.kwargs = kwargs
    def __iter__(self):
        return self.generator_func(**self.kwargs)
```
现在我们可以构建一个迭代器，并且想迭代几回就几回了：
```python
iterator = MakeIter(lines_generator, filename='file.txt'):
print('try number one')
for line in iterator:
   print(line)

# try iterating over a second time and succeed:
print('try number two:')
for line in iterator:
   print(line)
```
