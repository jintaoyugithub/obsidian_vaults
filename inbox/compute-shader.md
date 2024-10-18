---
tags:
    - graphics
create date: 2024-10-18
urls:
    - [learn opengl - compute shader](https://learnopengl.com/Guest-Articles/2022/Compute-Shaders/Introduction)
---

# Compute Shader

## Basic

1. Why we need a compute shader?

Graphics crads are also used for **General Purpose Computing on Graphics Processing Units**, shorts for **GPGPU-Programming**. 

Gpu is a **stream processor** which means the program that run on each unit must be independent, they don't share the memory, data etc.

All units will run exact the same code but with different input and generated different output based on the input **in parallel**. 

For example, I have a function that calculate the index based on the input:

```cpp
int index(int u, int v, int size) {
    return u + v * size;
}
```
So each process unit in GPU will run the same code but with different input

As I mentioned, it's hard or impossible for the communication amount the units, therefore accumulate all the result is not possible cause sharing the data or memory is impossible.

**Note**: you can do it in the host program, but not in GPU

2. How does a compute shader work?

Compute shader has its **own operating data "space"** and you basically have 3 ways to fetch/read the data to/from compute shader:

- textures
- image loads
- shader storage block access? check [[#^ssbo]]

there are some examples about how you use these methods to access the data:

```cpp

```
<++>

There are a few very improtant concepts in compute shader:

- **Work groups** 
- **Invocations** 

It's easier to explain these two concepts in one dimention first, and it might involve some tech about [[batches-rendering]].


3. A brand new *"rendering" pipeline*

As we don't actually rendering anything when we try to use compute shader, the traditional rendering pipeline could be simplified a little bit, like

![compute-shader-pipeline.png](assets/imgs/compute-shader-pipeline.png)


## FAQ & Troubleshooting

1. Compute shader require `OpenGL 4.3+`, note that Apple **does not** support compute shader in Opengl.

2. Why not use other GPGPU-Programming libs, like [[OpenCL]] or [[CUDA]]?

- compute shader can work with other opengl functions
- avoid complicated interfacing

3. Large work groups size or large work groups count?

Better to make the work groups size math the size of the thread count of the graphcis card.

4. Faster when using textures or images or shader storage block access?

images load doesn't involve any filtering tech 

while texture does

5. Diff between fragment shader and compute shader?

**Note** that compute shader != fragment shader to some extent

6. When we use a read_write image, how can we avoid the parallel conflict?

## Glossary

- Shader storage block ^ssbo

In opengl, it has a concept about `shader storage buffer object` which is used to store large-scale data, you can write from and write to it, usefule in fliud sim, particle sys etc.
