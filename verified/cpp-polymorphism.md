---
tags:
    - cpp
create date: 2024-10-14
urls: 
    - [virtual func, virtual inherit and polymorphism](https://zhuanlan.zhihu.com/p/136478734)
---

# Cpp Polymorphism

I've been writing a rendering framework call [[Shift]], here is the [github link](https://github.com/jintaoyugithub/Shift). This project is based on a more low level rendering lib call [bgfx](https://github.com/bkaradzic/bgfx) and I need to develop some tools and classes for my own project. 

Basically I take the codes in the example folder as references and they use a bunch of virtual functions, I think I know the basic of the virtual functions but I only know a few details of virtual functions and more broadly polymorphism, so I decide to take some notes.

## Basic

`Polymorphism` is one of the most important featrues of cpp, other two are `inherit` and `abstract`. Briefly we have a **Base Class** which determine the basic code of conduct, and we have bunch of **Derived Class** which inherit the public and protected properties from the **Base Class**. 

Polymorphism makes us be able to use the `Pointer` of a **Base Class** to execute the right functions overwrite in the **Derived Class**.

**Note**: Only virtual deconstructor will be execute recursively, common virtual functions won't. That's why if we have a pure virtual class, the deconstructor must be marked as virtual.

For example:

```cpp
class A {
    // ...
    virtual ~A() {
        log("Deconstructor call by A");
    };

    virtual func() {
        log("Func call by A");
    };
};

class B : public A {
    // ...
    virtual ~B() {
        log("Deconstructor call by B");
    };

    virtual func() {
        log("Func call by B");
    };
};

int main() {
    A* a = new B();
    a->func();

    // free the memory of the pointer
    delete a;
}
```
The output is:

```
Func call by B
Deconstructor call by B
Deconstructor call by A
```

As you can see, although *a* is a pointer which pointing to A but we assign it with B, then we call the function `func`, depending on the polymorphism of cpp, *a* still can find the right function to call.


## Virtual and pure virtual function

```cpp
class A {
    // a virtual function
    virtual func();

    // a pure virtual functions
    virtual funcV() = 0;
}
```
The class which has pure class functions will be considered as `pure virtual class`, which specified the code of conduct of its derived classes and can not has instancees.

We can take `pure virtual class` as the concept of **Interface** in other programming languages, which **only has declarations and no implementations** the implementations is required in the derived classes.

## Virtual table 

**Virtual table** is a table full of function pointers and created after we instantiate class A.

```cpp
class A {
    virtual funcOne() {
        ... 
    }
    virtual funcTwo() {
        ...
    }
};

class B : public A {
    virtual funcThree() {
        ...
    }
    virtual funcFour() {
        ...
    }
};

class C : public A {
    virtual funcOne() {
        ...
    }

    virtual funcFive() {
        ...
    }
};
```
When we instantiate all the three classes above, we will get three virtual table

For A's virtual table, it obviously has two virtual functions 

![vtbl1.png](assets/imgs/vtbl1.png)

For B's virtual table, it has four virtual functions because it didn't overwrite any virtual functions in class A, and it has two virtual functions by its own.

![vtbl2.png](assets/imgs/vtbl2.png)

For C's virtual table, because C overwrite the virtual function `funcOne()` in the base class A, so it only has 3 virtual functions in total

![vtbl3.png](assets/imgs/vtbl3.png)

## Tips

1. Make sure you implement all pure virtual functions in the **Base Class** otherwise you will get a compile error

2. A completely new way of polymorphism in cpp, refer to [proxy](https://github.com/microsoft/proxy) developed by Microsoft.


## FAQ

1. how we determine if a func should be a virtual func of not?

Think about if inherit and polymorphism are needed in you project, because virtual table and functions call are also a cost.

In cpp, we have `runtime abstraction` and `compile-time abstraction`, **virtual func** is one solution for the first one and **template** is the solution for the second one.

2. [[stdfunction]] vs. virtual functions

Seems like a lot of people advise me to use `std::function` instead of `virtual function`.

