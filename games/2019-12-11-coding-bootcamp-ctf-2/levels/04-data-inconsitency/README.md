---
title: "DATA INCONSISTENCY"
country: Nigeria
flag: CTF{21902f8e2f928648352eb27050105531}
points: 30
bonus: 20
decrement: 10
penalty: 15
tag: scraping
---

## Description

```
The attachment contains a list of 1000 profile pages of users on a hypothetical blockchain network.

Each file contains the user's name, number of tokens and wallet.

The number of tokens is initially calculated as the range of the ASCII encodings of the the characters in the user's name.

One user managed to force a 51% attack and set their tokens to an invalid number and crashed the entire network.

Find x, such that x is the wallet id belonging to the user who performed the attack.

Flag : CTF{x}
```

## Hint

```
Compute the number of tokens for each user and check them against the values specified in the files.
```

## Instructions

Install dependencies

```bash
pip install -r requirements.txt
```

Generate the problem attachments

```bash
python problem.py
```

## Attachments

- [profiles](profiles)

## Solution

Refer to [solution.py](solution.py)
