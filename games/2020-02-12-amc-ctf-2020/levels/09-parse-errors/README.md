---
title: "PARSE ERRORS"
country: Mexico
flag: CTF{wh47_700k_y0u_50_l0n6}
points: 15
bonus: 15
decrement: 5
penalty: 10
tag: parsing
---

## Description

```
This log file has only one valid flag.
It has only a pair of balanced parentheses.
It can have digits, letters, and underscores.
```

## Hint

```
Use regular expressions
```

## Instructions

Generate the problem attachments

```bash
python problem.py
```

## Attachments

- [logfile.txt](logfile.txt)

## Solution

`CTF{(_|\d|\w)*}\n` is one regular expression that finds the flag.
