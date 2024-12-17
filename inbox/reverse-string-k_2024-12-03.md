---
tags:
    - codeTest
create date: 2024-12-03
urls:
    - [leetcode link](https://leetcode.cn/problems/reverse-string-ii/description/)
---

# reverse-string-k

## Solutsion

### Mine

- First try ^1stTry

```cpp
class Solution {
public:
  string reverseStr(string s, int k) {
    string result;
    int itr = s.size() / (2 * k);

    // itr = 0?
    for (int i = 0; i < itr + 1; i++) {
      int strLen = s.size() - (itr * 2 * k);

      if (strLen < k) {
        // reverse all
        for (int fastIndex = s.size() - 1; fastIndex >= 0; fastIndex--) {
          result.push_back(s[fastIndex]);
        }
      } else if (strLen < 2 * k && strLen >= k) {
        // reverse previous k
        for (int fastIndex = s.size() - k - 1; fastIndex >= 0; fastIndex--) {
          result.push_back(s[fastIndex]);
        }
      } else {
        // reverse previous k
        for (int fastIndex = 2 * k - 1; fastIndex >= 0; fastIndex--) {
          result.push_back(s[fastIndex]);
        }
        // and cut the string
        s = s.substr(2 * k - 1, s.size() - 1);
      }
    }

    return result;
  }
};
```

- Second try ^2ndTry

```cpp
class Solution {
public:
  string reverseStr(string s, int k) {
    for (int i = 0; i < s.size(); i += (2 * k)) {
      // deal with two special situations
      if (s.size() - i < k) {
        // reverse the reset
        reverse(s.begin() + i, s.end());
      } else if (s.size() - i < (2 * k) && s.size() - i >= k) {
        reverse(s.begin() + i, s.begin() + i + k);
      } else {
        reverse(s.begin() + i, s.begin() + i + k);
      }
    }

    return s;
  }
};
```

#### Solutions analysis

| Attempts     | Reasoning | Pass? | Reasons                                   | Runtime cost | Memory cost |
|--------------|-----------|-------|-------------------------------------------|--------------|-------------|
| [[#^1stTry]] | N/A       | No    | dont know how to use loop stride flexibly | N/A          | N/A         |
| [[#^2ndTry]] | N/A       | Yes   | more clear when use loop stride           |              | Bad         |
