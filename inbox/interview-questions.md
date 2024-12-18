---
tags:
    - interviews
create date: 2024-12-17
urls:
    - [游戏和图形学面试问题总结](https://zhuanlan.zhihu.com/p/575930904)
---

# Interview Questions

1. What's rendering pipeline?

- Traditional Pipeline
- Modern Pipeline
- [[compute-shader#a-brand-new-rendering-pipeline]]/[[Mesh-shader#basic]] based pipeline

2. Normal map and tangent space

3. Phong and Blinn-Phong

4. Baching rendering tech

## Project Questions

- `Parallax Voxel Renderer`

1. What's USDF, why not SDF?

How far is a point to the shape we want,

We want voxel inside.

2. How you determine a ray interact with a bounding box?

3. How you did parallax mapping in the project?

对于一个quad的每个像素点来说，我们发射一条射线，当这个射线与bounding box相交的时候，开始做一个固定step的遍历，用当前的点来采样3d纹理，如果为空则继续往前走直到超过最大的steps，如果碰到不为空，那么当前的像素就返回纹理中的值。

我们用一个quad的uv加上camera的viewdir来做来射线的方向

```cpp
for i < max_steps:
    vec3 p = vec3(uv, 0) + timeStep * ViewDir;

    if(!insideAABB(P)) discard

    int mat = int(texture(volume, p).r * 255)

    if(mat != 0) return mat

    timeStep += 0.1 * voxel_size; // fix steps

discard;
```

4. why you rendering to the backface of the cube?

In order to be move around and into the volume, because if it is rendered in the front face, we will not see anything when we get into the volume.

5. How did you get the properties of the voxel?

6. Optimization with the 3d cell auto?

We sent color index instead of actual color to the texture

7. How different trunks connect to each other

8. How did you genereate the perline noise and vorono noise

9. Explain Fractal Brownian Motion

布朗运动（BM），如果没有“分数”部分，是一种物体位置随时间变化的随机运动（可以想象为一系列“位置 += 白噪声()”）。从形式上讲，布朗运动是白噪声的积分。这些运动定义了随机的路径，但在统计上是自相似的，即放大后的路径与整个路径相似。

分数布朗运动（fBM）是一个类似的过程，其中增量之间并不是完全独立的，而是存在某种形式的记忆。如果记忆是正相关的，那么在某个方向上的变化会倾向于在未来产生相同方向的变化，路径将比普通布朗运动更加平滑。如果记忆是负相关的，那么正向变化后最可能跟随负向变化，路径会显得更加随机。

控制记忆行为或积分方式，从而控制自相似性、分形维数和功率谱的参数被称为赫斯特指数（Hurst Exponent），通常用H表示。从数学上讲，H允许我们只部分地对白噪声进行积分（例如，进行1/3的积分，因此名字中的“分数”部分），以设计具有任何我们想要的记忆特性和视觉效果的分数布朗运动。实际上，H的取值范围在0到1之间，分别描述粗糙和平滑的fBM，其中普通的布朗运动发生在H=1/2时

10. LOD?

We simply change the voxel size depending on the how many steps I take.

11. How to generate perlin noise?

12. Why choose this traversal algo?

Fixed steps may miss some voxel, low performance because of the very small steps in order to get accurance.


- `Eularin Fluid Simulation`
