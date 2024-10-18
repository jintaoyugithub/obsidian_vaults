---
tags: 
    - cmake
create date: 2024-09-30
---

# CMake FAQ and Troubleshooting

## Overview

| ID         | Descriptions |
|------------|--------------|
| [[#^test]] | sdf          |


## Issues

1. Successfully compiled but cannot find the executable file ^test

That is maybe you don't specify the output dir so that the system take the output dir of some of your submodules by default, for example llgl.

In that case, you can explicit declare the output dir by

```cmake
set_target_properties(target PROPERTIES RUNTIME_OUTPUT_DIRECTORY /path/to/output)
```

**Tips**: check the printed info of compilation, it will show where is the executable file

2. 
