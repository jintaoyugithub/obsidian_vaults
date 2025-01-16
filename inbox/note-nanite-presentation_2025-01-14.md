---
tags:
    - master-thesis
create date: 2025-01-14
urls:
---

# Note on nanite presentation

Why?

Try to reduce the budets come from the `polycounts`, `draw calls` and `memory` so that the engine can directly import the **film quality source art**.

Challenges:

1. complexity of the geometry directly impact the rendering cost
2. hard to filter geometry compare to texture, texture can be divided into different cells but geometry can't

Other options?

1. Voxels & implcit surfaces

- Pros.
    - easier to filter and grouped
- Cons.
    - uniform resampling make the result looks blooby
    - massive data amount in order to get detailed models
    - hard to represent geometry with hard edges
    - how voxels work with UVs?

2. Adaptive tessellation and simplification

- Pros.
    - infinity details/simplification
    - dynamic level of details? Voxel can also achieved that
- Cons.
    - won't reduce the memory pressure cause it still load the whole geometry

3. Points

- Pros.
- Cons.
    - massive overdraw
    - hard to determine if the hole need to be filled or not
    - work with UVs?


## Unfamiliar terminology

- Uniform resampling

Tech used in convention from poly to voxels, is that means every quad will be replace by the voxel with a uniform size?

- Hard surface modeling & organic surface modeling

Check [What's hard surface modeling](https://blog.wingfox.com/what-is-hard-surface-modeling/)
- Video random-access memory (VRAM)
