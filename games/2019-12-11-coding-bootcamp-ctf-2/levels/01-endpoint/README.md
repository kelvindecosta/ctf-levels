---
title: "ENDPOINT"
country: India
flag: CTF{8443}
points: 10
bonus: 5
decrement: 5
penalty: 5
tag: web
---

## Description

```
In computer networking, a port is a communication endpoint.

Different communication protocols use specific ports.

Find x, such that x is the port assigned to the web server that hosts this site

Flag : CTF{x}
```

## Hint

```
A port can be identified easily by studying the url of the site.

protocol://domain:port
```

## Solution

The site is hosted at [https://ec2-157-175-57-89.me-south-1.compute.amazonaws.com:8443/](https://ec2-157-175-57-89.me-south-1.compute.amazonaws.com:8443/) and hence the port number is `8443`
