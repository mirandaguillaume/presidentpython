#-*- coding: utf-8 -*-
from jeu import jeu
from joueurHumain import joueurHumain
from pynetez.Protocol import Protocol
from paquet import paquet
from carte import Carte
class GameMaster():

    def __init__(self):
        self.Client=range(4)
        self.Classement=range(4)
        Joueurs=range(4)
        self.j=jeu(4,Joueurs)
        self.FinTour=False
        self.FinManche=False
        self.cpt=0
        self.comp=0

    def poserCarte(self,n,nb):
        if n==-1: # Si le joueur decide de renoncer
            for i in range(4):
                self.Client[i].send.affiche("{0} renonce à son tour de jeu.".format(self.j.Joueurs[nb].nom)) #Affichage du message
            self.j.setSeCouche(nb,True) #On note le joueur comme couche
            self.FiniTour_SansCartes() #On finit le tour
        else : # Sinon,
            if n<0 or n>=self.j.Joueurs[nb].NbMain(): #Si la carte demandee n'existe pas 
                self.Client[nb].send.err1() #Message d'erreur
                self.Client[nb].send.demande(self.j.Joueurs[nb].nom,nb) #Relance de la procedure de demande
            else: #Sinon,
                carte=self.j.Joueurs[nb].main.liste[n]
                if self.j.possibleJouer(carte): #S'il est possible de jouer la carte
                    self.j.setDerniereCarte(self.j.Joueurs[nb].poserCarte(n)) #On met cette carte sur le tapis et on l'enlève du jeu du joueur
                    self.j.Joueurs[nb].AFini=(self.j.Joueurs[nb].NbMain()==0)
                    if self.j.Joueurs[nb].Afini:
                        self.Classement.append(nb)
                        
                    self.j.nbGagnant=nb
                    if carte.no==2: # Si la carte est un 2,
                        for i in range(4):
                            if i!=self.j.nbGagnant:
                                self.j.setSeCouche(i,True) #On coupe le jeu
                    self.FiniTour() #On fini le tour
                
                else :
                    self.Client[nb].send.err2()
                    self.Client[nb].send.demande(self.j.Joueurs[nb].nom,nb)
                

    def getDerniereCarte(self):
        return "Le joueur {0} a joue un {1}".format(self.j.Joueurs[self.j.nbGagnant].nom,self.j.DerniereCarte.affiche())

    def Tour(self):
        nb=(self.j.cpt+1)%self.j.nbJoueurs
        nom=self.j.Joueurs[nb].nom
        for i in range(4):
            for j in range(4):
                self.Client[i].send.affiche("{0} a {1} cartes en main.".format(self.j.Joueurs[j].nom,self.j.Joueurs[j].NbMain())) #Affichage du nombre de cartes
            self.Client[i].send.affiche("Au tour de {0}".format(nom)) #Affichage du joueur courant
        if self.j.Joueurs[nb].Afini: #S'il n'a plus de cartes,
            self.Client[i].send.affiche("{0} n'a plus de cartes.".format(nom)) #Affichage du message 
            self.FiniTour_SansCartes() #Execution de la fin du tour sans cartes
        elif self.j.Joueurs[nb].seCouche: #S'il s'est dejà couche lors de ce tour
            for i in range(4):
                self.Client[i].send.affiche("{0} a déjà renoncé à ce tour.\n".format(nom))  #Affichage du message
            self.FiniTour_SansCartes() #Execution de la fin du tour
        else: #Sinon,
            self.j.Joueurs[nb].main.trieMain() #On trie la main du joueur
            self.j.Joueurs[nb].afficheMain(self.Client[nb],nb) #On lui affiche sa main
            for i in range(4): 
                if i!=nb:
                    self.Client[i].send.wait(nom) #Et pour tous les autres, message d'attente

    def DebutTour(self):
        self.j.cpt=self.j.nbGagnant-1
        self.j.DerniereCarte=Carte("H",1)
        self.FinTour=False
        for i in range(4):
            self.j.Joueurs[i].seCouche=False
        self.Tour()

    def FiniTour_SansCartes(self):
        if self.tourFini(): #Si le tour est fini
            for i in range(4):
                self.Client[i].send.affiche("{0} remporte le tour.".format(self.j.Joueurs[self.j.nbGagnant].nom)) #On affiche le gagnant du tour
                self.DebutTour() #On reamorce le tour
        else :
            self.j.setCpt()
            self.Tour()

    def FiniTour(self):
        nb=self.j.nbGagnant
        for i in range(4):
            self.Client[i].send.affiche(self.getDerniereCarte()) #Affichage de la carte posee
        if self.mancheFinie():
            self.FinieManche()
        if self.tourFini(): #Si le tour est fini
            for i in range(4):
                self.Client[i].send.affiche("{0} remporte le tour.".format(self.j.Joueurs[nb].nom)) #On affiche le gagnant du tour
            self.DebutTour() #On reamorce le tour
        else :
            self.j.setCpt() #Sinon,
            self.Tour()

    def FinieManche(self):
        for i in range(4):
            Joueur=self.j.Joueurs[i]
            while (Joueur.NbMain()==0):
                Joueur.poserCarte(0)
            self.Classement.append(i)
        self.debutManche()

    def nbJoueurs(self):
        return len(self.players)

    def newJoueur(self, client, nom):
        self.j.Joueurs[self.cpt] = joueurHumain(nom)
        self.Client[self.cpt]=client
        self.cpt+=1
        if self.cpt==4:
            self.startGame()

    def startGame(self):
        self.Manche()

    def FinDuJeu(self):
        for i in range(4):
            self.Client[i].send.finish()

    def Manche(self):
        self.j.Paquet=paquet()
        self.j.Paquet.melangePaquet()
        self.j.Paquet.distribuer(self.j.Joueurs,52/4)               
        self.Tour()
        
    def debutManche(self):
        self.j.Paquet=paquet()
        self.j.Paquet.melangePaquet()
        self.j.Paquet.distribuer(self.j.Joueurs,52/4)    
        for i in range(2):
            if (i==0):
                up="président"
                down="prisonnier"
            else :
                up="vice-président"
                down="geolier"
            for k in range(4):
                self.j.Joueurs[k].Afini=False
                self.Client[k].send.affiche("Le {1} {0} donne sa(ses) {4} meilleures cartes au {3} {2}.".format(self.j.Joueurs[self.Classement[3-i]].nom,down,self.j.Joueurs[self.Classement[0+i]].nom,up,2-i))
            self.j.Joueurs[self.Classement[3-i]].main.trieMain()
            for j in range(i):
                self.j.Joueurs[self.Classement[0+i]].recevoirCarte(self.j.Joueurs[self.Classement[3-i]].poserCarte(12-j))
            for k in range(4):
                self.Client[k].send.affiche("Le {1} {0} donne sa(ses) {4} pires cartes au {3} {2}.".format(self.j.Joueurs[self.Classement[0+i]].nom,up,self.j.Joueurs[self.Classement[3-i]].nom,down,2-i))
            self.j.Joueurs[self.Classement[0+i]].main.trieMain()
            for j in range(i):
                self.j.Joueurs[self.Classement[3-i]].recevoirCarte(self.j.Joueurs[self.Classement[0+i]].poserCarte(0+j))
        self.Tour()


    def QuatreJoueurs(self):
        return self.cpt==4

    def tourFini(self):
        cpt=0
        for i in range(4):
            if self.j.Joueurs[i].seCouche:
                cpt+=1
        if cpt>=3:
            self.FinTour=True
        return self.FinTour

    def mancheFinie(self):
        cpt=0
        for i in range(4):
            if self.j.Joueurs[i].Afini:
                cpt+=1
        if cpt>=3:
            self.FinManche=True
        return self.FinManche

GameMaster=GameMaster()
