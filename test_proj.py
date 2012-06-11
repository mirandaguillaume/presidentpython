# -*- coding: utf-8 -*-

from carte import Carte
from joueurHumain import joueurHumain
from paquet import paquet

nbjoueurs=4
nbCartes=52
joueurs=range(nbjoueurs)
nbCartesEnMain=nbCartes/nbjoueurs
joueurs[0]=joueurHumain("Bob")
joueurs[1]=joueurHumain("Sam")
joueurs[2]=joueurHumain("Alf")
joueurs[3]=joueurHumain("Max")
j=paquet()
j.melangePaquet()
j.paquet.trieMain()
j.affichePaquet()
j.melangePaquet()
"""j.distribuer(joueurs,nbCartesEnMain)
for i in range(4):
	joueurs[i].afficher()"""