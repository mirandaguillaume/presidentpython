# -*- coding: utf-8 -*-
import os

class Carte:

    def __init__(self,couleur,no):
        self.couleur=couleur
        self.no=no

    def affiche(self):
        print "{0} de {1}".format(self.no,self.couleur)

    def __gt__(self,other):
    	if self.no==other.no:
    		return False
    	if self.no==2 :
    		return True
    	elif other.no==2:
    		return False
    	elif self.no in [3,4,5,6,7,8,9,10] :
    		if other.no in [1,3,4,5,6,7,8,9,10] :
    			return (self.no>other.no)
    		else: return False
    	elif self.no in ["J","Q","K","A"]:
			if other.no in [3,4,5,6,7,8,9,10]:
				return True
			elif self.no=="J":
				return False
			elif self.no=="Q":
				if other.no =="J":
					return True
				return False
			elif self.no=="K":
				if other.no=="A":
					return False
				return True
			return True
