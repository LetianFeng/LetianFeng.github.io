---
layout: post
title: "linux下截取文件前n行"
date: 2018-04-12 19:12:45 +0200
categories: linux
---

为了毕设要从3个API上抓数据做数据集，然而其中一个SciGraph的Redirect API不知为何down掉了，无法直接用DOI来获取想要的数据。只好退而求其次，从SciGraph上下载的n-triple数据集里获取SciGraph URL，进而访问SciGraph的Linked Data API来获取数据。但是nt数据集动不动就10几个G，我这PC总共才8G内存完全hold不住啊！

用less看了看发现nt数据集里是按照行来划分的，然后就想到我可以先把nt文件按照行切分成若干份，再逐个读取处理，在网上查了一下，立刻在Stackoverflow上找到了[答案](https://stackoverflow.com/questions/1411070/how-can-i-view-only-the-first-n-lines-of-the-file):

`head -n NUM filename`

此处的`NUM`应替代为期望截取的行数,`filename`替代为目的文件名，例如文件`foo.txt`的前10行就是:

`head -n 10 foo.txt`

但是这个命令只是显示前n行而已，如果想将前n行保存成一个新文件，就要配合`>`使用:

`head -n 10 foo.txt > bar.txt`

这里`>`的作用是将本应输出到屏幕上的东西转发给`bar.txt`这个文件，如果`bar.txt`原本有内容，就会完全被覆盖掉。如果使用`>>`的话，则是在原有文件的下方继续写，不会覆盖原有内容。
