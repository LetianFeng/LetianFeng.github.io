---
layout: post
title: "使用Google Analytics监控GitHub Pages访问流量"
date: 2018-05-27 10:43:12 +0200
categories: github
tags: github
---

利用GitHub Pages使得我们可以很方便地搭建自己的博客，然而GitHub自带的分析工具却只能监控某个repo的访问流量,无法监控博客的流量，而Google Analytics这个免费的流量监控工具则提供了完美的补充，如何使两者一起工作呢？

首先，当然是去[Google Analytics](https://www.google.com/analytics/)注册一个账户，界面大概长下面这样，主要是填好账户名，网站名称和URL，然后拖到页面最下方Get Tracking ID就好了:

![Google Analytics Account](https://raw.githubusercontent.com/LetianFeng/letianfeng.github.io/master/images/google_analytics.png)

接下来，就要用到我们的Tracking ID了，如果不小心关了刚刚的页面，也可以在Google Analytics的网站的Admin > Property > Tracking Info > Tracking Code路径下找到。有两种方法来将Google Analytics的功能加入到我们搭建在GitHub Pages上的博客中。

***方法一***

如果你使用的是GitHub Pages官方提供的模板的话，那事情就非常简单了，只需在repo根目录下的的_config.yml文件中添加如下配置即可，注意请将下面的UA-XXXXXXXXX-X更改成你自己的Tracking ID。

```
# Google Analytics
google_analytics: UA-XXXXXXXXX-X
```

不过不同模板的具体配置可能不同，如果上面的配置不起作用的话，请到该模板的repo的README中查找。（附: [GitHub Pages Themes](https://pages.github.com/themes/)）

***方法二***

直接向GitHub Pages中的html文件添加Google Analytics提供的代码块儿，感兴趣的同学请参照这篇[blog](https://michaelsoolee.com/google-analytics-jekyll/)。

然后commit，push，打开你的博客（GitHub Pages生成新的静态页面可能需要等待几分钟），再访问你的Google Analytics首页，就会发现你得到了第一个访客。虽然知道是你自己，但仍然是很开心的一件事不是吗~
