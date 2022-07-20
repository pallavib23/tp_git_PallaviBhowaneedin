#!/bin/env python

import sys 

def add(a,b):
        sum = a + b
        print(sum)

a = int( sys.argv[1] )
b = int( sys.argv[2] )

a = int( sys.argv[1] )
b = int( sys.argv[2] )


try:
        a = int( sys.argv[1] )
        b = int( sys.argv[2] )
except IndexError:
        print("ERREUR. 2 valeurs numériques")
        a = int(input("Entrez la premiere valeur : "))
        b = int(input("Entrez la seconde valeur : "))
        add(a,b)
	

add(a,b)
