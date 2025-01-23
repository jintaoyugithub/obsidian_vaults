---
tags:
    - master-thesis
create date: 2025-01-21
urls:
---

# Hardware Tessellation

**3 main stages**:

- [[#Tessellation control shader]]
- [[#Tessellation primitive genreator]]
- [[#Tessellation evaluation shader]]

Based on the [[#^blog1211]] we can see the drawbacks of the `post transform cache` in modern GPU.


## Tessellation control shader

>Determine how many tessellation we want to do

## Tessellation primitive genreator

>Actual generate tessellated points based on the input from the TCS

## Tessellation evaluation shader

>Generate the vertex value based on the tessellated points from the genreator

## References

### Blogs

- [Vertex cache drawbacks on modern gpu](https://interplayoflight.wordpress.com/2021/11/14/shaded-vertex-reuse-on-modern-gpus/) ^blog1211
- [Post transform cache](https://www.khronos.org/opengl/wiki/Post_Transform_Cache)

- [Indexed rendering](https://www.khronos.org/opengl/wiki/Vertex_Specification#Theory)

- [Khronos tessellation](https://www.khronos.org/opengl/wiki/tessellation)
