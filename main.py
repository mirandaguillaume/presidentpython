# -*- coding: utf-8 -*-
import os
from carte import Carte
class Main:

    def __init__ (self):
        self.liste=list()

    def afficher(self):
        for i in range(len(self.liste)):
            if self.liste[i]!=0:
                self.liste[i].affiche()

    def ajouterCarte(self, carte):
        self.liste.insert(len(self.liste),carte)

    def enleverCarte(self,j):
        carte1=self.liste[j]
        del self.liste[j]
        return carte1
    
    def taille(self):
        return len(self.liste)

    
