---
layout: post
title:  "辗转相除法"
date:   2017-10-16 21:25:00 +0200
categories: algorithm
---

在求取最大公约数时，遍历是很耗资源的，因此，可以选择辗转相除法。
存在两数为a和b（a>=b），求a和b最大公约数的步骤如下：

1. a除以b，得到商q和余数r；
2. 若r为0，则最大公约数为b；
3. 否则，给a重新赋值为r；
4. b除以a，得到新的商q和余数r；
5. 若r为0,则最大公约数为新的a；
6. 否则，给b重新赋值为r；
7. 跳至1.

Java的代码实现：
```
public class Main {
    public static void main(String[] args) {
        int a = 76;
        int b = 68;
        System.out.println(greatestCommonDivisor(a, b)); // 19
    }

    private static int greatestCommonDivisor(int a, int b) {
        // swap a & b if a < b
        if (a < b) {
            int tmp = a;
            a = b;
            b = tmp;
        }
        // logic part
        int r = a % b;
        while (r != 0) {
            a = b;
            b = r;
            r = a % b;
        }
        return b;
    }
}
```

