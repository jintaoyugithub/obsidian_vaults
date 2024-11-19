---
tags:
    - codeTest
create date: 2024-11-16
urls:
---

# removeDulplicate

## Code

### My solutions
```cpp
class Solution
{
  public:
    int removeDuplicates(vector<int> &nums)
    {
        int slowIndex = 0;
        for (int fastIndex = 1; fastIndex < nums.size(); fastIndex++)
        {
            if (nums[slowIndex] != nums[fastIndex])
            {
                slowIndex++;
                nums[slowIndex] = nums[fastIndex];
            }
        }

        // Wrong: return slowIndex, ask to return the amount of the array
        return slowIndex + 1;
    }
};
```

Here I also use the method introduced in [[removeelement#better-solutions]], call `Dual Pointers`. 

