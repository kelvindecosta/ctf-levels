---
title: "SHAMELESS SELF PROMOTION"
country: United Arab Emirates
flag : CTF{590490000}
points: 15
bonus: 10
decrement: 5
penalty: 10
tag: miscellaneous
---

## Description

```
There are 3 special interest groups at ACM BPDC Chapter :

*   ACM CP
*   ACM AI
*   ACM HEX

You can find the links to their specific pages on our website.

The flag is "CTF{X}" where X = ((L1 x B1) + (L2 x B2) + (L3 x B3)) ^ 2
```

## Hint

```
Maybe the dimensions of the logos will help you?
```

## Solution

On the [website](https://www.acmbpdc.org/), each of the SIG's logos are 90x90 pixels.
Plug these values into the formula to get `X = 590490000`
