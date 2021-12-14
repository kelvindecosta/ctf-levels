---
title: "OUT OF THE NORM"
country: Canada
flag: CTF{12}
points: 20
bonus: 10
decrement: 5
penalty: 10
tag: scripting
---

## Description

```
If you have kept tabs on this page you would have noticed something unusual.

Transform from unfamiliar words to familiar digits to obtain a set of 5 numbers.

Let the numbers be a,b,c,d,e;
Find x, the number of permutations of these digits in the expression `a+b-c+d-e` that result in `1`.
The flag is the number of permutations that satisfy the above in the format:CTF{x}

For eg : If the digits were 0,7,3,5,2

(3+5-0+7-2)=1
(3+5-2+0-7)=1
(5+3-0+7-2)=1
(5+3-2+0-7)=1

4 such permutations, therefore the flag would be:CTF{4}
```

## Hint

```
Have a look at the title of the webpage to get the numbers, then permute them in the given expressionandcount how many of those result in 1
```

## Attachments

- [page.html](page.html)

## Solution

Refer to [notes.pdf](notes.pdf)
