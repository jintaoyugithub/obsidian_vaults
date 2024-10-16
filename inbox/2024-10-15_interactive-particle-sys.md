---
tags:
    - project
create date: 2024-10-15
urls:
---

# Interactive particle system

## Brainstrom

### 2024-10-15
Quick start for update texture: 

1. create a texture
2. track the position and click events of mouse
3. draw a small quad, for example 8x8, in that texture and update that texture

我看了一下FluidNinjia的一些视频，它其实是在一个2d texture上做fluid simulation，然后让那些volumetric的物体来采样这张纹理以达到interaction扽效果

如果利用数学公式，可以让raymarching将两个物体很smooth的融合在一起，那为什么不可以在交互的时候，生成一些小一点的ray marching box，然后里面的material就是比如说volumetrix cloud，用数学计算让这两个分离的smooth一点。

I found some youtube viedeos, check them later!

[introduce to flow map](https://www.youtube.com/watch?v=FvbPnndigL4)

[ray marching 2d fliud simulations](https://www.youtube.com/watch?v=TUk4sytRpfA)

[fliudninjia using flow map](https://www.youtube.com/watch?app=desktop&v=5ZoVDdFQuoE)

[fliudninjia detail maps and collision masking](https://www.youtube.com/watch?v=v8d0CalL9oA)

[parallax occlusion mapping](https://www.youtube.com/watch?v=-gDVyrPyvEs)

[Fliudninjia worldspace velocity](https://www.youtube.com/watch?v=rtsEwL33uUY)

[ray marching](https://www.youtube.com/watch?v=Cp5WWtMoeKg)

[3d collision detection using a triangle sdf](https://www.youtube.com/watch?v=chScv-vaXPo)


Question: 

1. How to make a object interact with the texture instead of using a mouse?

2. What about parallax mapping?

3. 如果把particl attach到object上面，只有当物体与云体交互的时候再生成粒子

详细可以参考[FluidNinjia volumetrix update](https://www.youtube.com/watch?v=jF4tXjPhw_c) at 0:15


### 2024-10-16

可不可以把生成的带有cloud material的ray marching的cube变成particle，这样就可以即有两个object之间的smooth融合又有粒子死亡带来的云朵消散。

参考一下[Chris' Graphics Blog](https://wallisc.github.io/rendering/2020/05/02/Volumetric-Rendering-Part-1.html)

怎么判断它up轴上的运动呢？

使用一个3d texture来记录3d fliud simulation的结果或者是记录vector field，然后用这个纹理来对云层采样？

比如说我们将一个cub分割成8x8的小格子，然后每个格子记录着当前粒子通过的平均的velocity vector

我觉得先可以看看不同的做法找找灵感，比如说

- flowmap
- 2d fliud simulation
- ray marching (optional)
