#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 08:37:04 2022

@author: tlanchec
"""

Âge = int(input("insérer votre âge"))

if Âge < 18 : 
    print("le tarif est de 8€") 
elif Âge >= 18 and Âge <=65 :
    print("le tarif est de 12€")
else :
    print("le tarif est de 10€")