---
tags:
    - graphics
create date: 2024-10-18
urls:
    - [Learn opengl - compute shader](https://learnopengl.com/Guest-Articles/2022/Compute-Shaders/Introduction)
    - [Compute shader and mesh shader](https://www.youtube.com/watch?v=HH-9nfceXFw)
    - [OpenGL with C++: Compute shader](https://www.youtube.com/watch?v=sVps_gqlrqQ)
---

# Compute Shader

## Why we need a compute shader?

Graphics crads are also used for **General Purpose Computing on Graphics Processing Units**, shorts for **GPGPU-Programming**. 

Gpu is a **stream processor** which means the program that run on each unit must be independent, they don't share the memory, data etc.

All units will run exact the same code but with different input and generated different output based on the input **in parallel**. 

For example, I have a function that calculate the index based on the input:

```cpp
int index(int u, int v, int size) {
    return u + v * size;
}
```
So each process unit in GPU will run the same code but with different input

As I mentioned, it's hard or impossible for the communication amount the units, therefore accumulate all the result is not possible cause sharing the data or memory is impossible.

**Note**: you can do it in the host program, but not in GPU

## How does a compute shader work?

Compute shader has its own **operating data "space"** and you basically have 3 ways to fetch/read the data to/from compute shader:

- textures
- image loads
- shader storage block access? check [[#^ssbo]]

And a compute shader involve two important concepts:

- **Work groups**  

A Work group can be consider as a bunch of threads with thier work space and GPU hardward category its compute union into many work groups like

![nvidia-wrap.png](assets/imgs/nvidia-wrap.png)

**Note**: The modern gpu arch takes 32 threads(NVIDIA) or 64 threads(AMD) as an operator union, so it would be better for us to specified 32 or 64 threads in total in the compute shader code, take [[#^computeShaderExample]] as a references.

- **Invocations/Threads**

The actual place where execute the shader code

It's easier to explain these two concepts in one dimension first, and it might involve some tech about [[batches-rendering]].

// todo


There are some examples about how you use these methods to access the data:

`Using image`: 

- host program

```cpp
/// Create a image object by using texture
GLuint _ib;
glGenTextures(1, &_ib);
glActiveTexture(GL_TEXTURE0);      // you can bind any texture slot you want
glBindTexture(GL_TEXTURE_2D, _ib); 
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);

/**
* @brief 
* @parameter
*/
glTexImage2D()

/**
* @brief 
* @parameter
*/
glBindImageTexture();
```

- shader code ^computeShaderExample

```cpp
#version 430

/**
* @brief Specify the work group size
* @parameter local_size_x thread number in x dimension
* @parameter local_size_y thread number in y dimension
* @parameter local_size_z thread number in z dimension
*/
layout(local_size_x = 4, local_size_y = 4, local_size_z = 4) in;

/**
* @brief Specify how compute shader access the data with the images
* @parameter rgb32f Image data format
* @parameter binding Bind to the images slot
* @varName gimage2D is a general name for 3 diff types: image2D(float), iimage2D(int) and uimage2D(uint)
*/
layout(rgb32f, binding = 0) uniform gimage2D _imageName;

/// Step 3
void main() {
    /// Functions that read/write to images
    /**
    * @brief read data from image
    * @parameter img image type from image2D, iimage2D and uimage2D
    * @parameter coord integer pixel coord
    */
    gvec4 imageLoad( gimage img, image_coord coord )

    /**
    * @brief write data to image
    * @parameter img image type from image2D, iimage2D and uimage2D
    * @parameter coord integer pixel coord
    */
    void imageStore( gimage img, image_coord coord, value val )
}
```

`Using texture`: 

- host program

```cpp
/// Create a texture
GLuint _texture;
glGenTextures(1, &_texture);
glActiveTexture(GL_TEXTURE0); // you can bind any texture slot you want
glBindTexture(GL_TEXTURE_2D, _texture); 
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);

/**
* @brief 
* @parameter
*/
glTexImage2D()

/**
* @brief Generate mipmap for the texture
* @parameter Specify a texture type
*/
glGenerateMipmap(GL_TEXTURE_2D);

```

- shader code

```cpp
#version 430

/**
* @brief Specify the work group size
* @parameter local_size_x thread number in x dimension
* @parameter local_size_y thread number in y dimension
* @parameter local_size_z thread number in z dimension
*/
layout(local_size_x = 4, local_size_y = 4, local_size_z = 4) in;

/**
* @brief Specify how compute shader access the data with the images
* @parameter binding Bind to the images slot
*/
layout(binding = 0) uniform sampler2D _textureName;


/// Step 3
void main() {
    // sample the data at position (0.5, 0.5) from the texture
    vec4 texel = texture(_textureName, vec2(0.5, 0.5));
}
```

`Using shader storage buffer object`: 

- host program

```cpp
// declare your custom data, for example a array
int data[size];

GLuint ssbo;
glGenBuffers(1, &ssbo);
glBindBuffer(GL_SHADER_STORAGE_BUFFER, ssbo);
glBufferData(
    GL_SHADER_STORAGE_BUFFER,
    sizeof(data),
    data,
    GL_STATIC_READ  // read/write
);

/**
* @brief 
* @parameter buffer type
* @parameter slot you specify in the shader code with binding keyword
* @parameter shader storage buffer object id
*/
glBindBufferBase(GL_SHADER_STORAGE_BUFFER, 0, ssbo);
```

- shader code

```cpp
#version 430

/**
* @brief Specify the work group size
* @parameter local_size_x thread number in x dimension
* @parameter local_size_y thread number in y dimension
* @parameter local_size_z thread number in z dimension
*/
layout(local_size_x = 4, local_size_y = 4, local_size_z = 4) in;

/**
* @brief Specify how compute shader access the data with the ssbo
* @parameter std430 Standardized memory layout format
* @parameter binding Bind to the buffer slot which specified in host program with glBindBufferBase()
*/
layout(std430, binding = 0) buffer _bufferNameIn {
    // buffer data, for example
    int data[];
} _bufferNameOut;

void main() {
    // functions that read/write to ssbo
    _bufferNameOut.data[index] = ...
}
```

### In the rendering loop

There are some steps you need to do to make compute shader work

```cpp
while( isRendering ) {
    /**
    * @brief use the compute shader program
    * @parameter the program id
    */
    glUseProgram(computeShader);

    /**
    * @brief 
    * @parameter
    * @parameter
    * @parameter
    */
    glDispatchCompute();

    /**
    * @brief Make sure the data can be accessed after the compute shader finish all the tasks
    */
    glMemoryBarrier(GL_SHADER_IMAGE_ACCESS_BARRIER_BIT);
}
```

## A brand new *"rendering" pipeline*

As we don't actually rendering anything when we try to use compute shader, the traditional rendering pipeline could be simplified a little bit, like

![compute-shader-pipeline.png](assets/imgs/compute-shader-pipeline.png)


## Extension - [[Mesh-shader]]


## FAQ & Troubleshooting

*1. Compute shader require `OpenGL 4.3+`, note that Apple **does not** support compute shader in Opengl.*

*2. Why not use other GPGPU-Programming libs, like [[OpenCL]] or [[CUDA]]?*

- compute shader can work with other opengl functions
- avoid complicated interfacing

*3. Large work groups size or large work groups count?*

Better to make the work groups size math the size of the thread count of the graphcis card.

*4. Faster when using textures or images or shader storage block access?*

images load doesn't involve any filtering tech 

while texture does

*5. Diff between fragment shader and compute shader?*

Fragment shader has specific input and output while the input/output of a compute shader can be anything.

**Note** that compute shader != fragment shader to some extent

*6. When we use a read_write image, how can we avoid the parallel conflict?*

By using atomic operations, check [OpenGL 4.5 References](https://registry.khronos.org/OpenGL-Refpages/gl4/) for more info

*7. Diff between using image and texture to access the data in compute shader* 

- Texture is read only while you can read/write to a image
- Image doesn't have mipmap but texture does

## Glossary

- Shader storage block ^ssbo

In opengl, it has a concept about `shader storage buffer object` which is used to store large-scale data, you can write from and write to it, usefule in fliud sim, particle sys etc.
