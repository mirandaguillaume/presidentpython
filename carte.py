# -*- coding: utf-8 -*-
import os

class Carte:

    def __init__(self,couleur,no):
        self.couleur=couleur
        self.no=no

    def affiche(self):
        print "{0} de {1}".format(self.no,self.couleur)


