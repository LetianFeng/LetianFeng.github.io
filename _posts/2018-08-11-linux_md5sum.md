---
layout: post
title: "linux命令行校验工具md5sum"
date: 2018-08-11 10:54:54 +0200
categories: linux
tags: linux md5
---

今天用到了DBLP，从官网上下载数据集文件dblp-2018-08-01.xml.gz和校验码文件dblp-2018-08-01.xml.gz.md5，那么如何校验我们下载的数据集是否完整呢? 我们需要用到一个命令行工具md5sum，来计算数据集文件的的md5码: 

```bash
letian@fengPC:~/Desktop/DBLP$ md5sum dblp-2018-08-01.xml.gz
e110553fb5148204544a25bdae613e0f  dblp-2018-08-01.xml.gz
```

然后我们可以和校验码文件进行比对: 

```bash
letian@fengPC:~/Desktop/DBLP$ cat dblp-2018-08-01.xml.gz.md5 
e110553fb5148204544a25bdae613e0f  dblp-2018-08-01.xml.gz
```

完全一致，说明我们下载的数据集是完整的。**但是**，需要人工比对md5简直毫无人性，效率低还容易出错，那么让我们来一起看一看md5sum正确的打开方式: 

```bash
letian@fengPC:~/Desktop/DBLP$ md5sum -c dblp-2018-08-01.xml.gz.md5
dblp-2018-08-01.xml.gz: OK
```

其实刚刚我们`cat dblp-2018-08-01.xml.gz.md5`的时候就发现了，`md5`文件中是有固定格式的，即`md5-code filename`，所以使用`md5sum`可以读取`md5`文件中的信息并自动校验，是不是很方便！

最后，附一下`md5sum --help`，还有很多其它的功能可以使用: 
```
letian@fengPC:~/Desktop/DBLP$ md5sum --help
Usage: md5sum [OPTION]... [FILE]...
Print or check MD5 (128-bit) checksums.

With no FILE, or when FILE is -, read standard input.

  -b, --binary         read in binary mode
  -c, --check          read MD5 sums from the FILEs and check them
      --tag            create a BSD-style checksum
  -t, --text           read in text mode (default)

The following five options are useful only when verifying checksums:
      --ignore-missing  don't fail or report status for missing files
      --quiet          don't print OK for each successfully verified file
      --status         don't output anything, status code shows success
      --strict         exit non-zero for improperly formatted checksum lines
  -w, --warn           warn about improperly formatted checksum lines

      --help     display this help and exit
      --version  output version information and exit
```
