---
title: "ONLY FOR 10xers"
country: United States
flag : CTF{74}
points: 30
bonus: 20
decrement: 10
penalty: 15
tag: competitive
---

## Description

```
We have a function f(x) defined as follows:
	f(x) = x + 1, while trailing zero exists, remove
​
For example
	f(3) = 4;		3 + 1 = 4
	f(999) = 1;		999 + 1 = 1000 -> 100 -> 10 -> 1
	f(31099) = 311;	31099 + 1 = 31100 -> 3110 -> 311
​
Given an integer n, count all the unique numbers which we can be obtained by applying the function infinitely many times on n.
​
Test Input 1
n = 1
​
Test Output 1
9
​
Test Explanation 1
We can apply the function f multiple times to get all the number 1 through 9
f(1) = 2
f(f(1)) = f(2) = 3
f(f(f(1))) = f(f(2)) = f(3) = 4
. . .
f(9) = 1;	9 + 1 = 10 -> 1

Find x, such that x is the number of unique numbers obtained by applying the function infinitely many times on n=12345678987654321

Flag : CTF{x}
```

## Hint

```
Test Input 2
n = 10
​
Test Output 2
19
​
Test Explanation 2
Below is table denoting the number of times function f was applied and the value
| times | value |
|-------|-------|
| 0		| 10 	|
| 1		| 11	|
| 2		| 12	|
| 3		| 13	|
| 4		| 14	|
| 5		| 15	|
| 6		| 16	|
| 7		| 17	|
| 8		| 18	|
| 9		| 19	|
| 10	| 2		|
| 11	| 3		|
| 12	| 4		|
| 13	| 5		|
| 14	| 6		|
| 15	| 7		|
| 16	| 8		|
| 17	| 9		|
| 18	| 1		|
```

## Solution

Refer to [solution.py](solution.py)
