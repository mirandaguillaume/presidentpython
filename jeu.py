import random
from carte import Carte
from main import Main

class jeu:
	
	couleur=["H","S","D","C"]
	nom_carte=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
	def __init__(self):
		self.paquet=Main(52)
		for i in self.couleur:
			for j in self.nom_carte:
				carte=Carte(i,j)
				self.paquet.ajouterCarte(carte)

				
	def affichePaquet(self):
		self.paquet.afficher()

