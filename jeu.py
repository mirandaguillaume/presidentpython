import random
from carte import Carte
from main import main

class jeu:

couleur=["H","S","D","C"]
nom_carte=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
	def __init__(self):
		paquet=Main(52)
		for i in couleur:
			for i in nom_carte:
				carte=Carte(couleur,nom_carte)
				self.paquet.ajouterCarte(carte)

