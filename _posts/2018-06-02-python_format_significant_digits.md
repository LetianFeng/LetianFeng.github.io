---
layout: post
title: "在python中利用Formatter保留有效数字"
date: 2018-06-02 10:00:00 +0200
categories: python
tags: python
---

依旧是上一篇文章中的问题，这一次我们换了[word2vec](https://code.google.com/archive/p/word2vec/)模型，不过这一次的model不能在命令行下直接使用，而是必须由python中的[gensim](https://radimrehurek.com/gensim/models/word2vec.html)模块加载后才能使用，这就带来了一个问题，python中的浮点数精度很高，如果我们输出时只需要保留n位有效数字，或者小数点后n位该怎么办呢？

![sent2vec](https://raw.githubusercontent.com/LetianFeng/letianfeng.github.io/master/images/linux_redirection_1.png)

python的Formatter可以很好地帮我们解决这个问题。Formatter原本是用于规整字符串的一个类，最简单也是最常见的用法是使用Formatter的`format()`函数在字符串中占位，然后填充变量的值，相较其它语言必须在占位的同时声明类型的语法，真的是非常友好:

```python
>>> 'Hello {}, I‘m {} years old.'.format('world', 26)
'Hello world, I‘m 26 years old.'
```

言归正传，如何保留n位有效数字和小数点后n位呢？这时候就需要额外的关键字了，这个关键字在[官方文档](https://docs.python.org/3.6/library/string.html)里叫format_string，甚至还为这个format_string专门搞了一个mini language，大概可以直接parse成语法树。。。<sup>[[1]](https://docs.python.org/3.6/library/string.html#format-specification-mini-language)</sup>

其中，保留有效数字的关键字是`g`，小数点后n位数的则是`f`，还有科学计数法`e`和转换成百分比之后保留小数点后n位数的骚操作`%`。示例如下:

```python
>>> format(12.456789, '.3g')
'12.5'
>>> format(12.456789, '.3f')
'12.457'
>>> format(12.456789, '.3e')
'1.246e+01'
>>> format(12.456789, '.3%')
'1245.679%'
```

#### **来源:**

1. [15. Floating Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html)
2. [6.1.3.1. Format Specification Mini-Language](https://docs.python.org/3.6/library/string.html#format-specification-mini-language)

如果有发现我写错的地方，欢迎邮件联系我<letian.feng@hotmail.com>，或者直接在这个博客的[repo](https://github.com/LetianFeng/letianfeng.github.io)里提pull request或issue也可以，谢谢！
