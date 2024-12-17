---
tags:
    - unreal-engine
create date: 2024-12-15
urls:
---

# Blueprint Overview

**Inheritance** in unreal engine:

**Object** -> **Actor** -> **Pawn** -> **Character**

`Object`: provide core function like garbage collection

`Actor`: inherited from `Object` can be spawned in the world, which means it has **transform** component.

`Pawn`: inherited from `Actor`, can receive input from a `Controller`

`Character`: inherited from `Pawn`, has differenct components like skeletal mesh, movement etc.

For each **components** of the current blueprint, you can add event to it, like

## Blueprint vs. C++

Blueprint is more easy for you to implement a functionality you want while C++ is more usefule when you try to optimize your code like memory management etc

It's annoying when you have to type the whole path in the code while you only need to drag the thing in blueprint and in blueprint, when someone don't want to use the references you set, or they deleted the reference accidently, blueprint will have a redirect action but c++ won't.

Recommandation is you should use both! **Prototype in blueprint, optimize in C++**.


## Assignments

- [ ] Turn on the light when the character is close enough to a door, oppsite when the character leave

Note: timeline, collider overlap event, flip flop


## Questions

1. 为什么对于`Construction Script`来说，每移动一次物体就会调用一次？比如说

```cpp
Construction Script -> Print String(Hello)
```

每移动下物体，就会打印一次hello

