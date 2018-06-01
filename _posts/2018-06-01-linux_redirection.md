---
layout: post
title: "linux重定向简介"
date: 2018-06-01 21:40:00 +0200
categories: linux
tags: linux
---

今天在和同学一起做nlp作业的时候遇到了一个小问题，我们用[sent2vec](https://github.com/epfml/sent2vec)训练了一个binary模型，可以在linux的命令行下面执行，每次可以输入一个句子，然后这个模型就会生成一个对应的长度为300的vector，并在屏幕上输出。

我们的任务是将若干个文本文件中的句子转换为vector，再存为另一个文件，其中输入文件的每一行都是一个句子，输出文件的每一行应句子对应的vector，我语言描述的不太清楚，画了个草图，大家一看应该就明白了:

![sent2vec](https://raw.githubusercontent.com/LetianFeng/letianfeng.github.io/master/images/linux_redirection_1.png)

显然，我们不可能手动一行一行地复制粘贴，而是使用工具来提升效率，并避免人工错误。这个工具就是linux自带的redirection功能，它分为3部分<sup>[[1]](http://cn.linux.vbird.org/linux_basic/0320bash_5.php)</sup>:

1. stdin，标准输入，代码为0，使用`<`或`<<`；
2. stdout，标准输出，代码为1,使用`>`或`>>`；
3. stderr，标准错误输出，代码为2,使用`2<`或`2>>`；

![linux redirection](https://raw.githubusercontent.com/LetianFeng/letianfeng.github.io/master/images/linux_redirection_2.png)<sup>[[2]](https://ryanstutorials.net/linuxtutorial/piping.php)</sup>

对于stdout和stderr，`>`代表覆盖写，`>>`则代表在文件末尾追加；对于stdin来说，`<`右边的文件取代键盘作为新的输入方式，`<<`右边的字符串代表结束输入的关键字，比如EOF，注意必须是完全匹配才能结束输入:

```
letian@fengPC:~/myblog/_posts$ cat << EOF
> hi
> there
> 123EOF
> EOF
hi
there
123EOF
```

所以，针对文章开头我们提到的任务，我们所应执行的命令行如下:

```
letian@fengPC:~/Desktop/nlp/src/sent2vec$ ./fasttext print-sentence-vectors
usage: fasttext print-sentence-vectors <model>

  <model>      model filename

letian@fengPC:~/Desktop/nlp/src/sent2vec$ ./fasttext print-sentence-vectors model.bin < input.txt > output.txt
```

其中，`./fasttext print-sentence-vectors model.bin`是启动这个工具，然后`< input.txt`将句子一行接一行地输入进来，之后model会把句子转为vector，再由`> output.txt`一行接一行地输出到目的文件中去。


#### **来源:**

1. [鸟哥的Linux私房菜 -- 学习 bash shell](http://cn.linux.vbird.org/linux_basic/0320bash_5.php)
2. [Linux Tutorial - 11. Piping and Redirection](https://ryanstutorials.net/linuxtutorial/piping.php)

如果有发现我写错的地方，欢迎邮件联系我<letian.feng@hotmail.com>，或者直接在这个博客的[repo](https://github.com/LetianFeng/letianfeng.github.io)里提pull request或issue也可以，谢谢！
