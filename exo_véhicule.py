#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 08:33:43 2022

@author: tlanchec
"""

Véhicule = int(input("insérér la masse du véhicule"))

if Véhicule >=0 and Véhicule <=20 : 
    print ("C'est un vélo")
elif Véhicule >=200 and Véhicule <=3500 : 
    print ("C'est un voiture")
elif Véhicule >=3500 and Véhicule <=26000 : 
    print ("C'est un camion")
elif Véhicule >26000 : 
    print ("C'est un avion")