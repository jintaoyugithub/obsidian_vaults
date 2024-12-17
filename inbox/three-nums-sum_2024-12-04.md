---
tags:
    - codeTest
create date: 2024-12-04
urls:
---

# Three nums sum

## Solutions

### Mine

- First ^1st

```cpp
class Solution {
  public:
    vector<vector<int>> threeSum(vector<int> &nums) {
      unordered_multimap<int, int> umaps;
      vector<vector<int>> result;
      // init umaps
      for (int i = 2; i < nums.size(); i += 3) {
        // key is the nums value, value is the index
        umaps.insert(nums[i], i);
      }
  
      int sum = 0;
      for (int i = 0; i < nums.size(); i += 3) {
        for (int j = 1; j < nums.size(); j += 3) {
          sum = nums[i] + nums[j];
  
          auto found = umaps.find(-sum);
          if (found != umaps.end()) {
            vector<int> temp{i, j, found->second};
            result.push_back(temp);
            // erase the element
            umaps.erase(found);
          }
        }
      }
  
      return result;
    }
  }
};
```

**Reasonging**:  ^1stReasoning

通过两个循环来记录两个数只和，然后总的sum要是0，所以事先将nums的数据以unordered map的形式存储起来，然后在那里面来找（0 - sum）， 能找到就返回他们的值，这里的目的就是用hash table产生的空间复杂度来换一个for循环的时间负责度，但是要考虑一件事情，就是`去重`，在hash table中去重变得很麻烦，所以这道题更好的解法是`双指针`.

- Second ^2nd

#### Solutions Analysis

| Attempts  | Reasoning          | Pass? | Reasons                 | Runtime cost | Memory cost |
|-----------|--------------------|-------|-------------------------|--------------|-------------|
| [[#^1st]] | [[#^1stReasoning]] | No    | can not avoid repeating | N/A          | N/A         |


### Standard

## Notes

