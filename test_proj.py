# -*- coding: utf-8 -*-

from carte import Carte
from joueurHumain import joueurHumain
from jeu import paquet

joueurs=list()
nbjoueurs=4
nbCartes=52
joueurs[0]=joueurHumain("Bob",nbCartes/nbjoueurs)
joueurs[1]=joueurHumain("Sam",nbCartes/nbjoueurs)
joueurs[2]=joueurHumain("Alf",nbCartes/nbjoueurs)
joueurs[3]=joueurHumain("Max",nbCartes/nbjoueurs)
j=paquet()
j.melangePaquet()
distribuer(joueurs,j,nbjoueurs)
for i in range(4):
joueurs


def distribuer(liste_joueurs,paquet,nbjoueurs):
    cpt=random.randint(0,3)
    while paquet.taille()!=0:
        liste_joueur[cpt].recevoirCarte(paquet.donnerCarte())
        cpt=random.randint(0,3)

