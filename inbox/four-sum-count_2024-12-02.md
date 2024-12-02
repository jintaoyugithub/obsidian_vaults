---
tags:
    - codeTest
create date: 2024-12-02
urls:
    - [leetcode link](https://leetcode.cn/problems/4sum-ii/description/)
---

# Four sum count

## Tips

除了要学会灵活运用不同的哈希数据结构以外，比如map，set，还要搞清楚什么情况下multi和single可以转换，比如这道题中，问的是让四个数只和的下标组合的个数，这种只问个数的，我们可以用map<int, int>一个存储key value，一个存储这个key value出现的次数取代使用multimap<int, int>一个存储key value，一个存储下标，但是如果需要我们返回下标的话，就需要用multimap了。

## Solutions

### Mine 

```cpp
class Solution {
public:
  int fourSumCount(vector<int> &nums1, vector<int> &nums2, vector<int> &nums3,
                   vector<int> &nums4) {
    // 这道题和前面一道两数只和的解法差不多，都是用空间换时间
    // 用两个循环来算nums1和nums2的和s1
    // 然后用s1来找在nums3和nums4中有没有可以抵消的
    // 比如说找nums4中有没有(-s1 + nums3)的值
    unordered_multimap<int, int> numsSum;

    int i = 0;
    for (int a : nums1) {
      for (int b : nums2) {
        // store the sum of nums1 and nums2
        numsSum.insert({a + b, i});
      }
    }

    int count = 0;
    for (int i = 0; i < nums1.size(); i++) {
      for (int j = 0; j < nums1.size(); j++) {
        if (numsSum.find(-(nums3[i] + nums4[j])) != numsSum.end()) {
          count++; // wrong, will only take into account once even there are two combinations in the map
        }
      }
    }

    return count;
  }
};
```
- **States** 

`Pass?`: No

`Reasons`: count的计算不对，如果是按照代码中的这么计算，如果有两种组合，但是代码中的只会算一种

