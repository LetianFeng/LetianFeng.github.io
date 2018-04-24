---
layout: post
title: "jupyter与python的内核"
date: 2018-04-24 17:59:30 +0200
categories: python, jupyter, ipython
---

开始学TensorFlow了，开始在terminal里面搞，一出语法错误就要从头输实在心烦，于是打算开始用jupyter，然后
就“惊喜”地发现我一年前竟然已经装好了，心里暗暗窃喜自己真是有先见之明，殊不知这是去年的我挖下的巨巨巨>巨坑。。。

在进入正题之前，先介绍一下[jupyter](http://jupyter.org/)吧。嗯，大概就是一个网页版的python shell，可>以储存每一步的结果，这样如果某一步出了错误，只需修改这一小部分就可以继续执行，不像一般的script要完全>重跑，而且与python原生的shell相比，jupyter更像一个editor，所以修改起来很方便，不会出现for循环最后一行
多打一个括号就要从头再来一遍的崩溃场景（怨念

好了，接下来就说说我给自己挖的坑吧，之前已经配置好了native的python(3.5.2)和tensorflow(1.7.0)，确定可以调用这个包，然而在jupyter下面，当我执行最简单的`import tensorflow as tf`时，竟然出现了如下的错误：
```
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-2-41389fad42b5> in <module>()
----> 1 import tensorflow as tf

/usr/local/lib/python2.7/dist-packages/tensorflow/__init__.py in <module>()
     22 
     23 # pylint: disable=wildcard-import
---> 24 from tensorflow.python import *
     25 # pylint: enable=wildcard-import
     26 

/usr/local/lib/python2.7/dist-packages/tensorflow/python/__init__.py in <module>()
     49 import numpy as np
     50 
---> 51 from tensorflow.python import pywrap_tensorflow
     52 
     53 # Protocol buffers

/usr/local/lib/python2.7/dist-packages/tensorflow/python/pywrap_tensorflow.py in <module>()
     50 for some common reasons and solutions.  Include the entire stack trace
     51 above this error message when asking for help.""" % traceback.format_exc()
---> 52   raise ImportError(msg)
     53 
     54 # pylint: enable=wildcard-import,g-import-not-at-top,unused-import,line-too-long

ImportError: Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/pywrap_tensorflow.py", line 41, in <module>
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 28, in <module>
    _pywrap_tensorflow_internal = swig_import_helper()
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 24, in swig_import_helper
    _mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
ImportError: libcublas.so.8.0: cannot open shared object file: No such file or directory


Failed to load the native TensorFlow runtime.

See https://www.tensorflow.org/install/install_sources#common_installation_problems

for some common reasons and solutions.  Include the entire stack trace
above this error message when asking for help.

```

咦，我选的是python3的kernel啊，为什么会向2.7的路径去查询tensorflow呢，我很疑惑，经过了0.2s的思索后我打开了google，然而，这一次，我竟然找不到和我遇到一样问题的人！！！持续搜索了1个小时依旧无功而返后，我向一位同学请教，得知新手最好还是不要用native的python来搞机器学习，现在流行的是anaconda和virtualenv这样的虚拟环境，这样就可以回避掉大部分的python版本冲突问题了。

从善如流的我立刻去装了这个逼，啊不，是anaconda，然后认真学习了user guide，之后就欣喜地发现:这特喵的没用啊，即便anaconda安装的是最新版的python(3.6.4)和tensorflow(1.7.0)，但报的错误完全没区别啊！这让我同学的脸往哪儿搁！

之后又尝试和思考了许久，我又回到了开始的思路，会不会kernel的问题，不仅仅是tensorflow，会不会所有的package都是从2.7的路径去导入?或者说干脆这个kernel根本是披着python3羊皮的python2.7哈士奇?在执行了`import sys`和`print(sys.version)`以后，我得到了我最不想看到的答案:
```
2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609]
```

所以说，遇到问题，别总想着依赖google，别总想着依赖同学，大家都写了这么久的代码了，第一感觉一般方向上还是差不离，这次就是典型的舍近求远了。这下问题不再是极其具体的难以复制的问题了，而是一个很明显的大问题，一下子就找到了两个相关的网页，竟然都是GitHub上的issue页面，看来难兄难弟不少嘛(滑稽)，这里贴一下链接好了，是[Jupyter running wrong python kernel](https://github.com/jupyter/jupyter/issues/270)和[Jupyter Notebook is loading incorrect Python kernel](https://github.com/jupyter/notebook/issues/2563)这两篇。

具体来说就是通过命令`jupyter kernelspec list`可以查看jupyter各个kernel的配置文件路径，比如我的python3 kernel就在目录`/usr/local/share/jupyter/kernels/python3`下，我打开了该路径下的kernel.json文件，看到了让人崩溃的一幕:
```json
{
 "argv": [
  "/usr/bin/python",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ],
"display_name": "Python 3",
"language": "python"
}
```

/usr/bin/python老哥啊，你的3呢！你的3呢！！！！！！！！我悲伤地加上了3,然后运行`jupyter notebook`，果然，一切运行平稳，岁月静好，今天画上了圆满的句号。。。才怪！

你以为我会就这样满足吗？不！我还没搞明白自己是怎么踩进这个坑的好吗，而且我刚刚用anaconda安装的可是3.6.4，这两个python3 kernel可不一样，如果我activate了anaconda的python3 env，还能import tensorflow吗?我试了一下，答案是果然不能。

首先，该如何添加python3.6.4的kernel呢，其实在上面两个issue的页面里就有人给出了答案:我系渣渣辉，只需轻轻一点`ipython3 kernel install`，装备立刻能换钱，你从未体验过的船新版本！如果看一眼help，你会发现，甚至可以给kernel命名name和display-name，以及设置为只有你的用户可见。比如:

```
ipython3 kernel install --user --name python35 --display-name='Python 3.5'
```

但是在这之后<span style="color:red">**一定要手动修改对应的kernel.json里文件中argv的第一行，一定要手动修改对应的kernel.json里文件中argv的第一行，一定要手动修改对应的kernel.json里文件中argv的第一行**</span>，指向对应的python kernel路径，否则你就会和我一样，爱上被自己坑死的感觉。。。

嗯，最后总结一下，anaconda可以安装多个版本的python和tensorflow等packages，但是需要手动install对应的ipython kernel，install完成后记得进入对应的kernel.json里检查路径是否正确。

p.s. 最后这里要手动修改让我感觉不太对，但ipython3 kernel install能提供的args并不能直接改变kernel的源路径，可能需要在此之前对ipython3本身进行设置?今天实在是有点累了，暂且休息了，若哪位高手知道，欢迎来个邮件传授一下在下(GitHub的blog没有留言功能，我又太弱不会搭自己的网站。。。)

