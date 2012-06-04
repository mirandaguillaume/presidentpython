# -*- coding: utf-8 -*-

from carte import Carte
from joueurHumain import joueurHumain
from jeu import paquet

joueurs=list()
nbjoueurs=4
nbCartes=52
joueurs[0]=Joueur("Bob",nbCartes/nbjoueurs)
joueurs[1]=Joueur("Sam",nbCartes/nbjoueurs)
joueurs[2]=Joueur("Alf",nbCartes/nbjoueurs)
joueurs[3]=Joueur("Max",nbCartes/nbjoueurs)
j=paquet()
j.melangePaquet()

def distribuer(liste_joueurs,paquet,nbjoueurs):
    liste_joueurs

