#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 09:52:24 2022

@author: tlanchec
"""

your_list = 'abcdefghijklmnopqrstuvwxyz'
complete_list = []
for current in range(10):
    a = [i for i in your_list]
    for y in range(current):
        a = [x+i for i in your_list for x in a]
    complete_list = complete_list+a