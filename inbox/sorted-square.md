---
tags:
    - codeTest
create date: 2024-11-17
urls:
---

# sorted-square

## Solutions

### My solutions

```cpp
class Solution
{
  public:
    vector<int> sortedSquares(vector<int> &nums)
    {
        vector<int> sortedSquaresNums(nums.size());
        int slowIndex = 0;
        int fastIndex = nums.size() - 1;
        int index = nums.size() - 1;

        while (slowIndex <= fastIndex)
        {
            if (abs(nums[slowIndex]) < abs(nums[fastIndex]))
            {
                sortedSquaresNums[index--] = pow(nums[fastIndex--], 2);
            }
            else
            {
                sortedSquaresNums[index--] = pow(nums[slowIndex++], 2);
            }
        }

        return sortedSquaresNums;
    }
};
```


