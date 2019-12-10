---
title: "GG WP"
country: Russia
flag : CTF{pk3yr9oudo}
points: 30
bonus: 20
decrement: 10
penalty: 15
tag: competitive
---

## Description

```
The attachment contains a list of 1000 games between 100 bots.

Each line of the file is of the following format

{bot1} defeated {bot2}

Find x, such that x is the username of the bot who was not defeated by any other bot.

Flag : CTF{x}
```

## Hint

```
Try making two sets; winners and losers.
```

## Instructions

Generate the problem attachments

```bash
python problem.py
```

## Attachments

*   [input.txt](input.txt)

## Solution

Refer to [solution.py](solution.py)
