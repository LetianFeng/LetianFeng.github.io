---
layout: post
title: "python的异常处理"
date: 2018-04-19 20:00:15 +0200
categories: python
---

继续给毕设抓数据，今天把抓数据的程序放到GitHub上了，具体在[这个repo](https://github.com/LetianFeng/makeDataset/tree/master)，因为是python小白，程序写得肯定各种不合理，欢迎各位路过大神指正，然而这鬼东西除了我应该不会有人看吧（滑稽）。

根据python的[官方文档](https://docs.python.org/3/tutorial/errors.html)，我们可以很直观地了解到异常处理的基本语法如下:

```python
try:
    pass
except ValueError:
    print('Lalala~')
except HTTPError as err:
    if err.code == 404:
        print('Do you know GFW?')
except (Exception, KeyboardInterrupt):
    print('Have someone pushed ctrl-c?')
except:
    print('Interesting!')
    raise
else:
    print('No exception! Celebrate!')
finally:
    print('This line will be printed anyway.')
```

和java很像，在`try`下面的代码块里写逻辑，然后用`except`关键字来抓取异常。可以处理单独种类的异常，也可以用tuple的形式`(Exception1, Exception2)`来处理多种异常，甚至可以不特地声明异常类型，直接`except:`搞所有，当然这招太bug了，各位和我水平差不多的同学一定要慎用。。。(补充一下，`except:`必须放在全部有具体异常的`except XX`之后，否则会报语法错误`SyntaxError: default 'except:' must be last`)

除此之外还有两个optional的关键字`else`和`finally`，这两位可都不好伺候(此处参考了一下[这篇博客](https://www.cnblogs.com/windlazio/archive/2013/01/24/2874417.html)，不过各位同学放心，我在命令行下测试了的，并不是照抄):

1. `else`前面必须有至少一个`except`，并且必须在`finally`之前，稍微换一下顺序都不行。一般人家都追求"一人之下，万人之上"，这位倒好，铁了心当"一人之上，万人之下"，实在是难以理解`else`老哥的心态。。。至于功能嘛，就是处理之前的`except`们没有处理的情况咯;
2. `finally`必须放在最后，就是说但凡有except，甭管是1个，多个，还是最牛逼的`except:`。然后`finally`的作用就是"此山是我开，此树是我栽，甭管有没有异常，起码得给爷笑一个吧嘿嘿嘿"。


啊，对了对了，差点忘了说，一般情况下，我们会根据不同的异常执行不同的操作，这就不得不提一下`raise`这个关键字了，它是干什么的呢？对！就是老子搞不死你个小破异常，你等着，我叫我大哥来搞你(将异常继续抛给上层程序)！

最后说一个小坑，`KeyboardInterrupt`竟然不是`Exception`的子类啊啊啊啊啊啊啊啊啊啊！

