---
title: "HASH HASH BABY"
country: Sudan
flag : CTF{fbc658352369e0d3f1b29ad0c7171a541c8d32ab}
points: 10
bonus: 5
decrement: 5
penalty: 5
tag: version-control
---

## Description

```
Find x, the id of the first commit on acmbpdc's coding-bootcamp repository

Flag : CTF{x}
```

## Hint

```
Each commit is identified by a hash
```

## Solution

```bash
git clone https://github.com/acmbpdc/coding-bootcamp
git log
```
