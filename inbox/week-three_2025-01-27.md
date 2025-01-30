---
tags:
    - master-thesis
create date: 2025-01-27
urls:
---

# Week Three

## Goals

- [x] goal doc
- [ ] [[#^micro-mesh-const]] paper
- [x] play around micromesh-tools
- [ ] direct x 12 ?
- [ ] micro mesh presentation videos

## 1.27

- [x] new hire form
- [x] nvidia micromesh-tools
- [>] goal doc

## 1.28

- [x] nvidia displacement micro-map toolkit
- [>] goal doc

### Misc

[nvpro_core](https://github.com/nvpro-samples/nvpro_core) doesn't not support `Vulkan SDK 1.4.0` or later, will casue **namespace vk has no member call dynamicloader**, have tested that `Vulakn SDK 1.3.261.1` work. 

3060ti doesn't have the vulkan extension for *micro mesh tools*:

```c
// in shader code
#extension: extension not supported: GL_NV_displacement_micromap
```

## 1.29

- [x] goal doc
- [>] find suitable framework to work on
- [x] organize the references
- [>] micro mesh presentation

## 1.30

- [x] micro-mesh basic (displacement compression left)
- [x] part of micro-mesh construction
- [>] falcor sample application code overview
- [x] DMM SDK tools
- [x] security trainings

### Misc

remove the compilation of `pathtrace.rchit` in cmakelists.txt file and some correspoding functions used in `toolbox_scene.cpp` will make [[#^DMMSDK]] work on gpu card before RTX 40s.

## 1.31


## Notes

[[micro-mesh_2025-01-29|micro-mesh]]

## References

- [Micromesh basic](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://developer.download.nvidia.com/ProGraphics/nvpro-samples/slides/Micro-Mesh_Basics.pdf) ^micro-mesh-basic
- [Micromesh construction](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://d1qx31qr3h6wln.cloudfront.net/publications/MicroMesh_generation.pdf) ^micro-mesh-const
- [Micromesh rasterization](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://developer.download.nvidia.com/ProGraphics/nvpro-samples/slides/Micro-Mesh_Rasterization.pdf) ^micro-mesh-rasterization
- [Micromesh tools github](https://github.com/NVlabs/micromesh-tools)
- [Displacement-microMap-toolkit github](https://github.com/NVIDIAGameWorks/Displacement-MicroMap-Toolkit) ^DMMSDK

