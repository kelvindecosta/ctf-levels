---
title: "GOLD DIGGER"
country: Argentina
flag: CTF{14615}
points: 40
bonus: 30
decrement: 10
penalty: 20
tag: competitive
---

## Description

```
You are a digger and have a map in the form of an m x n grid.
Each cell in the grid denotes a small island which has a certain amount of gold present on it.
The grid uses zero-based array indexing.
You start at the top-left position (0, 0) and end at the bottom-right position (m - 1, n - 1).
Your task is to collect the maximum amount of gold possible.

However, there is an issue. Time is limited and at each island you can do either of the following:
*	move down  from the current cell, i.e, from grid[i][j] go to grid[i + 1][j] if possible
*	move right from the current cell, i.e, from grid[i][j] go to grid[i][j + 1] if possible

Find x, the maximum amount of gold the digger can collect.

Flag: CTF{x}

Input: (input.txt)

The input starts with an integer T denoting the number of test cases.

The first line of each test case contains 2 integers denoting the size (m x n) of the grid.
m lines follow. Each of the m lines consists of n space-separated integers.

Constraints:
1 <= T <= 100
1 <= m, n <= 100
0 <= grid[i][j] <= 100
```

## Hint

```
Sample Input:
1
3 3
5 0 10
4 3 0
2 2 3

Sample Output:
18

Sample Explanation:

Below are all possible paths:

*	path 1: 5->0->10->0->3 = 18
*	path 2: 5->0->3->0->3 = 11
*	path 3: 5->0->3->2->3 = 13
*	path 4: 5->4->3->0->3 = 15
*	path 5: 5->4->3->2->3 = 17
*	path 6: 5->4->2->2->3 = 16

Out of all the paths, 18 is the maximum amount of gold we can collect.
```

## Attachments

- [input.txt](input.txt)

## Solution

Refer to [solution.py](solution.py)
