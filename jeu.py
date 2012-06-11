# -*- coding: utf-8 -*-

from carte import Carte
from paquet import paquet
from joueurHumain import joueurHumain 
from main import Main

class jeu:
	nbGagnant=0
	def __init__(self,nbJoueurs,Joueurs):
		Paquet=paquet()
		Paquet.melangePaquet()
		self.nbJoueurs=nbJoueurs
		self.Joueurs=Joueurs
		Paquet.distribuer(self.Joueurs,52/nbJoueurs)

	def resteDeuxJoueur(self):
		cpt=0
		for i in range(len(self.Joueurs)):
			if (self.Joueurs[i].seCouche==True):
				cpt+=1
		if (cpt<3):
			return True
		return False

	def tour(self,NouvelleListe):
		cpt=self.nbGagnant
		DerniereCarte=Carte("H",3)
		print "ok1"
		while(self.resteDeuxJoueur()):
			print "ok2"
			if (self.Joueurs[cpt%self.nbJoueurs].seCouche==False): 
				if (self.Joueurs[cpt%self.nbJoueurs].NbMain()==0):
					break
				print "Au tour de {0}".format(self.Joueurs[cpt%self.nbJoueurs].nom)
				NewDerniereCarte=self.Joueurs[cpt%self.nbJoueurs].jouer(DerniereCarte);
				if(NewDerniereCarte!=DerniereCarte):
					self.nbGagnant=cpt%self.nbJoueurs
					DerniereCarte=NewDerniereCarte
				if (self.Joueurs[cpt%self.nbJoueurs].NbMain()==0):
					NouvelleListe.insert(len(NouvelleListe),self.Joueurs[cpt%self.nbJoueurs])
				if (DerniereCarte.no==2) :
					break
				else:
					DerniereCarte.affiche()
					cpt+=1

	def resteUnJoueurEnJeu(self):
		cpt=0
		for i in range(i):
			if (self.Joueurs[i].seCouche):
				cpt+=1
		if (cpt==3):
			return True
		return False

	def FinTour():
		while(self.resteUnJoueurEnJeu()) :
			tour(NouvelleListe)
