---
tags:
    - DS&Algo
create date: 2024-11-22
urls:
---

# Hash Table

## Basic

>Access through keywords, array is one kine of Hash Table

1. Common data structure based on hash

- Arraay

- Set

- Map

2. `Hash Function`

Translate given key work to the index of a hash table

3. `Hash Collisions` 

It's a problem when the `hash function` give the same index based on the different `key word`.

There are two ways to solve this:

- Chaining

![hashtable-chaining.png](assets/imgs/hashtable-chaining.png)

- Linear Probing

Find another empty index to store the elements in the hash table.


### Tips

## Questions & Problems

1. 为什么我们不用一个更大的hash table，而使用哈希碰撞来解决哈希函数映射到同一索引？

## LeetCode Questions Overview ^hashTableLeetCode

| Notes link                       | Description                                                  | Level | Quick Tips                         | State    |
| -------------------------------- | ------------------------------------------------------------ | ----- | ---------------------------------- | -------- |
| [[anagram_2024-11-24]]           | determine if b is a's anagram                                | Easy  | None                               | Done     |
| [[find-intersection_2024-11-24]] | find the intersection of two vectors                         | Easy  | None                               | Done     |
| [[happy-num_2024-11-30]]         | determine if a num is happy num                              | Easy  | Optimize with unordered list       | Done     |
| [[two-sum_2024-11-30]]           | find two elements which the sum equals to the target         | Easy  | 一个数的和可转化成一个已知数找另一个未知数              | No clue  |
| [[four-sum-count_2024-12-02]]    | find how many combinations of four nums euqal to 0           | Mid   | Same as above                      | Not Done |
| [[can-construct_2024-12-02]]     | determine if B can be constructed by using the elements in A | Easy  | optimize with array instead of map | Done     |



