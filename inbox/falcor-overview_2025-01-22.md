---
tags:
    - computer-graphics
create date: 2025-01-22
urls:
---

# Falcor Overview

Falcor is a real-time rendering framework developed by Nvidia based on the [[render-graph_2025-01-21]] tech which is introduced by Frostbite team in [2017 GDC](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://ubm-twvideo01.s3.amazonaws.com/o1/vault/gdc2017/Presentations/ODonnell_Yuriy_FrameGraph.pdf), check 
[[falcor-code-review_2025-01-22]] for more technical details

**Note**: 

1. pay attention to the tools in the `tools` folder, falcor provides several useful tools, for example command line tool for quickly create `render pass`, `sample application`.

2. falcor 5.2 or later remove mose of 

There are 3 main parts that users will use:

1. [[#Render pass]]
2. [[#Render graph]]
3. [[#Scene/Shader]]

## Render pass

## Render graph

## Scene/Shader

## Examples

1. Falcor with mesh shader

may be I can split `Meshlet Viewer Example`in [DirectX 12 mesh shader example](https://github.com/microsoft/DirectX-Graphics-Samples/tree/master/Samples/Desktop/D3D12MeshShaders) into different render pass and reproduce it in the Falcor.



## Tips

1. On windows, **build the whole solution** with Visual Studio, directly open the **executable file** in the build folder of, for example, `RenderGraphEditor` otherwise visual studio will keep reporting `debug_breakpoint`

