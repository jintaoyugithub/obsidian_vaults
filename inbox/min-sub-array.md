---
tags:
    - codeTest
create date: 2024-11-17
urls:
---

# Min Subarray Len

## Solutions

### My Solution

```cpp
class Solution
{
  public:
    int minSubArrayLen(int target, vector<int> &nums)
    {
        int slowIndex = nums.size() - 1;
        int fastindex = nums.size() - 2;

        int sum = nums[slowIndex];
        while (slowIndex > fastindex)
        {
            if (sum == target)
            {
                return (slowIndex - fastindex);
            }

            if (sum < target)
            {
                sum += nums[fastindex--];
                if (fastindex == 0)
                    return 0;
                continue;
            }

            if (sum > target)
            {
                sum = 0;
                slowIndex++;
                sum += nums[slowIndex];
                fastindex = slowIndex - 1;
                continue;
            }
        }

        return 0;
    }
};

```
I tried to use `dual pointers` to solve the question, but 

