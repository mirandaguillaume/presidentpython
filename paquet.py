
import random
from carte import Carte
from main import Main

class paquet:
	
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

	def melangePaquet(self):
		paquetMelange=Main(52)
		for i in range(52):
			j=random.randint(0,self.paquet.nbCarte-1)
			paquetMelange.ajouterCarte(self.paquet.enleverCarte(j))
		self.paquet=paquetMelange

	def taille(self):
		return self.paquet.taille()

	def donnerCarte(self):			
		return self.paquet.enleverCarte(0)

	def distribuer(self,listejoueurs,nbjoueurs):
		cpt=0
		while self.paquet.taille()!=0 :
			print self.paquet.taille()
			listejoueurs[cpt%nbjoueurs].recevoirCarte(self.donnerCarte())
			cpt+=1

	
			
