---
title: "THIS IS RESTRICTED"
country: Australia
flag: CTF{754}
points: 10
bonus: 5
decrement: 5
penalty: 5
tag: file-system
---

## Description

```
What is x, the decimal triplet which describes the set the permissions for a directory where

the owner has read, write and execute permissions,
the group has read and execute permissions,
the rest have read permissions

Flag : CTF{x}
```

## Hint

```
Remember each decimal is governed by 3 bits for read, write and execute.

4 for read, 2 for write and 1 for execute.
```

## Solution

Permissions for:

- `owner` : `4+2+1` = `7`
- `group` : `4+0+1` = `5`
- `owner` : `4+0+0` = `4`

`x` = `754`
