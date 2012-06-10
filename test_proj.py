# -*- coding: utf-8 -*-

from carte import Carte
from joueurHumain import joueurHumain
from paquet import paquet

nbjoueurs=4
nbCartes=52
joueurs=range(nbjoueurs)
nbCartesEnMain=nbCartes/nbjoueurs
joueurs[0]=joueurHumain("Bob",nbCartesEnMain)
joueurs[1]=joueurHumain("Sam",nbCartesEnMain)
joueurs[2]=joueurHumain("Alf",nbCartesEnMain)
joueurs[3]=joueurHumain("Max",nbCartesEnMain)
j=paquet()
j.melangePaquet()
j.distribuer(joueurs,nbjoueurs)
for i in range(4):
	print joueurs[i].NbMain()
print nbCartesEnMain
while (1):
	a=1