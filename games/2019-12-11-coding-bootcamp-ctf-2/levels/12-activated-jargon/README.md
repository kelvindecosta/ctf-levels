---
title: "ACTIVATED JARGON"
country: Algeria
flag: CTF{softmax}
points: 10
bonus: 5
decrement: 5
penalty: 5
tag: machine-learning
---

## Description

```
You are working with a team of researchers to build a machine learning model that takes as input an image of a person and predicts their ethnicity.

You have gathered a huge dataset of roughly 100 million images. You wish to split it 90-10 for the purpose of training.

You have developed a neural network architecture.
However, during the training process, it performed poorly.

You forgot to apply an Activation Function to the last layer of your network.

Find x, the name of the suitable activation function you would apply.
Flag : CTF{x}
```

## Hint

```
The output layer must be converted to a probabilistic form.
```

## Solution

The `softmax` activation gives a probability distribution meaning all the values sum to one. Softmax does something extra too, it pushes a score close to `1` if it is large and a score close to `0` if it is small.
