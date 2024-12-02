---
tags:
    - codeTest
create date: 2024-11-16
urls:
---

# Remove Element Question Overview

## Array

[Remove element array leetcode]()

### Solutions

- My solution

- Better solutions

1. **Dual pointers**

## List

[Remove element list leetcode](https://leetcode.cn/problems/remove-linked-list-elements/description/)
### Solutions

- My solution

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
  ListNode *removeElements(ListNode *head, int val) {
    ListNode* lastNodePtr = nullptr;

    // in case of empty list
    if(head == nullptr) return nullptr;

    // if you try to use i->next !- nullptr wiil skip the last element
    for (ListNode* i = head; i != nullptr; i = i->next) {
      if (i->val == val) {
        if (lastNodePtr == nullptr) {
          // fatal, here the code sai i->next = nullptr
          // after continue, i will be set to i->next, which i nullptr
          // i->next = nullptr;
          head = i->next;
          continue;
        }

        lastNodePtr->next = i->next;
        continue;
      }

      lastNodePtr = i;
    }

    return head;
  }
};
```

**Shortcomings**

- forget to free the memory of the element which need to be deleted


