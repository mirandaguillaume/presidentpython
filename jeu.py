# -*- coding: utf-8 -*-

from carte import Carte
from paquet import paquet
from joueurHumain import joueurHumain 
from main import Main

class jeu:
	nbGagnant=0
	def __init__(self,nbJoueurs,Joueurs):
		self.Paquet=paquet()
    		self.nbJoueurs=nbJoueurs
		self.Joueurs=Joueurs
		self.DerniereCarte=Carte("H",1)
		self.cpt=-1

	def resteDeuxJoueur(self):
		cpt=0
		for i in range(len(self.Joueurs)):
			if (self.Joueurs[i].seCouche==True):
				cpt+=1
		if (cpt<3):
			return True
		return False	

	def possibleJouer(self,carte):
		if carte.no==self.DerniereCarte.no:
			return True
		else: return carte>self.DerniereCarte
	

	def setDerniereCarte(self,carte):
		self.DerniereCarte=carte

	def setCpt(self):
		self.cpt+=1

	def setNbGagnant(self):
		self.nbGagnant=self.cpt%self.nbJoueurs

	def setSeCouche(self,i,etat):
		self.Joueurs[i].seCouche=etat
