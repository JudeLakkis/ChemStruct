#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("result.txt", "r") as f:
    data = [i.strip() for i in f.readlines()]

for i in data:
    print(i.split(','))
