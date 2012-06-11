# -*- coding: utf-8 -*-

from carte import Carte
from joueurHumain import joueurHumain
from paquet import paquet
from jeu import jeu

nbjoueurs=4
joueurs=range(nbjoueurs)
joueurs[0]=joueurHumain("Bob")
joueurs[1]=joueurHumain("Sam")
joueurs[2]=joueurHumain("Alf")
joueurs[3]=joueurHumain("Max")
j=jeu(nbjoueurs,joueurs)
j.tour(joueurs)
