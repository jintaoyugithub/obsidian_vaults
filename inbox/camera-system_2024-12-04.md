---
tags:
    - graphics
create date: 2024-12-04
urls:
---

# Camera System

Actually camera doesn't exist when we talk about rendering api like OpenGL, it just a concept that make us easier to understand how these api capture a the scene.

There are few important concept in a camera system:

- Focal length
- Field of view
- Aspect Ratio

If you want to implement a **physical based camera**, there are more you need to pay attention to, like apeture, depth of view etc.

However, differ from the actual camera in the real world, in 3d application, you have to think the progress in a oppsite way.

For example, think about how final image we get update? 

If we wanna see the top face of a cube, we drag the "Camera" up a little bit, but like I said we don't have a thing call "Camera" in graphics api, so we need to think the transformation in a oppsite way, **It's not camera move upward, it's the cube move downward**, we can apply the oppsite transform of the camera to the objects in the entire scene to achieve the same result.

The **Camera Effect** can be divided into two parts

- View matrix 

Which store the `position` and the `orientation` of the camera, so we can **invert** the matrix and apply it to the reset of the objects in the scene

- Projection matrix

Which store the `FOV` and the `Aspect Ration` 

## Tips

It's better to pass the whole `MVP` matrix instead of pass model, view, projection matrix separately:

```cpp
uniform mat4 mvp;

gl_Position = mvp * position;

// instead of 
uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

gl_Position = projection * view * model * position;
```

Because one is per object, one is per vertex!!

