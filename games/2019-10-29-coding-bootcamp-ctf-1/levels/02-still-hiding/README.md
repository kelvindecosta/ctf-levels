---
title: "STILL HIDING"
country: Canada
flag: CTF{0h_5h17_y0u_f0und_m3}
points: 30
bonus: 20
decrement: 10
penalty: 15
tag: file-system
---

## Description

```
Somewhere in the server at 172.16.22.5 within the HOME directories of users registered in 2016, there is a hidden file named ctf-1-q2-flag.txt
```

## Hint

```
If only there was a command that:

listed out all directories recursively
and applied a filter

Too bad there isn't a single command that does that. Or is there?
How about you give up and smoke a pipe again?
```

## Solution

Run the following command

```bash
cat $(tree -afi //opt/bits2016 | grep .ctf-1-q2-flag.txt)
```
