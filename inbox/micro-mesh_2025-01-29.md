---
tags:
    - computer-graphics
create date: 2025-01-29
urls:
---

# Micro mesh

K-level subdivision means:

- 2^k segements
- 4^k micro-triangles
- (2^k + 1)(2^(k-1) + 1) micro-vertex

`micro-map` store the scalar value of the displacement per micro-vretex, it's like **Cem Yuksel's mesh color work**

important property is the displaced micro-mesh is bounded by the hull formed from the base mesh vertices and displacement vector, for better culling.

one way to solve visual discontinuity of LODs is to linearyly blendeing triangle into remove/exsitance 

Adaptive tesselation on individual micro meshes

RT cores can resolve the ray-triangle intersection without invoking any shader

DMM SDK come with a DMM toolbox, but 3060ti gpu doesn't have the corresponding vulkan extension, but I can run the `dmm_displacement` in the sample folder.

**The primary value** of micro-mesh is extreme compactness in VRAM which make high-quality geometry possible for efficiency ray traced or rasterized rendering.


## Challenges 

- Dynamic lod selection will cause lod cracks and violate the rule of `subdivision levels must differ by only +- 1 along edges` 

## Questions

1. Unlimited subdivision cause high deep tree of BVH and make it slow to traversal? 

Size of the bvh is critical in hardware 

to avoid cracks, subdivision levels must differ by only +- 1 along edges

2. Why micro mesh models don't need to recaulcate the displacement mapping when animating the model?

3. How to get displacement info from a high-res mesh to a base mesh?

check [[#^micromeshpresentation]] at 29:30

4. why not use vertex normals instead of displace vector?

Because it will crack if the vertices shader the same sharp edges

check [[#^micromeshpresentation]] at 30:30

5. To deal with the texture and uv mapping, check [[#^micromeshpresentation]] at 32:30

6. The topology of the model out from common dcc tools are not every good, it will cause problem in tessellation when the size of each triangle has a huge difference, some are over tessellated and some are under tessellated.


## Unfamiliar terminology

- FP 16 Mantissa

- Unorm 11

- Watertightness

- Alpha texture

- BLAS

- TLAS

## References

[Getting started with compressed micro-meshes](https://www.nvidia.com/en-us/on-demand/session/gtcspring23-s51410/) ^micromeshpresentation
