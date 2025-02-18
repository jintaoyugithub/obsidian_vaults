---
tags:
    - master-thesis
create date: 2025-01-16
urls:
    - [Input assembler stage](https://learn.microsoft.com/en-us/windows/uwp/graphics-concepts/input-assembler-stage--ia-)
    - [Mesh optimizer](https://github.com/zeux/meshoptimizer)
    - [Turing arch - from gpu-driven to mesh shader](https://zhuanlan.zhihu.com/p/514840683)
---

# Mesh shader

- Traditional pipeline

1. mesh represent by vertices stored in **vertex buffer** 

2. use **index buffer** to reduce data duplication

3. input assembler stage read, assemble the data and pass to the rest stages in the pipeline

>say this vertex(vertex id) should belong to this primitive(primitive id)

if this data is for like `geometry shader`, why we assemble the primitives this early, we can wait actually! `Vertex shader` is based on vertices not primitives.

4. vertex shader -> tessellation -> geometry shader

mesh data is processed in the gpu as vertices, batches or primitives, we don't have the access to the whole mesh.

not be able to subtract the geometry

- Mesh shader pipeline

You can take mesh shader pipeline with `compute shader with hardware rasterazation`

in traditional pipeline, each vertex will have one thread to process it, one thread output one vertex, but in mesh shader pipeline, think processing as a group way, i.e. one thread group output a primitive or bunch of vertices

**what's the differenct with batch rendering?**



mesh shader pipeline require additional stage to split mesh into meshlets.


Process the vertex first and then assemble the processed vertices while the rest are still on operating

**But** how this improve the vertex reuse?

In the traditional pipeline, a vertex might invoke vertex shader multiple time because there is no thing like a marker to mark this vertex has been processed. In mesh shader, it will split the mesh into different meshlet (including new indices buffer which only store the connectivity within that specific meshlet), and it will try to make sure that each vertex will only exist in one meshlet.

both mesh shader pipeline and [[gpu-driven-pipeline_2025-01-16|gpu-driven-pipeline]] are trying to effectively rerdering massive mesh data, one is to process batch of vertices in parallel to reuse the vertex data as much as possible, one is to avoid too many draw calls by utilising the indirectdraw and optimize culling.

**Note**: 

- each vs only work on one vertex

## Unfamiliar terminology

- Vertex cache optimization


