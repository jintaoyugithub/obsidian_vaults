---
tags:
    - codeTest
create date: 2024-12-03
urls:
    - [leetcode link](https://leetcode.cn/problems/reverse-string/description/)
---

# reverse-string

## Solutions

### Mine

```cpp
class Solution {
public:
  void reverseString(vector<char> &s) {
    if(s.size()<1) return;

    int slowIndex = 0;
    int fastIndex = s.size() - 1;

    // 如果使用！=的话会导致slow > fast的时候还在循环
    while (slowIndex < fastIndex) {
      char temp = s[slowIndex];
      s[slowIndex] = s[fastIndex];
      s[fastIndex] = temp;

      slowIndex++;
      fastIndex--;
    }
  }
};
```
- **State** 

`Pass?`: Yes

`Performance`: Not bad
