# -*- coding: utf-8 -*-

from paquet import paquet
from joueurHumain import joueurHumain 
from main import Main

class jeu:
	nbGagnant=0
	def __init__(self,nbJoueurs,Joueurs):
		paquet=paquet()
		paquet.melangePaquet()
		self.nbJoueurs=nbJoueurs
		self.Joueurs=Joueurs
		paquet.distribuer(self.Joueurs,nbJoueurs)

	def resteUnJoueur(self):
		cpt=0
		for i in range(i):
			if (Joueurs[i].seCouche):
				cpt++;
		if (cpt==3):
			return True
		return False

	def tour(self,NouvelleListe):
		cpt=self.nbGagnant
		DerniereCarte=list()
		while(self.resteUnJoueur()):
			if (!Joueurs[cpt%self.nbJoueurs].seCouche) or (Joueurs[cpt%nbJoueurs].nbMain()!=0):
				print "Au tour de {0}".format(Joueur[cpt%self.nbJoueurs].nom)
				NewDerniereCarte=Joueurs[cpt%self.nbJoueurs].jouer(DerniereCarte);
				if(NewDerniereCarte!=DerniereCarte)
					self.nbGagnant=cpt%self.nbJoueurs
					DerniereCarte=NewDerniereCarte
				if (Joueurs[cpt%self.nbJoueurs].nbMain()==0)
					NouvelleListe.insert(len(NouvelleListe),Joueurs[cpt%self.nbJoueurs])
				if (DerniereCarte[0].no=2) :
					break;
				else
					cpt++;

	def resteUnJoueurEnJeu(self):
		cpt=0
		for i in range(i):
			if (Joueurs[i].seCouche):
				cpt++;
		if (cpt==3):
			return True
		return False

	def FinTour():
		while(self.resteUnJoueurEnJeu()) :
			tour(NouvelleListe)

	def partie():

