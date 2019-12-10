---
title: "ABSOLUTE UNITS"
country: United Kingdom
flag : CTF{1007}
points: 20
bonus: 10
decrement: 5
penalty: 10
tag: scraping
---

## Description

```
Find x, the number of unique strings that are in <strong> tags on this website
```

## Hint

```
Input:
<strong>The Avengers</strong>
<strong>Ice Age</strong>
<strong>Avengers: Endgame</strong>
<strong>Ice Age</strong>
<strong>The Dark Knight</strong>
<strong>The Dark Knight</strong>

Output:
4

Explanation:

The unique text is shown below:

1.	The Avengers
2.	Ice Age
3.	Avengers: Endgame
4.	The Dark Knight

The strings "Ice Age" and "The Dark Knight" repeat.
```

## Links

*   [https://historyfilms.co.uk/](https://historyfilms.co.uk/)

## Solution

Refer to [solution.py](solution.py)

