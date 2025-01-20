---
tags:
    - master-thesis
create date: 2025-01-17
urls:
    - [Introducing NVIDIA RTX Kit: Transforming Rendering with AI and Path Tracing](https://www.youtube.com/watch?v=5PHBXY0FI5o)
    - [RTX Mega Geometry Is A Big Deal... But What Does It Actually Do?](https://www.youtube.com/watch?v=5KRxyvdjpVU)
    - [RTX Mega Geometry Is Massively Underappreciated : r/hardware](https://www.reddit.com/r/hardware/comments/1hx9hqu/rtx_mega_geometry_is_massively_underappreciated/)
---

# RTX Mega Geometry

Try to solve:

1. ray tracing on dynamic/moving geometry such as character 

2. acceleration structure (BVH) rebuild because of the dynamic lod load 

3. full rebuild of all the acceleration structure of nanite mesh, because every frame there might be hundreads of changes of lod

A streaming scheme that quickly stream in and out while does not have to rebuild the acceleration structure

tessellated with displacement map?

one triangle per pixel ration will make massive unparallel lods

they don't need a alpha cutout when you get very closer, the subdivision just happen so quickly.

**But** this tech seems to reduce the rebuild cost when lod changes, what to do with the tessellation

## Questions

1. Why rebuild when the details goes up?

the increase of the number of triangles might change the shape of the mesh, then we need to update/rebuild the acceleration structure.

2. if this tech can be work with nanite, will this be already high fidility models with meshlet level tessellation?

possible problem: 

1. if we want to tessellated the mesh with lod0, it will change the share edge of neighbouring clusters

## Unfamiliar terminology

- fallback mesh

- trace the primary rays (for example Quake 2 RTX)

- alpha cutout
