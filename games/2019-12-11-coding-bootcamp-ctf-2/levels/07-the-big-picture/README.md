---
title: "THE BIG PICTURE"
country: France
flag : CTF{90000000x512x512x3}
points: 10
bonus: 5
decrement: 5
penalty: 5
tag: machine-learning
---

## Description

```
You are working with a team of researchers to build a machine learning model that takes as input an image of a person and outputs an image of that person with a different hair color.

You have gathered a huge dataset of roughly 100 million images. You wish to split it 90-10 for the purpose of training.

Each image is 512 by 512 pixels.

Find x, the shape of the training data.
Format for x: d1xd2xd3...xdn
Flag : CTF{x}
```

## Hint

```
From the information, 90 million images are used for training.
```

## Solution

`90000000` images * `512` pixels * `512` pixels * `3` color channels

Output shape = `90000000x512x512x3`
