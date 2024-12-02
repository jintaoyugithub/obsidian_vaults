---
tags:
    - DS&Algo
create date: 2024-11-15
urls:
---

# Array

## Questions

1. How does the memory distribution looks like? What about 2-dim array?

2. What happen when we "delete" a element from an array?

## Common tips

We can generally use brute force to solve most array-related problems, but this approach typically results in a time complexity of `O(n^2)`, sometimes even `O(n^3)`. Therefore, we usually aim to implement algorithms with a time complexity of only O(n) by leveraging techniques such as `dual pointer` methods and their variations.

- Dual pointers

- Sliding Window

- Prefix Sum

## Leetcode Question Overview ^arrayLeetCode

| Notes Link            | Description                                                                    | Level | Quick Tips               |
|-----------------------|--------------------------------------------------------------------------------|-------|--------------------------|
| [[binary-search]]     | Search for the target element by using binary search algorightm                | Easy  | Left and right pointer   |
| [[remove-element]]    | Remove the target element from a sorted array                                  | Easy  | Dual(fast/slow) pointer  |
| [[remove-dulplicate]] | Remove the dulplicate elements from a sorted array                             | Easy  | Dual(fast/slow) pointer  |
| [[sorted-square]]     | Return a new array that contain the square of each elements in the given array | Easy  | Dual(front/rear) pointer |
| [[min-sub-array]]     | Return the len of the sub array which the sum of it equal to the given target  | Mid   | Sliding window           |
| [[sum-sub-range]]     | Return the sum of the given sub range                                         | Easy  | Prefix Sum               |







