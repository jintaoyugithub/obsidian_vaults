---
tags: 
    - utils
create date: 2024-10-03
urls: [
    - [Regular Explanation in 55 mins](https://zhuanlan.zhihu.com/p/91689180)
    - [Pratice website](https://regex101.com/)
]
---

# Regular explanation

**Notes**:

- Upper/Lower case matters if there is no special notes

## Basic

### Special characters

1. Meta characters

元字符主要是在正则表达式中的一些特殊字符

| Characters | Descriptions                 | Examples                                                    |
|------------|------------------------------|-------------------------------------------------------------|
| .          | 匹配任意单一字符，除了换行符 | a.c就表示匹配前后是ac中间是任意字符的单词，比如cat，cbt等等 |
| *          | 匹配前面的字符0次或多次      | ab*c就会匹配ac, abc, abbc, abbbbc以此类推                   |
| +          | 匹配前面的字符1次或多次      | ab+的例子就是去掉上面的ac                                   |
| ?          | 匹配前面的字符0次或1次       | abc?会匹配abc或ab                                           |
| ^          | 匹配行首                     |                                                             |
| $          | 匹配行尾                     |                                                             |

2. Escape characters

转义字符本质上就是利用反斜杠`\`来组成的一系列匹配模式

**Notes**: 如果想要表示上面元字符的字面上的意思就可以用到转义字符来实现，比如说：

- `/.`: 表示.而不是表示匹配任意单一字符
- `/*`:
- `/+`:

| Characters | Descriptions                             | Examples                                                    |
|------------|------------------------------------------|-------------------------------------------------------------|
| \          | 转义字符，使特殊字符表示原本字面上的意思 | \.就表示.而不是匹配任意单一字符                             |

3. Character classes

Character classes are defined with `[]`, it means math any one of them

For examples:

- `[abc]`: means match `a` or `b` or `c`.
- `[^abc]`: means match  `b` or `c` or any character which is `not a`.

**Notes**: 在字符类中和字符类外的规则可能会有些许的不同，比如

- `[.]`: 就表示匹配一个全角句号，并不是我们前面说的匹配任意单一字符

4. Quantifiers

5. Operators

- []

- ()

- {}


## References

