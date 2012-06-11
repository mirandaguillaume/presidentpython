# -*- coding: utf-8 -*-

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

	def resteUnJoueur(self):
		cpt=0
		for i in range(len(self.Joueurs)):
			if (self.Joueurs[i].seCouche):
				cpt+=1
		if (cpt==3):
			return True
		return False

	def tour(self,NouvelleListe):
		cpt=self.nbGagnant
		DerniereCarte=list()
		print "ok1"
		while(self.resteUnJoueur()):
			print "ok2"
			if (self.Joueurs[cpt%self.nbJoueurs].seCouche==False): 
				if (self.Joueurs[cpt%nbJoueurs].nbMain()==0):
					break
				print "Au tour de {0}".format(self.Joueur[cpt%self.nbJoueurs].nom)
				NewDerniereCarte=self.Joueurs[cpt%self.nbJoueurs].jouer(DerniereCarte);
				if(NewDerniereCarte!=DerniereCarte):
					self.nbGagnant=cpt%self.nbJoueurs
					DerniereCarte=NewDerniereCarte
				if (self.Joueurs[cpt%self.nbJoueurs].nbMain()==0):
					NouvelleListe.insert(len(NouvelleListe),self.Joueurs[cpt%self.nbJoueurs])
				if (DerniereCarte[0].no==2) :
					break
				else:
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
