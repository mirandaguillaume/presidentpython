# -*- coding: utf-8 -*-
import os
from carte import Carte
class Main:

    liste=list()
    nbCarte=0

    def __init__ (self,maxi):
        self.maxi=maxi

    def afficher(self):
        for i in range(self.nbCarte):
            if self.liste[i]!=0:
                self.liste[i].affiche()

    def ajouterCarte(self, carte):
        self.nbCarte+=1
        self.liste.insert(self.nbCarte-1,carte)

    def enleverCarte(self,j):
        carte1=self.liste[j]
        del self.liste[j]
        self.nbCarte-=1
        return carte1
    
    def taille(self):
        return self.nbCarte

    
