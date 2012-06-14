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
		self.DerniereCarte=Carte("H",1)
		self.cpt=0

	def resteDeuxJoueur(self):
		cpt=0
		for i in range(len(self.Joueurs)):
			if (self.Joueurs[i].seCouche==True):
				cpt+=1
		if (cpt<3):
			return True
		return False	

	def possibleJouer(self,carte):
		nb=self.cpt%self.nbJoueurs
			if carte.no==self.DerniereCarte.no:
				return True
			else: return carte>DerniereCarte
	

	def setDerniereCarte(carte):
		self.DerniereCarte=carte

	def setCpt():
		cpt+=1

	def setNbGagnant():
		self.nbGagnant=self.cpt%self.nbJoueurs

	def setSeCouche(etat):
		seCouche=etat

	def tour(self):
	
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
					print "Le gagnant du tour est {0}".format(self.Joueurs[self.nbGagnant].nom)
					break
				else:
					DerniereCarte.affiche()
					cpt+=1

	def resteUnJoueurEnJeu(self):
		cpt=0
		for i in range(i):
			if (self.Joueurs[i].main.taille()==0):
				cpt+=1
		if (cpt==3):
			return True
		return False

	def manche():
		NouvelleListe=list()
		while(self.resteUnJoueurEnJeu()) :
			tour(NouvelleListe)
		self.Joueurs=NouvelleListe
		self.EchangesCartes(0,nbJoueurs-1)

	def EchangeCartes(Recv,Send):
		pass
		"""print "Le prisonnier {0} donne ses 2 meilleures cartes au président {1}.".format(self.Joueurs[Send].nom,self.Joueurs[Recv].nom)
		self.Joueurs[Send].trieMain()
		self.Joueurs[Recv].recevoirCarte(self.Joueurs[Send].poserCarte(12))
		self.Joueurs[Recv].recevoirCarte(self.Joueurs[Send].poserCarte(11))
		print "Le président {0} donne ses 2 pires cartes au prisonnier {1}."format(self.Joueurs[Send].nom,self.Joueurs[Recv].nom)

		self.Joueurs[Recv].trieMain()
		self.Joueurs[Send].recevoirCarte(self.Joueurs[Recv].poserCarte(0))
		self.Joueurs[Send].recevoirCarte(self.Joueurs[Recv].poserCarte(1))
"""
