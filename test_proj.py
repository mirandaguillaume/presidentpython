
# -*- coding: utf-8 -*-
from carte import Carte
from joueurHumain import joueurHumain

joueur1=joueurHumain("Bob",27)
carte1=Carte("H",1)
joueur1.recevoirCarte(carte1)
joueur1.afficher()
