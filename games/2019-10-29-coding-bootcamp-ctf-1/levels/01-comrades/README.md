---
title: "COMRADES"
country: Russia
flag: CTF{146}
points: 20
bonus: 10
decrement: 5
penalty: 10
tag: file-system
---

## Description

```
Access the server at 172.16.22.5 and find x, the number of users who registered in 2016 in the Computer Science (A7) Discipline

Flag : CTF{x}
```

## Hint

```
If only there was a command that:

listed out all directories,
applied a filter and
listed out how many of such occurrences were found.

Too bad there isn't a single command that does that.
How about you give up and smoke a pipe?
```

## Solution

Navigate to the `//opt/bits2016` directory and run the following command

```bash
ls -al | grep a7 | wc -l
```
