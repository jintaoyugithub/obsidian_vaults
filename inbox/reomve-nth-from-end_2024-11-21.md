---
tags:
    - codeTest
create date: 2024-11-21
urls:
    - [Remove Nth from end LeetCode link](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)
---

# Reomve Nth From End

## Solutions

### Mine

- First Try

```cpp
class Solution {
public:
  ListNode *removeNthFromEnd(ListNode *head, int n) {
    ListNode *dummy = new ListNode(0);
    dummy->next = head;
    ListNode *slowIndex = dummy;
    ListNode *fastIndex = dummy;

    // find the length of the list
    uint _size = 0;
    while (fastIndex->next != nullptr) {
      _size++;
    }

    if (n > _size)
      return dummy->next;

    // get the index of the previous node
    uint itr = _size-(n+1);
    while (itr--) {
      slowIndex = slowIndex->next;
    }

    fastIndex = slowIndex->next;
    slowIndex->next = fastIndex->next;
    delete fastIndex;

    return dummy->next;
  }
};
```

- **States**:

`Pass?`: NO

`Reasons`: dont know, I try to first find the length of the list and then move the pointer to the position of len-n+1

- Seond try

```cpp
class Solution {
public:
  ListNode *removeNthFromEnd(ListNode *head, int n) {
    if (head == nullptr)
      return nullptr;

    ListNode *slow = head;
    ListNode *fast = head;

    while (n--) {
      fast = fast->next;
    }

    while (fast != nullptr) {
      slow = slow->next;
      fast = fast->next;
    }

    ListNode* target = slow->next;
    if(target != nullptr) {
        slow->next = target->next;
    } else {
        slow->next = nullptr;
    }
    delete target;
    target = nullptr;

    return head;
  }
};
```

- **States**:

`Pass?`: NO

`Reasons`: 但凡有删除的操作或者添加的操作，都要考虑头节点，增加`dummy node` 是最优解，它让头节点的删除和添加操作和其他节点一样，这里我就是忘记加dummy node导致在`case [1], 删除倒数第一个`的例子中失败。

