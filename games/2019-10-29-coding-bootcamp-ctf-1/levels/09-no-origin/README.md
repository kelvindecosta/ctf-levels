---
title: "NO ORIGIN"
country: Greenland
flag : CTF{7h15_15_n07_4_url}
points: 20
bonus: 10
decrement: 5
penalty: 10
tag: version-control
---

## Description

```
There is a flag hidden somewhere in this repo.
Wait, maybe it's on the remote.
```

## Hint

```
Use git remote
```

## Attachments

*   [repo](repo/)

## Solution

```bash
git remote -v
```
