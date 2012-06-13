from proto import proto
from pynetez.Session import Session
from pynetez.Server  import Server
from threading import Lock
from pynetez.Agent import Agent

from pynetez.Protocol import Protocol

masterproto = Protocol()
masterproto.define("play", None, None) # agent, n

class GameMaster(Agent):

    def __init__(self, players, nbJoueurs):
        super(GameMaster, self).__init__(masterproto)
        self.nbJoueurs=nbJoueurs
        self.players=players
        self.paquet()
        self.cpt=0
        self.nbManches=0
        self.DerniereCarte=range(2)
        self.DerniereCarte[0]=1
        self.DerniereCarte[1]="H"
        self.begin.connect(self.connected)

    def connected(self):
    	for i in range(self.nbJoueurs):
        	self.players[i].send.connected()
        	self.players[0].send.go()
        for i in range(self.nbJoueurs-1):
        	self.players[i].send.wait()

    def finish(self):
        super(GameMaster, self).finish()
        for i in range(self.nbJoueurs):
        	self.players[i].finish()

    def do_play(self, player,n): # Fonction qui gère la réponse du joueur et agit en conséquence
        nb=self.cpt%self.nbJoueurs
        if player is not self.players[nb]:
            # out of turn: abort game
            for i in range(self.nbJoueurs):
            self.Joueurs[i].abort()
            self.finish()

        if self.players[nb].main.taille()<n:
            self.players[nb].send.err1()
            self.players[nb].send.go()
        if n!=0:
            if self.players[nb].main.liste[n-1].no==DerniereCarte.no:
    	        DerniereCarte=self.players[nb].main.liste[n-1]
   	        elif (self.main.liste[n-1]>DerniereCarte) :
               	DerniereCarte=self.players[nb].main.liste[n-1]
                else :
                    self.players[nb].send.err2()
            		self.players[nb].send.go()  
            else :
                return DerniereCarte
        else:
			self.DerniereCarte= self.players[nb].main.liste[n]
            for i in range(self.nbJoueurs):
            self.players[i].send.inGame(self.left)
            if self.nbManches == 3:
                # if it's a win: end game
                self.player1.send.won()
                self.player2.send.lost()
                self.finManche()
                break;
            else:
                # else switch players
                self.players[self.cpt%self.nbJoueurs].send.wait()
                cpt+=1
                self.players[self.cpt%self.nbJoueurs].send.go()
              
#Partie de jeu 

            