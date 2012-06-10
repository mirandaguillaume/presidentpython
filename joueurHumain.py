# -*- coding: utf-8 -*-
import os,math
from main import Main

class joueurHumain:
    """Classe définissant une personne caractéristque :
    - son rang
    - sa main
    - son nom"""
    rang=0
    maxi=0
    main=Main(0)
    def __init__(self, nom,maxim):
        self.nom=nom
        self.maxi=maxim
        main=Main(self.maxi)

    def afficher(self):
        print self.nom
        self.main.afficher()

    def recevoirCarte(self, carte):
        self.main.ajouterCarte(carte)

    def poserCarte(self, carte):
        self.main.enleverCarte(carte)

    def NbMain(self):
        return self.main.taille()


