---
tags:
    - codeTest
create date: 2024-11-24
urls:
    -[leetcode link](https://leetcode.cn/problems/intersection-of-two-arrays/)
---

# Find Intersection

## Solutsion

### Mine

- First try

```cpp
class Solution {
public:
  vector<int> intersection(vector<int> &nums1, vector<int> &nums2) {
    unordered_set<int> temp;
    unordered_set<int> intersection;

    for (int i = 0; i < nums1.size(); i++) {
      temp.insert(nums1[i]);
    }

    for (int i = 0; i < nums2.size(); i++) {
      auto j = temp.find(nums2[i]);

      if (j != end(temp)) {
        intersection.insert(nums2[i]);
      }
    }

    // dont know how to transfer set to vector
    return vector<int>(intersection.begin(), intersection.end());
  }
};
```

- **States**

`Pass?`: Yes

`Problems`: Dont know how to construct vector from unordered_set

### Standard Solution

```cpp
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> result_set; // 存放结果，之所以用set是为了给结果集去重
        unordered_set<int> nums_set(nums1.begin(), nums1.end());

        for (int num : nums2) {
            // 发现nums2的元素 在nums_set里又出现过
            if (nums_set.find(num) != nums_set.end()) {
                result_set.insert(num);
            }
        }
        return vector<int>(result_set.begin(), result_set.end());
    }
};
```

**Note**: 注意快速构造unordered_set的方法
