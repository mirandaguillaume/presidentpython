
import random
from carte import Carte
from main import Main

class paquet:

	nom_couleur=["H","S","D","C"]
	nom_carte=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

	def __init__(self):
		self.paquet=Main()
		for i in self.nom_couleur:
			for j in self.nom_carte:
				carte=Carte(i,j)
				self.paquet.ajouterCarte(carte)

				
	def affichePaquet(self):
		self.paquet.afficher()

	def melangePaquet(self):
		paquetMelange=Main()
		for i in range(self.paquet.taille()):
			j=random.randint(0,self.paquet.taille()-1)
			paquetMelange.ajouterCarte(self.paquet.enleverCarte(j))
		self.paquet=paquetMelange

	def taille(self):
		return self.paquet.taille()

	def donnerCarte(self):			
		return self.paquet.enleverCarte(0)

	def distribuer(self,listejoueurs,nbMain):
		for i in range(len(listejoueurs)):
			print i
			print listejoueurs[i].nom
		for i in range(nbMain):
			for j in range(len(listejoueurs)):
				listejoueurs[j].recevoirCarte(self.donnerCarte())


	
			
