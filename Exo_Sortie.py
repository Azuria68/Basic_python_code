#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 08:41:53 2022

@author: tlanchec
"""

Température = int(input("Quelle est la température ?"))
Temps = input("y a t-il du Soleil ou de la Pluie ?")
Orage = input("Y'a t-il des orages ?")
if Orage == ("Oui") : 
    Orage = True
else : 
    Orage = False

if Température >= 20 and Temps == ("Soleil") : 
    print ("on peut sortir")

elif Température < 20 and Temps == ("Soleil") : 
    print ("on peut pas sortir")

elif Température >=25 and Temps == ("Pluie") and Orage == True: 
    print ("on peut sortir")

elif Température >= 25 and Temps == ("Pluie") and Orage == False : 
    print ("on peut pas sortir")

elif Température < 25 and Temps == ("Pluie") and Orage == False : 
    print ("on peut pas sortir")

    