---
title: "SO META"
country: Russia
flag : CTF{53lf_r3f3r3n714l}
points: 25
bonus: 15
decrement: 5
penalty: 15
tag: meta
---

## Description

```
This program requires a file as input
```

## Hint

```
Did you try running the file on itself?
```

## Instructions

Generate the problem attachments

```bash
javac Program.java
seq -w 1 10 | xargs -n1 -I% sh -c 'dd if=/dev/urandom of=file.% bs=$(shuf -i1-10 -n1) count=1024'
```

## Attachments

*   [Program.class](Program.class)
*   [files/](files/)

## Solution

Run the file on itself

```bash
java Program Program.class
```
