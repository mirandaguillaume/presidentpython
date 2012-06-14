# -*- coding: utf-8 -*-
import os
from carte import Carte
class Main:

    def __init__ (self):
        self.liste=list()

    def affiche(self,client):
        for i in range(len(self.liste)):
            client.send.affiche("{0}. {1}".format(i+1,self.liste[i].affiche()))

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

    def trieMain(self):
        aucunEchange=False
        while (aucunEchange==False):
            aucunEchange=True
            for j in range(len(self.liste)-1):
                if self.liste[j] > self.liste[j+1] :
                    self.liste[j],self.liste[j+1]=self.liste[j+1],self.liste[j]
                    aucunEchange=False

    def plusPetit(self,derniereCarte,i):
        return derniereCarte>self.liste[i]
