---
title: "TIME TRAVEL"
country: Greenland
flag: CTF{n37w0rk_4dm1n_cr135}
points: 30
bonus: 20
decrement: 10
penalty: 15
tag: version-control
---

## Description

```
Travel back to find the flag.
Are you the Hacker-Man?
```

## Hint

```
Use git diff commit1..commit2
```

## Attachments

- [repo](repo/)

## Solution

Use `git diff commit1..commit2` to check differences between commits.

```bash
git diff 0a4b..982b
```
