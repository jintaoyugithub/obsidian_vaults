---
tags:
    - computer-graphics
create date: 2025-01-21
urls:
    - [The Cherno - Batch Rendering Introduction](https://www.youtube.com/watch?v=Th4huqR77rI&list=PLlrATfBNZ98f5vZ8nJ6UengEkZUMC4fy5&index=1)
---
 
# Batches Rendering

Why?

for example, rendering thousands of tiles in a 2D games will require thousands of draw calls

particle system which is based on quad? why not use `instancing`.

or rendering text

But we do have #batch-rendering-challenge here, for example, we have two quads and they are in the different position in the word, we can access their model position from the vertex buffer because we store the position of this two quad in the same vertex buffer, but if the quads are constantly moving? We need `dynamic vertex buffer`!


## Questions

1. Batch rendering vs. Instancing

2. does [[note-nanite-presentation_2025-01-14]] use batch rendering in the nanite mesh pipeline? so they can rendering all the meshlet at one single draw call.
