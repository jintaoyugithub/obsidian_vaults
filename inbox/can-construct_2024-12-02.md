---
tags:
    - codeTest
create date: 2024-12-02
urls:
    - [leetcode link](https://leetcode.cn/problems/ransom-note/description/)
---

# Can construct

## Solutions

### Mine

```cpp
class Solution {
public:
  bool canConstruct(string ransomNote, string magazine) {
    unordered_multiset<char> mRansomNote(ransomNote.begin(), ransomNote.end());
    unordered_multiset<char> mMagazine(magazine.begin(), magazine.end());

    for (auto itr = mRansomNote.begin(); itr != mRansomNote.end(); itr++) {
      if (mMagazine.find(*itr) == mMagazine.end()) {
        return false;
      }
      // mMagazine.erase(*itr); wrong: this will erase all the elements which
      // equal to *itr

      auto found =
          mMagazine.find(*itr); // find the first element which match the value
      mMagazine.erase(found);   // erase the element from specific position
    }

    return true;
  }
};
```

- **States**

`Pass?`: Yes

`Performance`: very bad, it can be optimized with `array` of `unordered map` instead of `unordered multiset`, for example you can use an 26 array to record how many time each letter appear, or you can use map to store how many times correspoinding letter appears.

![can-construct performance.png](assets/imgs/can-construct-performance.png)
