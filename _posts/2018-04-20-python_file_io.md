---
layout: post
title: "python的文件读写"
date: 2018-04-20 19:25:37 +0200
categories: python
---

今天写了一个小的辅助程序，先截取n-triple文件的前n行存储为一个临时文件，再将这n行中的url提取出来，并转换成list，最后存储为另一个json文件。在这个过程中，遇到了一个小问题，就是使用IDE来运行程序的话，就无法从临时文件中提取出url，而用命令行程序则可以顺利完成上述任务。

问题代码大致如下：
```python
# load first n lines from data.nt

# save n-lines into tmp.nt
nt_file =  open(tmp_path, 'w'):
for nt in head:
    nt_file.write(nt)

# load data from tmp.nt using rdflib
```

Debug了一下午啊。。。还去看了rdflib里的源码啊。。。最后忽然发现，咦，我明明已经step过存tmp.nt的部分了，怎么这个文件还是空的啊？我去，等等。。。不是吧。。。我好蠢啊啊啊啊啊啊啊！

嗯，是这样的，open完file，然后写，但是我特么忘了close了！！！！直到整个脚本跑完，这个file才会被自动close掉，到那时临时文件才有内容，所以这之后用命令行再运行一遍这些脚本才有效。IDE，我错怪你了，这个锅还是我自己背吧= =

所以正确的代码如下:

```python
# load first n lines from data.nt

# save n-lines into tmp.nt
nt_file =  open(tmp_path, 'w'):
for nt in head:
    nt_file.write(nt)
# attention!!!!!!!!!!!!!!!!!!!!!!!!!!!!
nt_file.close()

# load data from tmp.nt using rdflib
```

除此之外，如果在读写的过程中发生异常，文件也是不会被正常关闭的，这个时候可以使用我上一篇博客里提到的`try...finally...`来处理，或者直接使用下面python的`with`关键字，python君会帮你完成close的逻辑:

```python
with open('/path/to/file', 'r') as f:
    print(f.read())
```

这一部分廖雪峰大大的教程讲得很清楚，大家想看的话请点这个**[传送门](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431917715991ef1ebc19d15a4afdace1169a464eecc2000)**，我就不复制粘贴了，并不是我懒哟，真的不是哟:)

