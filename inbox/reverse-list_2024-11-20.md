---
tags:
    - codeTest
create date: 2024-11-20
urls:
    - [reverse list leetcode link](https://leetcode.cn/problems/reverse-linked-list/)
---

# Reverse List

## Solutions

### My solutions

```cpp
class Solution {
public:
  ListNode *reverseList(ListNode *head) {
    // find the rear pointer
    ListNode *rear = head;
    ListNode *prev = nullptr;

    if(head != nullptr) {
        while (rear->next != nullptr) {
        prev = rear;
        rear = rear->next;
        }
    } else {
        return nullptr;
    }

    rear->next = head;
    prev->next = nullptr;

    return rear;
  }
};

```
- **States**:

`Pass?`: No

`Reasons`: dont know how to reverse the *next* pointer.

### Standard solutions



