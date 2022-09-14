# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:55:13 2022

@author: Tomla
"""
#importer la bibliothèque random déjà installer avec python
import random 


x = (input("voulez vous jouer (y/n) ? "))


if x == "y":     
    nb = random.randint(1,50)
    print("le nombre à trouver est entre 1 et 50")
    nbj = int(input("nombre = "))
    
#ici on cherche si notre nombre est plus grand ou plus petit
    while nbj != nb :
        if nbj > nb : 
            print(f"le nombre à trouver est plus petit que {nbj}")
            nbj = int(input("nombre= "))
        
        elif nbj < nb : 
            print(f"le nombre à trouver est plus grand que {nbj}")
            nbj = int(input("nombre= "))  
            
#pas obligé de else car on sort de la boucle si on a le juste prix 
    print (f"{nbj} est le juste prix let's gooo")

else : 
    print("ok m'en fou")
