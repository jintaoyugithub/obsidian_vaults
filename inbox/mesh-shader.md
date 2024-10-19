---
tags:
    - graphics
create date: 2024-10-19
urls:
    - [Introduction to Turing Mesh shader](https://developer.nvidia.com/blog/introduction-turing-mesh-shaders/)
    - [Mesh shader](https://reecocho.github.io/2024/08/19/mesh-shaders/)
    - [Compute shader and mesh shader](https://www.youtube.com/watch?v=HH-9nfceXFw)
---

# Mesh-shader

## Basic

Traditional rendering pipeline which is *rasterization based* actually doesn't fit modern gpu arch so well

To some extent, `compute shader` leverage the gpu power better

**Mesh shader** wants to make the rendering pipeline match the gpu arch, to turn the pipeline from

![traditional-rendering-piple.png](assets/imgs/traditional-rendering-piple.png)

to

![mesh-shader-based-rendering-pipeline.png](assets/imgs/mesh-shader-based-rendering-pipeline.png)


**Note**: you can take mesh shader as a **special compute shader that output primitives** 


### Meshlets

## FAQ & Troubleshooting

1. Traditional rendering pipeline solve the bottleneck with sending only a few vertices to the gpu and let gpu tessellated the vertices at runtime, but mesh shader require massive data from the beginning 
