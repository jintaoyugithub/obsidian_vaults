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
- sdf

使用少量的paritcle来做fliud simulation，然后将结果写入一张texture，再在这张texture上做noise 

这个交互系统最重要的是我要如何记录角色的位置，以及什么时候该将交互信息写入纹理

- scene capture，也就是一个在角色脚下的摄像机，记录角色的高度，用这个高度来和场景中其他物体的高度做比较，来确认是否要做交互

在ue中还使用到了runtime virtual texture, check the videos:

[Pathways & Roads using RVTs](https://www.youtube.com/watch?v=momc4h5J19Y)

- 像[Prismatiscape Interaction Plugin](https://www.youtube.com/watch?v=OgXrpMdpkHA)视频中提到的，完全使用material和runtime virtual texture来做交互

但是opengl中并没有runtime virtual texture这种东西，这是引擎对大量加在纹理做的一种优化技术

virtual texture 在这里的作用就是用来构建虚拟高度场

我觉得现在的工作顺序就是

1. 完成2d eulerian fliud sim 
2. 先采用scene capture的形式来做交互，rvt可以考虑作为一个bonus
3. 最后考虑使用什么来做showcase，ray marching clouds?

那粒子系统还有用吗?

可以把粒子系统中的粒子更换material/shader吗，这样后续就可以apply ray marching clouds的shader上去了

**References found today**:

- [为Unity实现Runtime Virtual Texture](https://zhuanlan.zhihu.com/p/452875365)
- [UE4 Runtime Virtual Texture 实现机制及源码解析](https://zhuanlan.zhihu.com/p/143709152)
- [Virtual Texture（虚拟纹理）的理解和应用](https://www.bilibili.com/video/BV1KK411L7Rg/?vd_source=0fcddcb3612de862c70bcf69ba163263)
- [Virtual Texture](https://zhuanlan.zhihu.com/p/676075965)

[浅谈Virtual Texture](https://zhuanlan.zhihu.com/p/138484024)

Unreal Virtual Texture 源码导读https://zhuanlan.zhihu.com/p/147213120

Unity GPU collision detection
https://github.com/drzhn/UnityGpuCollisionDetection

Chapter 32. Broad-Phase Collision Detection with CUDA
https://developer.nvidia.com/gpugems/gpugems3/part-v-physics-simulation/chapter-32-broad-phase-collision-detection-cuda

Unity Raymarching Collision
https://github.com/hecomi/UnityRaymarchingCollision

Real-time dreamy Cloudscapes with Volumetric Raymarching
https://blog.maximeheckel.com/posts/real-time-cloudscapes-with-volumetric-raymarching/

Collision Detection for Raymarch Objects
https://www.floneyyang.com/post/collision-detection-for-raymarch-objects

my experience as a frontend engineer
https://blog.maximeheckel.com/

Moebius-style post-processing and other stylized shaders
https://blog.maximeheckel.com/posts/moebius-style-post-processing/

An Introduction to Raymarching
https://typhomnt.github.io/teaching/ray_tracing/raymarching_intro/

Intro to Vertex Colour [Unreal Engine]
https://www.youtube.com/watch?v=vIA2oU4JNmY&t=24simulations

Runtime Vertex Paint || The Best Bang-for-Buck Plugin
https://www.youtube.com/watch?v=1RSP5m52vPM

Niagara Collisions | Niagara [UE5]
https://www.youtube.com/watch?v=vVuHxl7w2bA

Vector Fields in Computer Graphicschrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://perso.liris.cnrs.fr/david.coeurjolly/teaching/ENS-M2-2020/VectorField-export-novideos.pdf

Vector Field Visualizationchrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://cgl.ethz.ch/teaching/former/scivis_07/Notes/stuff/StuttgartCourse/VIS-Modules-07-Vector_Field_Visualization.pdf

chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://cgl.ethz.ch/teaching/former/scivis_07/Notes/stuff/StuttgartCourse/VIS-Modules-07-Vector_Field_Visualization.pdf

Vector Field Visualization
https://vcg.iwr.uni-heidelberg.de/research/vectorvis/

Visualization of a Vector Field
https://medium.com/researchsummer/visualization-of-a-vector-field-9402615c780a

chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/http://15462.courses.cs.cmu.edu/fall2016content/lectures/03_vectorcalc/03_vectorcalc_slides.pdf

But How DO Fluid Simulations Work?
https://www.youtube.com/watch?v=qsYE1wMEMPA&t=47simulations

Real-time Eulerian fluid simulation on a Macbook Air, using GPU shaders
https://www.youtube.com/watch?v=x6mcua0HOJs

How to write an Eulerian fluid simulator with 200 lines of code.
https://www.youtube.com/watch?v=iKAVRgIrUOU

Coding Challenge #132: Fluid Simulation
https://www.youtube.com/watch?v=alhpH6ECFvQ

How to use Runtime Virtual Texturing (RVT) in Unreal Engine
https://www.youtube.com/watch?v=Ft2kzfxV7DU

Runtime Virtual Texture Research Notes
https://github.com/ibbles/LearningUnreal/blob/main/Runtime%20Virtual%20Texture%20Write%20From%20C%2B%2B.md

### 2024-10-17

现在有点不确定为什么要把fluid sim的结果写到一张纹理里面，然后用这张纹理来决定云的变动

我直接在fluid sim的结果上直接cloud rendering不就可以了，还剩下了读写纹理的步骤

比如说我直接在一个3d bounding box中利用3d worly noise生成一些density，然后用这个density来做模拟就可以了

但是对于超大scale云层的渲染，将渲染和流体模拟在一起算会不会太消耗性能了

但是这个时候我用一个小一点的cube来做模拟，然后将结果写入纹理，最后用这个low resolution的纹理来计算云体的变化，可行吗？
后续的优化可以考虑用runtime virtual texture来做对大scale云的模拟计算，这样那个小cube就只会更新能看的到的地方的流体模拟结果了

但是目前必须需要做的事情有什么？

- 搞清楚欧拉流体模拟
- 利用compute shader来加速方程求解

那这跟我在[ue5 inetraction plugin](https://www.youtube.com/watch?v=3VfhvULu2k4&t=17s)视频中看到的交互系统有什么关系？


