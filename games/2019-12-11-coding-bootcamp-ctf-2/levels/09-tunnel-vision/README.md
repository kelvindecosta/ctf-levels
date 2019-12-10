---
title: "TUNNEL VISION"
country: Brazil
flag : CTF{508x508x3}
points: 20
bonus: 10
decrement: 5
penalty: 10
tag: machine-learning
---

## Description

```
You are working with a team of researchers to build a machine learning model that takes as input an image of a person and outputs an image of that person with a different hair color.

You have gathered a huge dataset of roughly 100 million images. You wish to split it 90-10 for the purpose of training.

Each image is 512 by 512 pixels.

The first layer of your network is a Convolutional Layer with the following specifications:
* F = Kernel Size = (5 x 5)
* S = Stride = 1
* P = Padding = Valid = 0
* Filters = 3

Find x, the shape of the output of the first layer.
Format for x: d1xd2xd3...xdn
Flag: CTF{x}
```

## Hint

```
O = (W - F + 2P) / S + 1
```

## Solution

`O = (512 - 5 + 2 * 0) / 1 + 1 = 507 + 1 = 508`

Output shape = `508x508x3`
