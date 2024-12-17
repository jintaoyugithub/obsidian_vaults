---
tags:
    - graphics
create date: 2024-12-03
urls:
    - [Interactive Computer Graphics - Volume Rendering](https://www.youtube.com/watch?v=y4KdxaMC69w)
---

# volume-rendering

Definition: think volume as a bunch of 2d contious images stack on each others

There are several ways to rendering volumetric data

1. 3D texture with slices rendering(Ray marching)

**Note**:

- The order of the slices because of the alpha blending
- Sampling steps may differ from different view dir

should have imgs here!

- Can be optimized aligning the slices dir with the camera dir, but have to consifer the shape of the slices in the bounding box

should have imgs here!


## Transfer Functions (TFs)

`Definition`: Map data value to color and opacity, it's application independnt!
