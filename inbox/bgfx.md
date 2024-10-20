---
tags:
    - graphics
create date: 2024-10-20
urls:
---

# bgfx

## Basic

### Buffer

In `bgfx`, there are 

- `Vertex buffer` 

1. Static

>Used when the data is sent to the gpu at one time and barely changed

[API: create a static vertex buffer](https://bkaradzic.github.io/bgfx/bgfx.html#_CPPv4N4bgfx18createVertexBufferEPK6MemoryRK12VertexLayout8uint16_t)

2. Dynamic

>Used when you have to update the data frequently, for example every frame

[API: create a empty dynamic vertex buffer](https://bkaradzic.github.io/bgfx/bgfx.html#_CPPv4N4bgfx25createDynamicVertexBufferE8uint32_tRK12VertexLayout8uint16_t)
[API: create a dynamic vertex buffer and init](https://bkaradzic.github.io/bgfx/bgfx.html#_CPPv4N4bgfx25createDynamicVertexBufferEPK6MemoryRK12VertexLayout8uint16_t)

- `Index buffer` 

1. Static 

[API: create a static index buffer](https://bkaradzic.github.io/bgfx/bgfx.html#_CPPv4N4bgfx17createIndexBufferEPK6Memory8uint16_t)

2. Dynamic

[API: create a dynamic index buffer](https://bkaradzic.github.io/bgfx/bgfx.html#_CPPv4N4bgfx24createDynamicIndexBufferE8uint32_t8uint16_t)
[API: create a dynamic index buffer and init](https://bkaradzic.github.io/bgfx/bgfx.html#_CPPv4N4bgfx24createDynamicIndexBufferEPK6Memory8uint16_t)

- `Instance data buffer`


- `Uniform buffer` 


### Texture

### Shaders

#### Compute Shader

