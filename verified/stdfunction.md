---
tags:
    - cpp
create date: 2024-10-15
urls:
    - [std::function详解与实战](https://zhuanlan.zhihu.com/p/390883475)
    - [Why we need std::function](https://zhuanlan.zhihu.com/p/565796718)
---

# std::function

Recently I've been learning polymorphism and I found out not only `virtual function`, but also `function pointer` can also be a solution to implement polymorphism in cpp.

std::function is a **function pointer wrapper** which store any callable object like functions, functors, lambda expression etc only if the signature can match, usually the signature will be the *return type* and *paramters type*, for example void(int);

## Basic

Like I mention, std::function can store any callable object, but the usage among them might be a little different

```cpp
#include <functionnal>

/* function pointer */

/* function */

/* template function */

/* function object */

/* lambda expression */

/* static function */

/* class member function */

```

## Polymorphism with std::function

After virtual function, std::function make other solutions to **runtime abstraction** possible. It's heavily used in [[callback-function]].


## FAQ

1. Why we need std::function when we already have the function pointer?

If you familiar with **pointer** in cpp, you know a pointer is pointing to a variable. Same for **function pointer**, it points to a block of code instead of one single variables.

But std::function is a little bit more than a function pointer, it also store the variables or context that the function will need, for example:


