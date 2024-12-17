---
tags:
    - codeTest
create date: 2024-12-05
urls:
---

# four-nums-sum

## Solutions

### Mine

- First try ^1st

```cpp
class Solution {
public:
  vector<vector<int>> fourSum(vector<int> &nums, int target) {
    vector<vector<int>> result;

    for (int i = 0; i < nums.size(); i++) {
      for (int j = i + 1; j < nums.size(); j++) {
        int left = j + 1;
        int right = nums.size() - 1;

        while (left <= right) {
          if (left == right) {
            left += 1;
            right = nums.size() - 1;
            continue;
          }

          if ((nums[i] + nums[j] + nums[left] + nums[right]) == target) {
            vector<int> temp{nums[i], nums[j], nums[left], nums[right]};
            result.push_back(temp);
          }

          right--;
        }
      }
    }

    return result;
  }
};
```

**Reasonging**:  ^1stReasoning

其实思路和[[three-nums-sum_2024-12-04]]差不多，就是多了个循环，主要的问题还是出在不知道如何去掉重复的，比如说在遇到例子[2,2,2,2,2]的时候，题目要求只返回[2,2,2,2]，但是我的代码会返回5个同样的答案

 --- --- --- --- ---
|   |   |   |   |   |
 --- --- --- --- ---
  ^   ^   ^       ^
  |   |   |       |  
  i   j   l       r

#### Solutions Analysis

| Attempts  | Reasoning          | Pass? | Reasons                              | Runtime cost | Memory cost |
|-----------|--------------------|-------|--------------------------------------|--------------|-------------|
| [[#^1st]] | [[#^1stReasoning]] | No    | dont know how to avoid repeat result | N/A          | N/A         |


### Standard

## Notes

