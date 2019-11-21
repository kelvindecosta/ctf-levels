---
title: "THIS IS YOUR HOST"
country: Libya
flag : CTF{nginx}
points: 15
bonus: 10
decrement: 5
penalty: 5
tag: web
---

## Description

```
What type of server is the website running on?

The flag is "CTF{X}" where X is the type of server in lowercase
```

## Hint

```
See if you can find anything with developer tools.
```

## Solution

The HTTP Response header `Server` is `nginx`
