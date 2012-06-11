# -*- coding: utf-8 -*-
import os,math
from main import Main

class joueurHumain:
    """Classe définissant une personne caractéristque :
    - son rang
    - sa main
    - son nom"""

    seCouche=False

    def __init__(self,nom):
        self.nom=nom
        self.main=Main()

    def afficher(self):
        print self.nom
        self.main.afficher()

    def recevoirCarte(self, carte):
        self.main.ajouterCarte(carte)

    def poserCarte(self, carte):
        return self.main.enleverCarte(carte)

    def NbMain(self):
        return self.main.taille()

    def jouer(self,DerniereCarte):
        self.main.trieMain()        
        MainProv=self.affichePoss(DerniereCarte)
        rep=input("Quelle carte voulez_vous choisir ?")
        if rep!='R':
            return MainProv.liste[rep-1]
        else :
            return DerniereCarte
    
    def affichePoss(self,DerniereCarte):
        i=0
        MainProv=Main()
        while (self.main.plusPetit(DerniereCarte,i)==True):
            i+=1
        while (i<self.main.taille()):
            MainProv.ajouterCarte(self.main.liste[i])
            i+=1
        MainProv.afficher()
        return MainProv




