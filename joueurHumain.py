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

    def afficheMain(self,client):
        self.main.affiche(client)

    def jouer(self,DerniereCarte):
        self.main.trieMain()
        self.main.afficher()
        while 1:
            rep=input("Quelle carte voulez_vous choisir (R pour renoncer) ?")
            if self.main.taille()<rep:
                print "Le carte demandée n'est pas dans votre main."
            if rep!='R':
                if self.main.liste[rep-1].no==DerniereCarte.no:
                    return self.poserCarte(rep-1)
                elif (self.main.liste[rep-1]>DerniereCarte) :
                    return self.poserCarte(rep-1)
                else :
                    print "Vous ne pouvez pas jouer cette carte."
            else :
                return DerniereCarte




