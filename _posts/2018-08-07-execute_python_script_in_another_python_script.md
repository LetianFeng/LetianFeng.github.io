---
layout: post
title: "在python脚本中调用另一个python脚本"
date: 2018-08-07 23:31:33 +0200
categories: python
tags: python
---

大家好久不见，毕设不是很顺利，焦头烂额了好一阵，这一个月几乎都浪费在寻找数据集和评估方式，预处理，训练并评估，被导师否决，重新寻找数据集和评估方式这样的死循环上了。。。很多重复但又有微妙不同的工作，代码很难管理和复用，没有学到什么非常值得分享的技术，抑或是遇到了但是因为忙着赶工没能及时分享然后现在不记得了。总之，这会儿在等一个模型训练完成，大概还要15分钟，正好有个小知识点，简单记录一下。  

因为我tensorflow学得很半吊子，毕设初期都是按脚本来写的，而且一个模型一个脚本，有不少相同的部分，但也有大量差异。现在想做成一个统一的脚本，直接在命令行里输入模型类别，以及每层的神经元个数，激励函数等就可以直接训练，省下我一行一行改in line设置的时间，也可以预防我漏改了某个设置得到错误数据的情况。理想的情况自然是把这些脚本都改成模块和函数等，在train.py里调用。可是一想到毕设时间之紧迫，而且这种程度的重构免不了一堆bug，实在是头疼。于是我就想能不能直接在train.py中调用其它的python脚本，这样以来我只需要尽量统一初期的模型训练脚本argparse部分，就可以以很少的代码量，实现我想要的功能了。  

于是Google大法好，stackoverflow教我做人，`os.system('/path/to/foo.py')`**搞定**！  

嗯，在写到这里之前我一直以为这就搞定了，不过，刚刚看了一眼[官方文档](https://docs.python.org/3.5/library/os.html#os.system)，发现事情并不简单，捡重要的贴给大家一下:  

```
Execute the command (a string) in a subshell. This is implemented by calling 
the Standard C function system(), and has the same limitations... 
...
The subprocess module provides more powerful facilities for spawning new 
processes and retrieving their results; using that module is preferable to 
using this function. See the Replacing Older Functions with the subprocess 
Module section in the subprocess documentation for some helpful recipes.  
```

代码块里贴不了链接，感兴趣的朋友可以点这里[Replacing Older Functions with the subprocess Module](https://docs.python.org/3.5/library/subprocess.html#subprocess-replacements)。简而言之，就是subprocess这个模块里有个function，叫做call，可以替代`os.system()`使用，使用方法如下:  

```python
sts = os.system("mycmd" + " myarg")
# becomes
sts = call("mycmd" + " myarg", shell=True)
```

写博客很开心，几个月前记录的技巧最近经常要跑回去翻看，省下了重新查找并构思如何应用到自己的代码中的时间，今天甚至还了解到了写博客之前没注意的知识点，真的是大有益处。  

最后想说的是，这种开process跑shell的骚操作其实并不稳，在毕设这种规模不算很大，又要赶时间的时候是一个很好的折衷，但如果是正经搞项目还是老老实实重构吧！
