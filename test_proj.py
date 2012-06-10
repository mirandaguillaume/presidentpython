# -*- coding: utf-8 -*-

from carte import Carte
from joueurHumain import joueurHumain
from jeu import paquet

nbjoueurs=4
nbCartes=52
joueurs=range(nbjoueurs)
joueurs[0]=joueurHumain("Bob",nbCartes/nbjoueurs)
joueurs[1]=joueurHumain("Sam",nbCartes/nbjoueurs)
joueurs[2]=joueurHumain("Alf",nbCartes/nbjoueurs)
joueurs[3]=joueurHumain("Max",nbCartes/nbjoueurs)
j=paquet()
j.melangePaquet()
j.distribuer(joueurs,nbjoueurs)
